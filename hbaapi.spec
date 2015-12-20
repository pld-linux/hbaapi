Summary:	Fibre Channel HBA API Project
Summary(pl.UTF-8):	Projekt API dla kart kontrolerów światłowodowych
Name:		hbaapi
Version:	2.2
Release:	2
License:	SNIA Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/hbaapi/%{name}_src_%{version}.tgz
# Source0-md5:	5c9281e28f8731e38721b34494a75eef
Patch0:		%{name}-build.patch
URL:		http://hbaapi.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SNIA Common HBA API is an industry standard C language
Application Programming Interface for management of Fibre Channel Host
Bus Adapters and discovery of SAN resources. Developed through the
Storage Networking Industry Association (SNIA), the HBA API has been
overwhelmingly adopted by Storage Area Network vendors to help manage,
monitor, and deploy storage area networks. It defines a scope within
which application software can be written without attention to
vendor-specific infrastructure behavior.

%description -l pl.UTF-8
SNIA Common HBA API to przemysłowy standard interfejsu programowego
(API) języka C do zarządzania kartami kontrolerów (HBA)
światłowodowych (Fibre Channel) oraz wykrywania zasobów SAN. Stworzone
przez organizację SNIA (Storage Networking Industry Association) HBA
API zostało przytłaczająco zaadaptowane przez producentów rozwiązań
SAN (Storage Area Network) jako pomoc przy zarządzaniu, monitorowaniu
i wdrażaniu sieciowych systemów przechowywania danych. Definiuje
zakres, w jakim można tworzyć aplikacje bez uwzględniania zachowania
zależnego od producenta.

%package devel
Summary:	Header files for HBA API
Summary(pl.UTF-8):	Pliki nagłówkowe HBA API
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for HBA API.

%description devel -l pl.UTF-8
Pliki nagłówkowe HBA API.

%prep
%setup -q -n hbaapi_src_%{version}
%patch0 -p1

%build
%{__make} -f makefile.unix \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install libHBAAPI.so $RPM_BUILD_ROOT%{_libdir}
cp -p hbaapi.h vendorhbaapi.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_libdir}/libHBAAPI.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/hbaapi.h
%{_includedir}/vendorhbaapi.h
