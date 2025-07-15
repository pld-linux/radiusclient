Summary:	Radiusclient library and tools
Summary(pl.UTF-8):	Biblioteka radiusclient oraz narzędzia
Name:		radiusclient
Version:	0.3.2
Release:	6
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

%description -l pl.UTF-8
Radiusclient jest zamiennikiem /bin/login wywoływanym przez getty w
celu umożliwienia użytkownikowi zalogowania się. Normalne programy
typu login sprawdzają nazwę użytkownika oraz hasło względem lokalnego
pliku (/etc/passwd, /etc/shadow). W przeciwieństwie do nich
Radiusclient używa także protokołu RADIUS w celu uwierzytelnienia
użytkownika.

%package devel
Summary:	Header files for radiusclient library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki radiusclient
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for radiusclient library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki radiusclient.

%package static
Summary:	Radiusclient static library
Summary(pl.UTF-8):	Statyczna biblioteka radiusclient
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Radiusclient static library.

%description static -l pl.UTF-8
Statyczna biblioteka Radiusclient.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES COPYRIGHT README* doc/*.html
%attr(755,root,root) %{_sbindir}/login.radius
%attr(755,root,root) %{_sbindir}/radacct
%attr(755,root,root) %{_sbindir}/radexample
%attr(755,root,root) %{_sbindir}/radlogin
%attr(755,root,root) %{_sbindir}/radstatus
%attr(755,root,root) %{_libdir}/libradiusclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libradiusclient.so.0
%attr(750,root,root) %dir %{_sysconfdir}/radiusclient
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient/dictionary
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient/dictionary.ascend
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient/dictionary.compat
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient/dictionary.merit
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient/issue
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient/port-id-map
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient/radiusclient.conf
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/radiusclient/servers

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libradiusclient.so
%{_libdir}/libradiusclient.la
%{_includedir}/radiusclient.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libradiusclient.a
