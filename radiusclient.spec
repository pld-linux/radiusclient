Summary:	Radiusclient library and tools
Summary(pl):	Biblioteka radiusclient oraz narzêdzia
Name:		radiusclient
Version:	0.3.2
Release:	2
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.cityline.net/pub/radiusclient/%{name}-%{version}.tar.gz
# Source0-md5:	dd6a85f2f6fcb944cbf1dddd05ab132f
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-nolibs.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Radiusclient is a /bin/login replacement which gets called by a getty
to log in a user and to setup the user's login environment. Normal
login programs just check the login name and password which the user
entered against the local password file (/etc/passwd, /etc/shadow). In
contrast to that Radiusclient also uses the RADIUS protocol to
authenticate the user.

%description -l pl
Radiusclient jest zamiennikiem /bin/login wywo³ywanym przez getty
w celu umo¿liwienia u¿ytkownikowi zalogowania siê. Normalne programy
typu login sprawdzaj± nazwê u¿ytkownika oraz has³o wzglêdem lokalnego
pliku (/etc/passwd, /etc/shadow). W przeciwieñstwie do nich
Radiusclient u¿ywa tak¿e protoko³u RADIUS w celu uwierzytelnienia
u¿ytkownika.

%package devel
Summary:	Header files for radiusclient library
Summary(pl):	Pliki nag³ówkowe biblioteki radiusclient
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for radiusclient library.

%description devel -l pl
Pliki nag³ówkowe biblioteki radiusclient.

%package static
Summary:	Radiusclient static library
Summary(pl):	Statyczna biblioteka radiusclient
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Radiusclient static library.

%description static -l pl
Statyczna biblioteka Radiusclient.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shadow \
	--enable-scp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES COPYRIGHT README* doc/*.html
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(750,root,root) %dir %{_sysconfdir}/radiusclient
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 size mtime) %{_sysconfdir}/radiusclient/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
