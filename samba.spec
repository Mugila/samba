Summary:	SMB client and server
Summary(pl):	Klient i serwer SMB
Name:		samba
Version:	2.0.3
Release:	2
Copyright:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://samba.anu.edu.au/pub/samba/%{name}-%{version}.tar.gz
Source1:	samba.PLD.tar.bz2
Patch0:		samba-glibc2.1.patch
Patch1:		samba-config.patch
Patch2:		samba-cap.patch
Prereq:		/sbin/chkconfig 
Requires:	pam >= 0.66 
BuildPrereq:	ncurses-devel
BuildPrereq:	readline-devel
BuildPrereq:	pam-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Samba provides an SMB server which can be used to provide
network services to SMB (sometimes called "Lan Manager")
clients, including various versions of MS Windows, OS/2,
and other Linux machines. Samba also provides some SMB
clients, which complement the built-in SMB filesystem
in Linux. Samba uses NetBIOS over TCP/IP (NetBT) protocols
and does NOT need NetBEUI (Microsoft Raw NetBIOS frame)
protocol.

This release is known as the "Locking Update" and has full
support for Opportunistic File Locking. In addition this update
includes native support for Microsoft encrypted passwords,
improved browse list and WINS database management.

Please refer to the WHATSNEW.txt document for fixup information.
This binary release includes encrypted password support.
Please read the smb.conf file and ENCRYPTION.txt in the
docs directory for implementation details.

%description -l pl
Samba udost�pnia serwer SMB, kt�ry mo�e by� u�yty w celu dostarczenia
us�ug sieciowych (potocznie zwanych "Lan Manager"), dla klient�w takich
jak MS Windows, OS/2 a tak�e maszyn linuxowych.  W pakiecie znajduje si�
r�wnie� oprogramowanie klienckie. Samba u�ywa protoko�u NetBIOS po TCP/IP
(NetBT) i nie wymaga protoko�u NetBEUI. Ta wersja ma pe�ne wsparcie dla
blokowania plik�w, a tak�e wsparcie dla kodowania hase� w standardzie
MS i zarzadzania baz� WINS.

UWAGA: w przeciwie�stwie do wersji 2.0.2 aktualnie samba pozbawiona jest
mozliwo�ci kontrolowania domeny NT.

%package -n swat
Summary:	Samba Web Administration Tool
Summary(pl):	Narz�dzie administracyjne serwisu Samba
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
Requires:	%{name}

%description -n swat
swat allows a Samba administrator to configure the complex smb.conf
file via a Web browser. In addition, a swat configuration page has
help links to all the configurable options in the smb.conf file
allowing an administrator to easily look up the effects of any change.

swat is run from inetd

%description -n swat -l pl
swat pozwala na kompleksow� konfiguracj� smb.conf przy pomocy przegl�darki
internetowej.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd source
autoconf
LDFLAGS="-s" export LDFLAGS \
%configure \
	--prefix=/usr \
	--sysconfdir=/etc/samba \
	--sbindir=/usr/sbin \
	--bindir=/usr/bin \
	--with-privatedir=/etc/samba \
	--libdir=/etc/samba \
	--localstatedir=/var \
	--with-swatdir=/usr/share/swat \
	--with-smbmount \
	--with-smbwrapper \
	--with-quotas \
	--with-syslog \
	--with-automount
	
make all smbwrapper bin/smbrun bin/debug2html

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/samba/codepages/src \
	$RPM_BUILD_ROOT/etc/{logrotate.d,pam.d,sysconfig} \
	$RPM_BUILD_ROOT/etc/rc.d/init.d \
	$RPM_BUILD_ROOT/home/samba \
	$RPM_BUILD_ROOT/lib/security \
	$RPM_BUILD_ROOT/usr/{bin,man/man{1,5,7,8},sbin} \
	$RPM_BUILD_ROOT/var/{lock,log,spool}/samba \
	$RPM_BUILD_ROOT/usr/share/swat/{include,images,help}

