#
# Conditional build:
%bcond_without	mmx		# without MMX and MMX2
%bcond_without	sse		# without SSE
%bcond_without	altivec		# without altivec
%bcond_without	directfb	# build without DirectFB support
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
Version:	0.9.9.032
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	f7cedd3e75290bc8a8220b8081a14018
URL:		http://enlightenment.org/Libraries/Evas/
%{?with_directfb:BuildRequires:	DirectFB-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edb-devel
BuildRequires:	eet-devel
BuildRequires:	freetype-devel
BuildRequires:	libgif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
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
%{?with_directfb:Requires:	DirectFB-devel}
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

##### MODULES #####
# engines:
%package engine-buffer
Summary:	Buffer rendering engine module for Evas
Summary(pl):	Modu³ silnika renderuj±cego do bufora dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-buffer
Memory Buffer rendering engine module for Evas.

%description engine-buffer -l pl
Modu³ silnika renderuj±cego do bufora dla Evas.

%package engine-directfb
Summary:	Directfb rendering engine module for Evas
Summary(pl):	Modu³ silnika renderuj±cego na Directfb dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description engine-directfb
Directfb rendering engine module for Evas.

%description engine-directfb -l pl
Modu³ silnika renderuj±cego na Directfb dla Evas.

%package engine-fb
Summary:	Framebuffer rendering engine module for Evas
Summary(pl):	Modu³ silnika renderuj±cego na framebuffer dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-fb
Framebuffer rendering engine module for Evas.

%description engine-fb -l pl
Modu³ silnika renderuj±cego na framebuffer dla Evas.

%package engine-gl_x11
Summary:	OpenGL under X11 rendering engine module for Evas
Summary(pl):	Modu³ silnika renderuj±cego na OpenGL pod X11 dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description engine-gl_x11
OpenGL under X11 rendering engine module for Evas.

%description engine-gl_x11 -l pl
Modu³ silnika renderuj±cego na OpenGL pod X11 dla Evas.

%package engine-software_generic
Summary:	Software rendering common engine module for Evas
Summary(pl):	Modu³ wspólnego programowego silnika renderuj±cego dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description engine-software_generic
Software rendering common engine module for Evas.

%description engine-software_generic -l pl
Modu³ wspólnego programowego silnika renderuj±cego dla Evas.

%package engine-software_qtopia
Summary:	Qtopia rendering engine module for Evas
Summary(pl):	Modu³ silnika renderuj±cego Qtopia dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-software_qtopia
Qtopia rendering engine module for Evas.

%description engine-software_qtopia -l pl
Modu³ silnika renderuj±cego Qtopia dla Evas.

%package engine-software_x11
Summary:	Software X11 rendering engine module for Evas
Summary(pl):	Modu³ programowego silnika renderuj±cego X11 dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-software_x11
Software X11 rendering engine module for Evas.

%description engine-software_x11 -l pl
Modu³ programowego silnika renderuj±cego X11 dla Evas.

%package engine-software_xcb
Summary:	Software XCB X11 rendering engine module for Evas
Summary(pl):	Modu³ programowego silnika renderuj±cego XCB X11 dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-software_xcb
Software XCB X11 rendering engine module for Evas.

%description engine-software_xcb -l pl
Modu³ programowego silnika renderuj±cego XCB X11 dla Evas.

%package engine-xrender_x11
Summary:	XRender rendering engine module for Evas
Summary(pl):	Modu³ silnika renderuj±cego XRender dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-xrender_x11
XRender rendering engine module for Evas.

%description engine-xrender_x11 -l pl
Modu³ silnika renderuj±cego XRender dla Evas.

# loaders:
%package loader-edb
Summary:	EDB Image loader module for Evas
Summary(pl):	Modu³ wczytywania obrazów EDB dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description loader-edb
EDB Image loader module for Evas.

%description loader-edb -l pl
Modu³ wczytywania obrazów EDB dla Evas.

%package loader-eet
Summary:	EET Image loader module for Evas
Summary(pl):	Modu³ wczytywania obrazów EET dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description loader-eet
EET Image loader module for Evas.

%description loader-eet -l pl
Modu³ wczytywania obrazów EET dla Evas.

%package loader-gif
Summary:	GIF Image loader module for Evas
Summary(pl):	Modu³ wczytywania obrazów GIF dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description loader-gif
GIF Image loader module for Evas.

%description loader-gif -l pl
Modu³ wczytywania obrazów GIF dla Evas.

%package loader-jpeg
Summary:	JPEG Image loader module for Evas
Summary(pl):	Modu³ wczytywania obrazów JPEG dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description loader-jpeg
JPEG Image loader module for Evas.

%description loader-jpeg -l pl
Modu³ wczytywania obrazów JPEG dla Evas.

%package loader-png
Summary:	PNG Image loader module for Evas
Summary(pl):	Modu³ wczytywania obrazów PNG dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description loader-png
PNG Image loader module for Evas.

%description loader-png -l pl
Modu³ wczytywania obrazów PNG dla Evas.

%package loader-tiff
Summary:	TIFF Image loader module for Evas
Summary(pl):	Modu³ wczytywania obrazów TIFF dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description loader-tiff
TIFF Image loader module for Evas.

%description loader-tiff -l pl
Modu³ wczytywania obrazów TIFF dla Evas.

# savers:
%package saver-edb
Summary:	EDB Image saver module for Evas
Summary(pl):	Modu³ zapisywania obrazów EDB dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description saver-edb
EDB Image saver module for Evas.

%description saver-edb -l pl
Modu³ zapisywania obrazów EDB dla Evas.

%package saver-eet
Summary:	EET Image saver module for Evas
Summary(pl):	Modu³ zapisywania obrazów EET dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description saver-eet
EET Image saver module for Evas.

%description saver-eet -l pl
Modu³ zapisywania obrazów EET dla Evas.

%package saver-jpeg
Summary:	JPEG Image saver module for Evas
Summary(pl):	Modu³ zapisywania obrazów JPEG dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description saver-jpeg
JPEG Image saver module for Evas.

%description saver-jpeg -l pl
Modu³ zapisywania obrazów JPEG dla Evas.

%package saver-png
Summary:	PNG Image saver module for Evas
Summary(pl):	Modu³ zapisywania obrazów PNG dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description saver-png
PNG Image saver module for Evas.

%description saver-png -l pl
Modu³ zapisywania obrazów PNG dla Evas.

%package saver-tiff
Summary:	TIFF Image saver module for Evas
Summary(pl):	Modu³ zapisywania obrazów TIFF dla Evas
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description saver-tiff
TIFF Image saver module for Evas.

%description saver-tiff -l pl
Modu³ zapisywania obrazów TIFF dla Evas.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-software-x11 	\
	--disable-software-xcb	\
	--%{?with_directfb:en}%{!?with_directfb:dis}able-directfb	\
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
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/*

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

%files engine-buffer
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/buffer
%dir %{_libdir}/%{name}/modules/engines/buffer/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/buffer/linux-gnu-*/module.so

%files engine-directfb
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/directfb
%dir %{_libdir}/%{name}/modules/engines/directfb/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/directfb/linux-gnu-*/module.so

%files engine-fb
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/fb
%dir %{_libdir}/%{name}/modules/engines/fb/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/fb/linux-gnu-*/module.so

%files engine-gl_x11
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/gl_x11
%dir %{_libdir}/%{name}/modules/engines/gl_x11/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/gl_x11/linux-gnu-*/module.so

%files engine-software_generic
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_generic
%dir %{_libdir}/%{name}/modules/engines/software_generic/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_generic/linux-gnu-*/module.so

%if 0
%files engine-software_qtopia
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_qtopia
%dir %{_libdir}/%{name}/modules/engines/software_qtopia/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_qtopia/linux-gnu-*/module.so
%endif

%files engine-software_x11
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_x11
%dir %{_libdir}/%{name}/modules/engines/software_x11/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_x11/linux-gnu-*/module.so

%if 0
%files engine-software_xcb
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_xcb
%dir %{_libdir}/%{name}/modules/engines/software_xcb/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_xcb/linux-gnu-*/module.so
%endif

%files engine-xrender_x11
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/xrender_x11
%dir %{_libdir}/%{name}/modules/engines/xrender_x11/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/xrender_x11/linux-gnu-*/module.so

%files loader-edb
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/loaders/edb
%dir %{_libdir}/%{name}/modules/loaders/edb/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/edb/linux-gnu-*/module.so

%files loader-eet
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/loaders/eet
%dir %{_libdir}/%{name}/modules/loaders/eet/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/eet/linux-gnu-*/module.so

%files loader-gif
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/loaders/gif
%dir %{_libdir}/%{name}/modules/loaders/gif/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/gif/linux-gnu-*/module.so

%files loader-jpeg
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/loaders/jpeg
%dir %{_libdir}/%{name}/modules/loaders/jpeg/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/jpeg/linux-gnu-*/module.so

%files loader-png
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/loaders/png
%dir %{_libdir}/%{name}/modules/loaders/png/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/png/linux-gnu-*/module.so

%files loader-tiff
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/loaders/tiff
%dir %{_libdir}/%{name}/modules/loaders/tiff/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/tiff/linux-gnu-*/module.so

%files saver-edb
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/savers/edb
%dir %{_libdir}/%{name}/modules/savers/edb/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/savers/edb/linux-gnu-*/module.so

%files saver-eet
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/savers/eet
%dir %{_libdir}/%{name}/modules/savers/eet/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/savers/eet/linux-gnu-*/module.so

%files saver-jpeg
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/savers/jpeg
%dir %{_libdir}/%{name}/modules/savers/jpeg/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/savers/jpeg/linux-gnu-*/module.so

%files saver-png
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/savers/png
%dir %{_libdir}/%{name}/modules/savers/png/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/savers/png/linux-gnu-*/module.so

%files saver-tiff
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/savers/tiff
%dir %{_libdir}/%{name}/modules/savers/tiff/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/savers/tiff/linux-gnu-*/module.so
