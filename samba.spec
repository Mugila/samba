#
# Conditional build:
# _without_cups	- without CUPS support
# _with_ldap	- with LDAP-based auth (instead of smbpasswd)
# _with_ipv6	- with IPv6 support
#
%define		vscan_version 0.3.4
Summary:	SMB server
Summary(cs):	Server SMB
Summary(da):	SMB server
Summary(de):	SMB-Server
Summary(es):	El servidor SMB
Summary(fi):	SMB-palvelin
Summary(fr):	Serveur SMB
Summary(it):	Server SMB
Summary(ja):	Samba SMB �����С�
Summary(ko):	��� SMB ����
Summary(pl):	Serwer SMB
Summary(pt_BR):	Cliente e servidor SMB
Summary(ru):	SMB ������ � ������
Summary(tr):	SMB sunucusu
Summary(uk):	SMB �̦��� �� ������
Summary(zh_CN):	Samba �ͻ��˺ͷ�����
Name:		samba
Version:	2.2.8a
Release:	5
Epoch:		1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.samba.org/samba/ftp/%{name}-%{version}.tar.bz2
# Source0-md5:	51466fdd7b7125a5bd41608a76e8e7c8
Source1:	smb.init
Source2:	%{name}.pamd
Source3:	swat.inetd
Source4:	%{name}.sysconfig
Source5:	%{name}.logrotate
Source6:	smb.conf
Source7:	http://dl.sourceforge.net/openantivirus/%{name}-vscan-%{vscan_version}.tar.bz2
# Source7-md5:	acbcb28cff080dcf2ee732b7f2c0f949
Patch1:		%{name}-config.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-manpages_PLD_fixes.patch
Patch4:		%{name}-smbprint.patch
Patch5:		%{name}-autoconf.patch
Patch6:		%{name}-smbadduser.patch
Patch7:		%{name}-nmbd_socket.patch
Patch8:		%{name}-vfs.patch
Patch9:		%{name}-quota.patch
Patch10:	http://v6web.litech.org/samba/%{name}-2.2.8a+IPv6-20030712.diff
Patch11:	%{name}-DESTDIR-fix.patch
Patch12:	%{name}-CIFS-extensions.patch
Patch13:	%{name}-allow-suid.patch
URL:		http://www.samba.org/
BuildRequires:	autoconf
%{!?_without_cups:BuildRequires:	cups-devel}
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	ncurses-devel >= 5.2
%{?_with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pam-devel > 0.66
BuildRequires:	popt-devel
BuildRequires:	readline-devel >= 4.2
Requires(post,preun):	/sbin/chkconfig
Requires:	logrotate
Requires:	pam >= 0.77.3
Requires:	samba-common = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/samba
%define		_vfsdir		/usr/lib/%{name}/vfs
%define		_libdir		%{_sysconfdir}
%define		_localstatedir	%{_var}/log/samba
%define		_sambahome	/home/services/samba
%if 0%{!?_without_cups:1}
%define		cups_serverbin	%(cups-config --serverbin)
%endif

%description
Samba provides an SMB server which can be used to provide network
services to SMB (sometimes called "Lan Manager") clients, including
various versions of MS Windows, OS/2, and other Linux machines. Samba
also provides some SMB clients, which complement the built-in SMB
filesystem in Linux. Samba uses NetBIOS over TCP/IP (NetBT) protocols
and does NOT need NetBEUI (Microsoft Raw NetBIOS frame) protocol.

This release is known as the "Locking Update" and has full support for
Opportunistic File Locking. In addition this update includes native
support for Microsoft encrypted passwords, improved browse list and
WINS database management.

Please refer to the WHATSNEW.txt document for fixup information. This
binary release includes encrypted password support. Please read the
smb.conf file and ENCRYPTION.txt in the docs directory for
implementation details.

%description -l cs
Samba poskytuje server SMB, kter� lze pou��t pro poskytov�n� s�ov�ch
slu�eb klient�m SMB (n�kdy naz�van�ch klienti "LAN mana�er") v�etn�
klient� r�zn�ch verz� MS Windows, OS/2 a dal��ch linuxov�ch stroj�.
Samba t� poskytuje n�kter� klienty SMB, kte�� komplementuj� vestav�n�
souborov� syst�m SMB v Linuxu. Samba pou��v� protokoly NetBIOS p�es
TCP/IP (NetBT) a NEpot�ebuje protokol NetBEUI (neform�tovan� r�mec
NetBIOS od spole�nosti Microsoft.

%description -l da
Samba tilbyder en SMB server som kan bruges til at tilbyde netv�rk
services til SMB (ogs� kaldet "Lan Manager") klienter, incl.
forskellige versioner af MS Windows, OS/2, og andre Linux maskiner.
Samba tilbyder ogs� SMB klienter, som udbygger det indbyggede SMB
filsystem i Linux. Samba benytter NetBIOS over TCP/IP (NetBT)
protocolen og kr�ver ikke NetBEUI (Microsoft Raw NetBIOS frame)
protokollen.

%description -l de
Samba stellt einen SMB-Server zum Anbieten von Netzwerkdiensten f�r
SMB-Clients (auch "Lan Manager" genannt) zur Verf�gung, darunter
verschiedenen Versionen von MS Windows-, OS/2- und anderen
Linux-Rechnern. Samba enth�lt au�erdem einige SMB-Clients, die das in
Linux integrierte SMB-Dateisystem erg�nzen. Samba benutzt
NetBIOS-�ber-TCP/IP (NetBT)-Protokolle und ben�tigt KEIN NetBEUI
(Microsoft Raw NetBIOS frame)-Protokoll.

%description -l es
Samba provee un servidor SMB que se puede usar para ofrecer servicios
de red a clientes SMB (algunas veces se le llama de "Lan Manager"),
incluyendo varias versiones de MS Windows, OS/2, y otras m�quinas
Linux. Samba tambi�n ofrece algunos clientes SMB, que complementan el
sistema de archivos SMB de Linux. Samba usa el protocolo NetBIOS sobre
TCP/IP (NetBT) y no necesita del protocolo NetBEUI (Microsoft Raw
NetBIOS frame).

%description -l fi
Samba on SMB-palvelin, jota voidaan k�ytt�� SMB-asiakasohjelmien
verkkopalvelujen tarjoajana. SMB-protokollaa kutsutaan joskus "Lan
Manager" protokollaksi ja asiakasohjelmat toimivat dosissa,
Windowseissa, OS/2:ssa ja toisissa Linux-koneissa. Samban mukana on
my�s joitakin SMB-asiakasohjelmia, jotka t�ydent�v�t Linuxin
kerneliss� olevaa SMB-tiedostoj�rjestelm�n tukea. Samba vaatii NetBIOS
over TCP/IP (NetBT) protokollaa eik� tarvitse tai pysty k�ytt�m��n
NetBEUI-protokollaa.

%description -l it
Samba fornisce un server SMB che puo` essere usato per fornire servizi
di rete ai client SMB, incluse le versioni MS Windows, OS/2 e per
altre macchine Linux. Samba fornisce anche i client SMB. Samba usa
NetBIOS sopra TCP/IP e non ha bisogno del protocollo NetBEUI.

%description -l ja
Samba �� MS Windows ���͡��ʥС������OS/2 ������¾�� Linux �ޥ���
��ޤ� SMB (���ޤ� "Lan Manager" �ȸƤФ��)
���饤����Ȥ˥ͥåȥ�� �����ӥ����󶡤��뤿��˻��Ѥ���� SMB
�����Ф��󶡤��ޤ���Samba �� NetBIOS over TCP/IP (NetBT)
�ץ�ȥ������Ѥ��� NetBEUI(Microsoft Raw NetBIOS frame)
�ץ�ȥ����ɬ�פ���ޤ���

Samba �ۤȤ��ư��� NT �ɥᥤ�󥳥�ȥ���ε�ǽ����ħ�Ȥ���
�����ʥ֥饦����Ȥä� samba �� smb.conf �ե�������⡼�ȴ�������
������ SWAT (Samba Web Administration Tool) ��ޤߤޤ���
�ܲ��ΤȤ������ inetd ���̤��� TCP �ݡ��� 901 ��ͭ���ˤʤ�ޤ���

%description -l ko
��ٴ� MS Windows, OS/2, Ȥ�� �ٸ� ������ �ӽ��� �����ϴ� SMB(Ȥ��
"Lan Manager"��� �Ҹ�) Ŭ���̾�Ʈ�� ��Ʈ��ũ ���� ���� ����� ��
�ִ� SMB ������ �����Ѵ�. ��ٴ� TCP/IP ���������� ���� NetBIOS��
����ϰ� NetBEUI (Microsoft Raw NetBIOS ������) ���������� �ʿ�����
�ʴ�.

���-2.2 �� Ư¡�� NT ������ ��Ʈ���� �������� �۾��� �ϰ�, ���ο�
SWAT(Samba Web Administration Tool)�� ���������� ����Ͽ� ����������
����� smb.conf ������ �����ϵ��� �Ѵ�. �̷��� ��� inetd ������ ����
TCP 901 ��Ʈ�� ����ϰ� �ȴ�.

�ֱ� ������ WHATSNEW.txt ������ ������ �����ϵ��� �Ѵ�. ���̳ʸ���
������� ��ȣȭ�� �н����带 �����Ѵ�. ������ ���� �ڼ��� ������ ���
���� docs ���丮���� �ִ� smb.conf ���ϰ� ENCRYPTION.txt ������
�о��.

%description -l pl
Samba udost�pnia serwer SMB, kt�ry mo�e by� u�yty w celu dostarczenia
us�ug sieciowych (potocznie zwanych "Lan Manager"), dla klient�w
takich jak MS Windows, OS/2 a tak�e maszyn linuksowych. W pakiecie
znajduje si� r�wnie� oprogramowanie klienckie. Samba u�ywa protoko�u
NetBIOS po TCP/IP (NetBT) i nie wymaga protoko�u NetBEUI. Ta wersja ma
pe�ne wsparcie dla blokowania plik�w, a tak�e wsparcie dla kodowania
hase� w standardzie MS i zarzadzania baz� WINS.

%description -l pt_BR
O Samba prov� um servidor SMB que pode ser usado para oferecer
servi�os de rede a clientes SMB (algumas vezes chamado de "Lan
Manager"), incluindo v�rias vers�es de MS Windows, OS/2, e outras
m�quinas Linux. O Samba tamb�m fornece alguns clientes SMB, que
complementam o sistema de arquivos SMB do Linux. O Samba usa o
protocolo NetBIOS sobre TCP/IP (NetBT) e n�o necessita do protocolo
NetBEUI (Microsoft Raw NetBIOS frame).

O Samba inclui a maioria das caracter�sticas de um servidor de
Controle de Dom�nios NT e o SWAT (Samba Web Administration Tool), que
permite que o arquivo smb.conf seja gerenciado remotamente atrav�s de
um navegador. Atualmente isto est� sendo habilitado na porta TCP 901
via inetd.

%description -l ru
Samba ������������� SMB-������, ������� ����� ���� ����������� ���
�������������� ������� �������� SMB (������ ���������� "Lan Manager")
��������, ������� ������������� ������ MS Windows, OS/2, � ������
Linux-������. Samba ����� ������������� SMB-��������, ������� ��������
�� ���������� � Linux �������� �������� SMB.

Samba ���������� �������� NetBIOS over TCP/IP (NetBT) � �� ��������� �
��������� NetBEUI (Microsoft Raw NetBIOS frame).

Samba �������� ����������� ���������� ���������� NT Domain Control �
�������� ����� SWAT (Samba Web Administration Tool), ������� ���������
�������� ��������� ���������������� ������ smb.conf ��� ������ ������
�������� WEB-��������. ���� ��� �� �������� ����� inetd �� TCP-�����
901.

%description -l uk
Samba ����� SMB-������, �� ���� ���� ������������ ��� �������
��������� ���צӦ� SMB (�� �� ���Ħ ��������� "Lan Manager") �̦�����,
��������� Ҧ�����Φ�Φ ���Ӧ� MS Windows, OS/2, �� ��ۦ Linux-������.
Samba ����� ����� SMB-�̦��Ԧ�, �� �������� � ���������� � Linux
�������� �������� SMB.

Samba ����������դ �������� NetBIOS over TCP/IP (NetBT) �� �� ������դ
��������� NetBEUI (Microsoft Raw NetBIOS frame).

Samba ͦ����� ����� �������� �������æ� NT Domain Control �� �����
SWAT (Samba Web Administration Tool), ������ ������Ѥ צ�������
�������� ���Ʀ����æ���� ������ smb.conf �� ��������� ������
���������� WEB-��������. ���� �� צ� ���������� ����� inetd ��
TCP-����� 901.

%package -n swat
Summary:	Samba Web Administration Tool
Summary(es):	Samba SWAT and Web documentation
Summary(pl):	Narz�dzie administracyjne serwisu Samba
Summary(pt_BR):	Samba SWAT e documenta��o Web
Summary(ru):	��������� ������������ SMB-������� Samba
Summary(uk):	�������� ���������æ� SMB-������� Samba
Group:		Networking/Admin
Requires:	%{name}
Requires:	rc-inetd >= 0.8.2
Requires:	inetdaemon
Provides:	samba-swat
Obsoletes:	samba-swat

%description -n swat
swat allows a Samba administrator to configure the complex smb.conf
file via a Web browser. In addition, a swat configuration page has
help links to all the configurable options in the smb.conf file
allowing an administrator to easily look up the effects of any change.

%description -n swat -l pl
swat pozwala na kompleksow� konfiguracj� smb.conf przy pomocy
przegl�darki WWW.

%description -n swat -l pt_BR
SWAT - ferramentada Web de configura��o do Samba.

%description -n swat -l ru
����� samba-swat �������� ����� SWAT (Samba Web Administration Tool),
��� ���������� ����������������� ����� smb.conf ��� ������ ������
�������� Web-��������.

%description -n swat -l uk
����� samba-swat ͦ����� ����� SWAT (Samba Web Administration Tool),
��� ������æ����� ��ͦΦ��������� ����� smb.conf �� ��������� ������
���������� Web-��������.

%package client
Summary:	Samba client programs
Summary(es):	Cliente SMB de Samba
Summary(ja):	Samba (SMB) ���饤����ȥץ����
Summary(pl):	Klienci serwera Samba
Summary(pt_BR):	Cliente SMB do samba
Summary(ru):	���������� ��������� Samba (SMB)
Summary(uk):	�̦�����˦ �������� Samba (SMB)
Group:		Applications/Networking
Requires:	samba-common = %{version}
Obsoletes:	smbfs

%description client
Samba-client provides some SMB clients, which complement the build-in
SMB filesystem in Linux. These allow accessing of SMB shares and
printing to SMB printers.

%description client -l pt_BR
O pacote samba-clientes prove alguns clientes SMB, que complementam o
sistema de arquivos SMB do Linux. Eles permitem o acesso a shares SMB,
e tamb�m, � impressoras SMB.

%description client -l es
Cliente SMB de Samba.

%description client -l ja
Samba-client �� Linux ��˴ޤޤ�Ƥ��� SMB �ե����륷���ƥ���䤦 SMB
���饤����Ȥ��󶡤��ޤ��������� SMB ��ͭ�Υ��������� SMB
�ץ�󥿤ؤΰ�������Ĥ��ޤ���

%description client -l pl
Samba-client dostarcza pewne programy kt�re uzupe�niaj� system plik�w
SMB zawarty w j�drze. Pozwala na wsp�dzielenie i drukowanie w sieci
SMB.

%description client -l pt_BR
O pacote samba-clientes prove alguns clientes SMB, que complementam o
sistema de arquivos SMB do Linux. Eles permitem o acesso a shares SMB,
e tamb�m, � impressoras SMB.

%description client -l ru
����� samba-client ������������� ��������� ������� SMB ��� ������ ��
���������� �������� �������� SMB � Linux. ��� ������� ���������
�������� ������ � ����������� ��������� SMB � ������ �� SMB-��������.

%description client -l uk
����� samba-client ����� ���˦ �̦���� SMB ��� ������ ڦ ����������
�������� �������� SMB � Linux. � �̦���� ���������� ���������� ������
�� ������Ǧ� �Ц������ ������������ SMB �� ���� �� SMB-�Ҧ�����.

%package common
Summary:	Files used by both Samba servers and clients
Summary(es):	Common files between samba and samba-clients
Summary(ja):	Samba �����С��ȥ��饤����Ȥǻ��Ѥ����ץ����
Summary(pl):	Pliki u�ywane przez serwer i klient�w Samba
Summary(pt_BR):	Arquivos em comum entre samba e samba-clients
Summary(ru):	�����, ������������ ��� ��������, ��� � �������� Samba
Summary(uk):	�����, �� ���������������� �� ��������, ��� � �̦����� Samba
Group:		Networking/Daemons

%description common
Samba-common provides files necessary for both the server and client
packages of Samba.

%description common -l ja
Samba-common �� Samba �Υ����Фȥ��饤����Ȥ�ξ���Υѥå�������
���Ѥ����ե�������󶡤��ޤ���

%description common -l pl
Samba-common dostarcza pliki niezb�dne zar�wno dla serwera jak i
klient�w Samba.

%description common -l pt_BR
Arquivos em comum entre os pacotes samba e samba-clients.

%description common -l ru
Samba-common �������� �����, ����������� ��� ������ ��� �������, ��� �
������� Samba.

%description common -l uk
Samba-common ͦ����� �����, ����Ȧ�Φ ��� ������ �� �̦����, ��� �
������� Samba.

%package -n pam-pam_smbpass
Summary:	PAM Samba Password Module
Summary(pl):	Modu� PAM smbpass
Group:		Base
Obsoletes:	pam_smbpass

%description -n pam-pam_smbpass
PAM module which can be used on conforming systems to keep the
smbpasswd (Samba password) database in sync with the unix password
file.

%description -n pam-pam_smbpass -l pl
Modu� PAMa, kt�ry mo�e by� u�ywany do trzymania pliku smbpasswd (has�a
Samby) zsynchronizowanego z has�ami unixowymi.

%package -n libsmbclient
Summary:	libsmbclient - samba client library
Summary(pl):	libsmbclient - biblioteka klienta samby
Group:		Libraries

%description -n libsmbclient
libsmbclient - library that allows to use samba clients functions.

%description -n libsmbclient -l pl
libsmbclient - biblioteka pozwalaj�ca korzysta� z funcji klienta
samby.

%package -n libsmbclient-devel
Summary:	libsmbclient - samba client library
Summary(pl):	libsmbclient - biblioteka klienta samby
Summary(pt_BR):	Ferramentas de desenvolvimento para clientes samba
Group:		Development/Libraries
Requires:	libsmbclient = %{version}

%description -n libsmbclient-devel
Header files for libsmbclient.

%description -n libsmbclient-devel -l pl
Pliki nag��wkowe dla libsmbclient.

%description -n libsmbclient-devel -l pt_BR
Arquivos de inclus�o, bibliotecas e documenta��o necess�rios para
desenvolver aplicativos clientes para o samba.

%package -n cups-backend-smb
Summary:	CUPS backend for printing to SMB printers
Summary(pl):	Backend CUPS-a drukuj�cy na drukarkach SMB
Group:		Applications/Printing
Requires:	cups
Requires:	samba-client = %{version}

%description -n cups-backend-smb
CUPS backend for printing to SMB printers.

%description -n cups-backend-smb -l pl
Backend CUPS-a drukuj�cy na drukarkach SMB.

%package vfs-audit
Summary:	VFS module to audit file access
Summary(pl):	Modu� VFS do monitorowania operacji na plikach
Group:		Networking/Daemons
Requires:	samba = %{version}

%description vfs-audit
A simple module to audit file access to the syslog facility. The
following operations are logged: share connect/disconnect, directory
opens/create/remove, file open/close/rename/unlink/chmod.

%description vfs-audit -l pl
Prosty modu� do monitorowania dost�pu do plik�w do sysloga.
Monitorowane s� nast�puj�ce operacje: pod��czone/od��czenie do zasobu,
otwarcie/utworzenie/zmiana nazwy katalogu, otwarcie/zamkn�cie/zmiana
nazwy/skasowania/zmiana praw plik�w.

%package vfs-block
Summary:	VFS module to block access to files
Summary(pl):	Modu�y VFS do blokowania dost�pu do plik�w
Group:		Networking/Daemons
Requires:	samba = %{version}

%description vfs-block
Sample module by Ronald Kuetemeier <ronald@kuetemeier.com> to block
named symbolic link following. Note: Config file is in
/etc/samba/samba-block.conf .

%description vfs-block -l pl
Przyk�adowy modu� stworzony przez Ronald Kuetemeier
<ronald@kuetemeier.com> do blokowania dost�pu do plik�w wskazywanych
przez linki symboliczne. Plik konfiguracyjny w
/etc/samba/samba-block.conf .

%package vfs-recycle
Summary:	VFS module to add recycle bin facility to a samba share
Summary(pl):	Modu� VFS dodaj�cy mo�liwo�� kosza do zasobu samby
Group:		Networking/Daemons
Requires:	samba = %{version}

%description vfs-recycle
VFS module to add recycle bin facility to a samba share.

%description vfs-recycle -l pl
Modu� VFS dodaj�cy mo�liwo�� kosza do zasobu samby.

%package vfs-vscan-clamav
Summary:	On-access virus scanning for samba using ClamAV
Summary(pl):	Skaner antywirusowy online wykorzystuj�cy ClamAV
Group:		Networking/Daemons
Provides:	%{name}-vscan
Requires:	clamav
Requires:	samba = %{version}

%description vfs-vscan-clamav
A vfs-module for samba to implement on-access scanning using the ClamAV
antivirus software (which must be installed to use this).

%description vfs-vscan-clamav -l pl
Modu� vfs do samby implementuj�cy skaning antywirusowy w czasie
dost�pu do plik�w korzystaj�c z oprogramowania antywirusowego
ClamAV (kt�re musi by� zainstalowane, aby wykorzysta� ten modu�).

%package vfs-vscan-fprot
Summary:	On-access virus scanning for samba using FPROT
Summary(pl):	Skaner antywirusowy online wykorzystuj�cy FPROT
Group:		Networking/Daemons
Obsoletes:	vscan-fprot
Provides:	%{name}-vscan
Requires:	samba = %{version}

%description vfs-vscan-fprot
A vfs-module for samba to implement on-access scanning using the FPROT
antivirus software (which must be installed to use this).

%description vfs-vscan-fprot -l pl
Modu� vfs do samby implementuj�cy skaning antywirusowy w czasie
dost�pu do plik�w korzystaj�c z oprogramowania antywirusowego
FPROT (kt�re musi by� zainstalowane, aby wykorzysta� ten modu�).

%package vfs-vscan-openantivirus
Summary:	On-access virus scanning for samba using OpenAntivirus
Summary(pl):	Modu� VFS dodaj�cy obs�ug� antywirusa OpenAntiVirus
Group:		Networking/Daemons
Obsoletes:	vscan-openantivirus
Provides:	%{name}-vscan
Requires:	samba = %{version}

%description vfs-vscan-openantivirus
A vfs-module for samba to implement on-access scanning using the
OpenAntivirus antivirus software (which must be installed to use
this).

%description vfs-vscan-openantivirus -l pl
Modu� vfs do samby implementuj�cy skaning antywirusowy w czasie
dost�pu do plik�w korzystaj�c z oprogramowania antywirusowego
OpenAntiVirus.org (kt�re musi by� zainstalowane, aby wykorzysta� ten
modu�).

%package vfs-vscan-sophos
Summary:	On-access virus scanning for samba using Sophos
Summary(pl):	Modu� VFS dodaj�cy obs�ug� antywirusa Sophos
Group:		Networking/Daemons
Obsoletes:	vscan-sophos
Provides:	%{name}-vscan
Requires:	samba = %{version}

%description vfs-vscan-sophos
A vfs-module for samba to implement on-access scanning using the
Sophos antivirus software (which must be installed to use this).

%description vfs-vscan-sophos -l pl
Modu� vfs do samby implementuj�cy skaning antywirusowy w czasie
dost�pu do plik�w korzystaj�c z oprogramowania antywirusowego Sophos
(kt�re musi by� zainstalowane, aby wykorzysta� ten modu�).

%package vfs-vscan-symantec
Summary:	On-access virus scanning for samba using Symantec
Summary(pl):	Skaner antywirusowy online wykorzystuj�cy Symantec
Group:		Networking/Daemons
Obsoletes:	vscan-symantec
Provides:	%{name}-vscan
Requires:	samba = %{version}

%description vfs-vscan-symantec
A vfs-module for samba to implement on-access scanning using the
Symantec antivirus software (which must be installed to use this).

%description vfs-vscan-symantec -l pl
Modu� vfs do samby implementuj�cy skaning antywirusowy w czasie
dost�pu do plik�w korzystaj�c z oprogramowania antywirusowego firmy
Symantec (kt�re musi by� zainstalowane, aby wykorzysta� ten modu�).

%package vfs-vscan-trend
Summary:	On-access virus scanning for samba using Trend
Summary(pl):	Modu� VFS dodaj�cy obs�ug� antywirusa Trend
Group:		Networking/Daemons
Obsoletes:	vscan-trend
Provides:	%{name}-vscan
Requires:	samba = %{version}

%description vfs-vscan-trend
A vfs-module for samba to implement on-access scanning using the Trend
antivirus software (which must be installed to use this).

%description vfs-vscan-trend -l pl
Modu� vfs do samby implementuj�cy skaning antywirusowy w czasie
dost�pu do plik�w korzystaj�c z oprogramowania antywirusowego Trend
(kt�re musi by� zainstalowane, aby wykorzysta� ten modu�).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p2
%patch7 -p1
#%patch8 -p1
#%patch9 -p1
%{?_with_ipv6:%patch10 -p1}
%patch11 -p1
#%patch12 -p1
%patch13 -p1

cd examples/VFS
tar xjf %{SOURCE7}

%build
cd source
%{__autoconf}
%configure \
	--with-acl-support \
	--with-automount \
	--with-libsmbclient \
	--with-lockdir=/var/lock/samba \
	--with-mmap \
	--with-msdfs \
	--with-netatalk \
	--without-smbwrapper \
	--with-pam \
	--with-piddir=/var/run \
	--with-privatedir=%{_libdir} \
	--with-quotas \
	--with-readline \
	--with-smbmount \
	--with-ssl \
	--with-sslinc=%{_prefix} \
	--with-swatdir=%{_datadir}/swat \
	--with-syslog \
	--with-utmp \
	--with-vfs \
	%{?_with_ipv6:--with-ipv6} \
	%{?_with_ldap:--with-ldapsam}

#	--with-acl-support \
mv Makefile Makefile.old
sed -e "s#-symbolic##g" Makefile.old > Makefile

%{__make} everything pam_smbpass

cd ../examples/VFS
%{__autoconf}
%configure
%{__make}
mv README{,.vfs}

cd samba-vscan-%{vscan_version}
# use autoconf?
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,rc.d/init.d,pam.d,security,sysconfig/rc-inetd} \
	$RPM_BUILD_ROOT/var/{lock,log,log/archiv,spool}/samba \
	$RPM_BUILD_ROOT/{sbin,lib/security,%{_libdir},%{_vfsdir},%{_includedir},%{_sambahome}}

cd source
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install script/mksmbpasswd.sh /$RPM_BUILD_ROOT%{_sbindir}
cd ..

ln -sf %{_bindir}/smbmount $RPM_BUILD_ROOT/sbin/mount.smbfs

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/smb
install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/samba
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/swat
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/samba
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/samba
install %{SOURCE6} $RPM_BUILD_ROOT%{_libdir}/smb.conf

install source/nsswitch/libnss_winbind.so	$RPM_BUILD_ROOT/lib/libnss_winbind.so.2
install source/nsswitch/pam_winbind.so	$RPM_BUILD_ROOT/lib/security/
install source/bin/pam_smbpass.so	$RPM_BUILD_ROOT/lib/security/
install source/bin/wbinfo		$RPM_BUILD_ROOT%{_bindir}

install source/bin/libsmbclient.so $RPM_BUILD_ROOT/lib/libsmbclient.so.0
ln -s libsmbclient.so.0 $RPM_BUILD_ROOT/lib/libsmbclient.so

install source/include/libsmbclient.h $RPM_BUILD_ROOT%{_includedir}

# przyk�adowe modu�y VFS
install examples/VFS/{*.so,block/*.so,recycle/*.so} $RPM_BUILD_ROOT%{_vfsdir}
install examples/VFS/block/samba-block.conf examples/VFS/recycle/recycle.conf $RPM_BUILD_ROOT%{_sysconfdir}

# modu�y vscan
install examples/VFS/samba-vscan-%{vscan_version}/*.so $RPM_BUILD_ROOT%{_vfsdir}
install examples/VFS/samba-vscan-%{vscan_version}/*/*.conf $RPM_BUILD_ROOT%{_sysconfdir}

touch $RPM_BUILD_ROOT/var/lock/samba/{STATUS..LCK,wins.dat,browse.dat}

echo 127.0.0.1 localhost > $RPM_BUILD_ROOT%{_libdir}/lmhosts

%if 0%{!?_without_cups:1}
install -d $RPM_BUILD_ROOT%{cups_serverbin}/backend
ln -s %{_bindir}/smbspool $RPM_BUILD_ROOT%{cups_serverbin}/backend/smb
%endif

> $RPM_BUILD_ROOT%{_libdir}/smbusers
> $RPM_BUILD_ROOT/etc/security/blacklist.samba

rm -f docs/faq/*.{sgml,txt}
rm -f docs/htmldocs/*.[0-9].html

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add smb
if [ -r /var/lock/subsys/smb ]; then
	/etc/rc.d/init.d/smb restart >&2
else
	echo "Run \"/etc/rc.d/init.d/smb start\" to start Samba daemons."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/smb ]; then
		/etc/rc.d/init.d/smb stop >&2
	fi
	/sbin/chkconfig --del smb
fi

%post -n swat
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun -n swat
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%triggerpostun -- samba < 1.9.18p7
if [ "$1" != "0" ]; then
	/sbin/chkconfig --add smb
fi

%triggerpostun -- samba < 2.0.5a-3
if [ "$1" != "0" ]; then
	[ ! -d /var/lock/samba ] && mkdir -m 0755 /var/lock/samba
	[ ! -d /var/spool/samba ] && mkdir -m 1777 /var/spool/samba
fi

%files
%defattr(644,root,root,755)
%doc source/nsswitch/README examples/VFS/README.vfs
%attr(755,root,root) %{_sbindir}/nmbd
%attr(755,root,root) %{_sbindir}/smbd
%attr(755,root,root) %{_sbindir}/winbindd
%attr(755,root,root) %{_sbindir}/mksmbpasswd.sh
%attr(755,root,root) %{_bindir}/smbstatus
%attr(755,root,root) %{_bindir}/smbpasswd
%attr(755,root,root) %{_bindir}/smbcontrol
%attr(755,root,root) %{_bindir}/tdbbackup

%attr(755,root,root) /lib/libnss_*
%attr(755,root,root) /lib/security/pam_winbind.so

%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_libdir}/smbusers
%attr(754,root,root) /etc/rc.d/init.d/smb
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/samba
%attr(640,root,root) /etc/logrotate.d/samba
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/samba
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.samba
%{_mandir}/man1/smbstatus.1*
%{_mandir}/man1/smbcontrol.1*
%{_mandir}/man5/smbpasswd.5*
%{_mandir}/man7/samba.7*
%{_mandir}/man8/nmbd.8*
%{_mandir}/man8/smbd.8*
%{_mandir}/man8/smbpasswd.8*
%{_mandir}/man8/pdbedit.8*
%{_mandir}/man8/winbindd.8*

%dir %{_sambahome}
%dir /var/lock/samba
%ghost /var/lock/samba/*

%attr(0750,root,root) %dir /var/log/samba
%attr(0750,root,root) %dir /var/log/archiv/samba
%attr(1777,root,root) %dir /var/spool/samba

%files client
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/mount.smbfs
%attr(755,root,root) %{_bindir}/smbmount
%attr(755,root,root) %{_bindir}/smbmnt
%attr(755,root,root) %{_bindir}/smbumount
%{_mandir}/man8/smbmnt.8*
%{_mandir}/man8/smbmount.8*
%{_mandir}/man8/smbumount.8*
%attr(755,root,root) %{_bindir}/nmblookup
%attr(755,root,root) %{_bindir}/smbclient
%attr(755,root,root) %{_bindir}/smbtar
%attr(755,root,root) %{_bindir}/smbcacls
%{_mandir}/man1/smbtar.1*
%{_mandir}/man1/smbclient.1*
%{_mandir}/man1/nmblookup.1*
%{_mandir}/man1/smbcacls.1*
%{_mandir}/man1/smbsh.1*
%attr(755,root,root) %{_bindir}/rpcclient
%{_mandir}/man1/rpcclient.1*
%attr(755,root,root) %{_bindir}/wbinfo
%{_mandir}/man1/wbinfo.1*
%attr(755,root,root) %{_bindir}/findsmb
%{_mandir}/man1/findsmb.1*

%files common
%defattr(644,root,root,755)
%doc README Manifest WHATSNEW.txt
%doc Roadmap docs/faq docs/Registry/*
%doc docs/textdocs/* docs/htmldocs/*.* docs/{history,announce,THANKS}
%dir %{_libdir}
%config(noreplace) %verify(not size mtime md5) %{_libdir}/smb.conf
%config(noreplace) %verify(not size mtime md5) %{_libdir}/lmhosts
%attr(755,root,root) %{_bindir}/make_smbcodepage
%attr(755,root,root) %{_bindir}/make_unicodemap
%attr(755,root,root) %{_bindir}/testparm
%attr(755,root,root) %{_bindir}/testprns
%attr(755,root,root) %{_bindir}/make_printerdef
%{_libdir}/codepages
%{_mandir}/man1/make_smbcodepage.1*
%{_mandir}/man1/make_unicodemap.1*
%{_mandir}/man1/testparm.1*
%{_mandir}/man1/testprns.1*
%{_mandir}/man5/smb.conf.5*
%{_mandir}/man5/lmhosts.5*

%files -n swat
%defattr(644,root,root,755)
%doc swat/README* swat/help/*
%attr(755,root,root) %{_sbindir}/swat
%{_datadir}/swat
%{_mandir}/man8/swat.8*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/swat

%files -n pam-pam_smbpass
%defattr(644,root,root,755)
%doc source/pam_smbpass/{CHAN*,README,TODO} source/pam_smbpass/samples
%attr(755,root,root) /lib/security/pam_smbpass.so

%files -n libsmbclient
%defattr(644,root,root,755)
%attr(755,root,root) /lib/libsmbclient.so.*

%files -n libsmbclient-devel
%defattr(644,root,root,755)
%{_includedir}/libsmbclient.h
%attr(755,root,root) /lib/libsmbclient.so

%if 0%{!?_without_cups:1}
%files -n cups-backend-smb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smbspool
%attr(755,root,root) %{cups_serverbin}/backend/smb
%{_mandir}/man8/smbspool.8*
%endif

%files vfs-block
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/samba-block.conf
%attr(755,root,root) %{_vfsdir}/block.so

%files vfs-audit
%defattr(644,root,root,755)
%attr(755,root,root) %{_vfsdir}/audit.so

%files vfs-recycle
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/recycle.conf
%attr(755,root,root) %{_vfsdir}/recycle.so
%doc examples/VFS/recycle/README

%files vfs-vscan-clamav
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vscan-clamav.conf
%attr(755,root,root) %{_vfsdir}/vscan-clamav.so
%doc examples/VFS/%{name}-vscan-%{vscan_version}/{INSTALL,FAQ}

%files vfs-vscan-fprot
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vscan-fprotd.conf
%attr(755,root,root) %{_vfsdir}/vscan-fprotd.so
%doc examples/VFS/%{name}-vscan-%{vscan_version}/{INSTALL,FAQ}

%files vfs-vscan-openantivirus
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vscan-oav.conf
%attr(755,root,root) %{_vfsdir}/vscan-oav.so
%doc examples/VFS/%{name}-vscan-%{vscan_version}/{INSTALL,FAQ}

%files vfs-vscan-sophos
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vscan-sophos.conf
%attr(755,root,root) %{_vfsdir}/vscan-sophos.so
%doc examples/VFS/%{name}-vscan-%{vscan_version}/{INSTALL,FAQ}

%files vfs-vscan-symantec
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vscan-icap.conf
%attr(755,root,root) %{_vfsdir}/vscan-icap.so
%doc examples/VFS/%{name}-vscan-%{vscan_version}/{INSTALL,FAQ}

%files vfs-vscan-trend
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vscan-trend.conf
%attr(755,root,root) %{_vfsdir}/vscan-trend.so
%doc examples/VFS/%{name}-vscan-%{vscan_version}/{INSTALL,FAQ}