( cd source;
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	BASEDIR=$RPM_BUILD_ROOT/usr \
	BINDIR=$RPM_BUILD_ROOT/usr/bin \
	SBINDIR=$RPM_BUILD_ROOT/usr/sbin \
	LIBDIR=$RPM_BUILD_ROOT/etc/samba \
	PRIVATEDIR=$RPM_BUILD_ROOT/etc/samba \
	SWATDIR=$RPM_BUILD_ROOT/usr/share/swat \
	VARDIR=$RPM_BUILD_ROOT/var
)

install  source/codepages/codepage_def.* \
	$RPM_BUILD_ROOT/etc/samba/codepages/src

install  packaging/PLD/smb.conf		$RPM_BUILD_ROOT/etc/samba
install  packaging/PLD/smbusers		$RPM_BUILD_ROOT/etc/samba
install  packaging/PLD/smbprint		$RPM_BUILD_ROOT/usr/bin
install  packaging/PLD/smbadduser	$RPM_BUILD_ROOT/usr/bin
install  packaging/PLD/findsmb		$RPM_BUILD_ROOT/usr/bin
install  packaging/PLD/smb.init		$RPM_BUILD_ROOT/etc/rc.d/init.d/smb
install  packaging/PLD/samba.pam	$RPM_BUILD_ROOT/etc/pam.d/samba
install  packaging/PLD/samba.log	$RPM_BUILD_ROOT/etc/logrotate.d/samba

