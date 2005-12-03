#
# Conditional build:
%bcond_without	mmx		# without MMX and MMX2
%bcond_without	sse		# without SSE
%bcond_without	altivec		# without altivec
%bcond_without	static_libs	# don't build static library
#
%ifnarch i586 i686 athlon %{x8664}
%undefine	with_mmx
%endif
%ifnarch i686 athlon %{x8664}
%undefine	with_sse
%endif
%ifnarch ppc
%undefine	with_altivec
%endif
#
Summary:	Multi-platform Canvas Library
Summary(pl):	Wieloplatformowa biblioteka do rysowania
Name:		evas
Version:	0.9.9.022
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	5b4f791ee7085012e04ec3031d634c6c
#Patch0:		%{name}-missing_m4.patch
URL:		http://enlightenment.org/Libraries/Evas/
BuildRequires:	DirectFB-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edb-devel
BuildRequires:	eet-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	fonts-TTF-bitstream-vera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%description -l pl
Evas to czyste API "p³ótna obrazu" dla ró¿nych systemów wy¶wietlania,
bêd±ce w stanie rysowaæ tekst z antyaliasingiem, wyg³adzane, skalowane
obrazy, obiekty z alpha-blendingiem i inne elementy.

%package libs
Summary:	Evas library
Summary(pl):	Biblioteka evas
Group:		X11/Libraries

%description libs
Evas library.

%description libs -l pl
Biblioteka evas.

%package devel
Summary:	Evas header files
Summary(pl):	Pliki nag³ówkowe Evas
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	DirectFB-devel
Requires:	OpenGL-devel
Requires:	edb-devel
Requires:	eet-devel
Requires:	freetype-devel
Requires:	libjpeg-devel
Requires:	libpng-devel

%description devel
Header files for Evas.

%description devel -l pl
Pliki nag³ówkowe Evas.

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
%setup -q
#%%patch0 -p1

%build
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-software-x11 	\
	--disable-software-xcb	\
	--enable-directfb	\
	--enable-fb		\
	--enable-buffer		\
	--disable-software-qtopia \
	--enable-gl-x11		\
	--enable-xrender-x11	\
	--enable-image-loader-png	\
	--enable-image-loader-jpeg	\
	--enable-image-loader-eet	\
	--enable-font-loader-eet	\
	--enable-image-loader-edb	\
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
	--enable-cpu-c		\
	--disable-valgrind

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
VERA=$(ls Vera*.ttf)
for FONT in $VERA; do
	rm -f $FONT
	ln -s %{_fontsdir}/TTF/$FONT .
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
%attr(755,root,root) %{_bindir}/evas_*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevas.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/evas-config
%attr(755,root,root) %{_libdir}/libevas.so
%{_libdir}/libevas.la
%{_pkgconfigdir}/evas.pc
%{_includedir}/Evas*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libevas.a
%endif
