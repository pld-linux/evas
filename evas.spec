#
%bcond_without	mmx		# without MMX and MMX2
%bcond_without	sse		# without SSE
%bcond_without	altivec		# without altivec
#
%ifnarch i586 i686 athlon
%undefine	with_mmx
%endif
%ifnarch i686 athlon
%undefine	with_sse
%endif
%ifnarch ppc
%undefine	with_altivec
%endif
#
Summary:	Multi-platform Canvas Library
Summary(pl):	Wieloplatformowa biblioteka do rysowania
Name:		evas
Version:	0.9.9
%define	_snap	20050329
Release:	0.%{_snap}.0.1
License:	BSD
Group:		Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}_%{_pre}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{_snap}.tar.gz
# Source0-md5:	d29b5c91e01c3eda9ff8a940dfe84398
URL:		http://enlightenment.org/
BuildRequires:	DirectFB-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	edb-devel
BuildRequires:	eet-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%description -l pl
Evas to czyste API "p��tna obrazu" dla r�nych system�w wy�wietlania,
b�d�ce w stanie rysowa� tekst z antyaliasingiem, wyg�adzane, skalowane
obrazy, obiekty z alpha-blendingiem i inne elementy.

%package devel
Summary:	Evas header files
Summary(pl):	Pliki nag��wkowe Evas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB-devel
Requires:	OpenGL-devel
Requires:	cairo-devel
Requires:	edb-devel
Requires:	eet-devel
Requires:	freetype-devel
Requires:	libjpeg-devel
Requires:	libpng-devel

%description devel
Header files for Evas.

%description devel -l pl
Pliki nag��wkowe Evas.

%package static
Summary:	Static Evas library
Summary(pl):	Statyczna biblioteka Evas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Evas library.

%description static -l pl
Statyczna biblioteka Evas.

%prep
#%%setup -q -n %{name}-%{version}_%{_pre}
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-software-x11 	\
	--enable-direct-fb	\
	--enable-fb		\
	--enable-buffer		\
	--disable-software-qtopia \
	--enable-gl-x11		\
	--enable-cairo-x11	\
%if %{with mmx}
	--enable-cpu-mmx	\
%else
	--disable-cpu-mmx	\
%endif
%if %{with sse}
	--enable-cpu-sse	\
%else
	--disable-cpu-sse	\
%endif
%if %{with altivec}
	--enable-cpu-altivec	\
%else
	--disable-cpu-altivec	\
%endif
	--enable-cpu-c

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
%doc AUTHORS README COPYING
%attr(755,root,root) %{_bindir}/evas_*
%attr(755,root,root) %{_libdir}/libevas.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/evas-config
%attr(755,root,root) %{_libdir}/libevas.so
%{_libdir}/libevas.la
%{_pkgconfigdir}/evas.pc
%{_includedir}/Evas*

%files static
%defattr(644,root,root,755)
%{_libdir}/libevas.a