install -s source/bin/*.so 	$RPM_BUILD_ROOT/lib/security
install -s source/bin/{smbsh,smbrun,debug2html} $RPM_BUILD_ROOT/usr/bin

touch $RPM_BUILD_ROOT/var/lock/samba/{STATUS..LCK,wins.dat,browse.dat}

echo 127.0.0.1 localhost > $RPM_BUILD_ROOT/etc/samba/lmhosts

echo "NICELEVEL=+5" > $RPM_BUILD_ROOT/etc/sysconfig/samba

for i in 437 737 850 852 861 866 932 949 950 936; do
$RPM_BUILD_ROOT/usr/bin/make_smbcodepage c $i \
$RPM_BUILD_ROOT/etc/samba/codepages/src/codepage_def.$i \
$RPM_BUILD_ROOT/etc/samba/codepages/codepage.$i; done

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[1578]/* \
	README Manifest WHATSNEW.txt Roadmap docs/*.reg swat/README

%post
/sbin/chkconfig --add smb
if test -r /var/run/smb.pid; then
	/etc/rc.d/init.d/smb stop >&2
	/etc/rc.d/init.d/smb start >&2
else
	echo "Run \"/etc/rc.d/init.d/smb start\" to start samba daemons."
fi

%preun
if [ "$1" = "0" ]; then
	/etc/rc.d/init.d/smb stop >&2
	/sbin/chkconfig --del smb
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz Manifest.gz WHATSNEW.txt.gz
%doc Roadmap.gz docs/faq/*.html docs/*.reg.gz 

%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/sbin/nmbd
%attr(755,root,root) /usr/sbin/smbd

%dir /etc/samba
%config(noreplace) %verify(not size mtime md5) /etc/samba/smb.conf
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /etc/samba/smbusers
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/samba/lmhosts

%attr(750,root,root) /etc/rc.d/init.d/smb
%attr(640,root,root) %config %verify(not size mtime md5) /etc/sysconfig/samba
%attr(640,root,root) /etc/logrotate.d/samba
%attr(640,root,root) /etc/pam.d/samba

%attr(755,root,root) /lib/security/*.so

%{_mandir}/man[157]/*
%{_mandir}/man8/nmbd.8.gz
%{_mandir}/man8/smbd.8.gz
%{_mandir}/man8/smbmnt.8.gz
%{_mandir}/man8/smbmount.8.gz
%{_mandir}/man8/smbpasswd.8.gz
%{_mandir}/man8/smbumount.8.gz

%dir /home/samba
/etc/samba/codepages

%dir /var/lock/samba
%ghost /var/lock/samba/*

%attr(0750,root,root) %dir /var/log/samba
%attr(1777,root,root) %dir /var/spool/samba

%files -n swat
%defattr(644,root,root,755)
%doc swat/README.gz
%attr(755,root,root) /usr/sbin/swat
/usr/share/swat
%{_mandir}/man8/swat.8.gz

%changelog
* Wed Apr 28 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.3-2]
- added BuildPrereq rules,
- standarized %post{un} - now samba service is restarted automatically on   
  upgrade and downed on uninstall).

* Wed Apr 14 1999 Artur Frysiak <wiget@pld.org.pl>
- Changed group to Networking/Daemons
- Changed name of source1
- Added swat subpackage
- Used %configure macro
- Correct one typo in configure args
- Added --with-syslog and --with-automount to configure
- Added /etc/sysconfig/samba (allow set nice level of [sn]mbd )
- Removed %config from /etc/rc.d/init.d/smb
- Removed manuly install man and swat ( make install do it)
- Install smbrun and debug2html
- Fixed lmhosts files
- Added noreplace to config files
- Added %ghost macro to state files 

* Sun Mar 28 1999 Ziemek Borowski <zmb@ziembor.waw.pl>
  [2.0.3] 
- updated to 2.0.3 (change in samba.2.0.3.patch file)
- removed kerberos support

* Tue Jan 26 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.2.0-1d]
- updated to new version,
- added Group(pl),
- added patch against GNU libc-2.1 -- prepared by Paul Laufer
  http://www.cspupomona.edu/~pelaufer/samba,
- some other changes ...

* Wed Aug 05 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.9.18p8-1d]
- build against glibc-2.1,
  patch prepared by Paul Laufer <PELaufer@csupomona.edu>
  http://www.netcom.com/~mlaufer/samba,
- translation modified for pl,
- build with Kerberos V support,
- moved %changelog at the end of spec,
- build from non root's acccount,
- changed permisions of binaries to 755,
- moved config files to /etc/samba instead /etc,
- added a sticky bit on /var/spool/samba,
- minor modifications of spec.

* Sat Jul 4 1998 John H Terpstra <jht@samba.anu.edu.au>
  - changed classification of codepage source files
  - altered installation of samba system files
  - modified doc handling (removed attribute setting parameters)

* Sat Jun 13 1998 John H Terpstra <jht@samba.anu.edu.au>
  - Added code pages 737 and 861 to files section
  - Added auto-generation of empty /etc/lmhosts file if not exist
  - Always zap and create empty /var/lock/samba/STATUS..LCK file

* Wed Jun 10 1998 John H Terpstra <jht@samba.anu.edu.au>
  - Updated version info for 1.9.18p8 release
  - updated codepage support for pages 737 861

* Sun Apr 26 1998 John H Terpstra <jht@samba.anu.edu.au>
  - minor tidy up in preparation for release of 1.9.18p5
  - added findsmb utility from SGI package

* Wed Mar 18 1998 John H Terpstra <jht@samba.anu.edu.au>
  - Updated version and codepage info.
  - Release to test name resolve order

* Sat Jan 24 1998 John H Terpstra <jht@samba.anu.edu.au>
 - Many optimisations (some suggested by Manoj Kasichainula <manojk@io.com>
  - Use of chkconfig in place of individual symlinks to /etc/rc.d/init/smb
  - Compounded make line
  - Updated smb.init restart mechanism
  - Use compound mkdir -p line instead of individual calls to mkdir
  - Fixed smb.conf file path for log files
  - Fixed smb.conf file path for incoming smb print spool directory
  - Added a number of options to smb.conf file
  - Added smbadduser command (missed from all previous RPMs) - Doooh!
  - Added smbuser file and smb.conf file updates for username map
