# TODO: use system liblinebreak?
#
# Conditional build:
%bcond_without	mmx		# MMX and MMX2 support (on x86)
%bcond_without	sse		# SSE support (on x86)
%bcond_without	altivec		# altivec support (on PPC)
%bcond_without	fb		# FB engine
%bcond_without	directfb	# DirectFB engine
%bcond_without	sdl		# SDL (OpenGL and software) engines
%bcond_with	svg		# Esvg-based SVG loader
%bcond_without	wayland		# wayland-egl, wayland-shm engines
%bcond_without	xcb		# XCB engines (software_8_x11, possibly software_x11/gl_x11)
%bcond_with	xcb_api		# software_x11/gl_x11 engines with XCB support (experimental)
%bcond_without	static_libs	# don't build static library
#
%ifnarch i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_mmx
%endif
%ifnarch i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_sse
%endif
%ifnarch ppc
%undefine	with_altivec
%endif
%if %{without xcb}
%undefine	xcb_api
%endif
%if %{with xcb_api}
%define		xapi	xcb
%else
%define		xapi	xlib
%endif
#
%define		edb_ver		1.0.5.043
%define		eet_ver 	1.7.0

Summary:	Multi-platform Canvas Library
Summary(pl.UTF-8):	Wieloplatformowa biblioteka do rysowania
Name:		evas
Version:	1.7.7
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	6f6bd375c37c3b01b9a4c622a77e72c6
Patch0:		%{name}-wayland.patch
Patch1:		%{name}-fribidi.patch
URL:		http://trac.enlightenment.org/e/wiki/Evas
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.16}
BuildRequires:	Mesa-libGLU-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.0}
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.6
BuildRequires:	edb-devel >= %{edb_ver}
BuildRequires:	eet-devel >= %{eet_ver}
BuildRequires:	eina-devel >= 1.6.0
%{?with_svg:BuildRequires:	esvg-devel >= 0.0.16}
BuildRequires:	fontconfig-devel >= 2.5.0
BuildRequires:	freetype-devel >= 1:2.2
BuildRequires:	fribidi-devel >= 0.19.2
BuildRequires:	giflib-devel
BuildRequires:	harfbuzz-devel >= 0.9.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libXext-devel
%if %{with xcb}
BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-image-devel >= 0.2.1
%endif
%if %{with wayland}
BuildRequires:	OpenGL-devel
BuildRequires:	Mesa-libEGL-devel >= 7.10
BuildRequires:	Mesa-libGLES-devel
BuildRequires:	Mesa-libwayland-egl-devel
BuildRequires:	wayland-devel
%endif
Requires:	eet >= %{eet_ver}
Requires:	eina >= 1.6.0
Requires:	freetype >= 1:2.2
Requires:	fribidi >= 0.19.2
Requires:	harfbuzz >= 0.9.0
Obsoletes:	evas-libs
Obsoletes:	evas-engine-software_qtopia
Obsoletes:	evas-engine-xrender_x11
Obsoletes:	evas-engine-xrender_xcb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%description -l pl.UTF-8
Evas to czyste API "płótna obrazu" dla różnych systemów wyświetlania,
będące w stanie rysować tekst z antyaliasingiem, wygładzane, skalowane
obrazy, obiekty z alpha-blendingiem i inne elementy.

%package devel
Summary:	Evas header files
Summary(pl.UTF-8):	Pliki nagłówkowe Evas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	eet-devel >= %{eet_ver}
Requires:	eina-devel >= 1.6.0
Requires:	fontconfig-devel >= 2.5.0
Requires:	freetype-devel >= 1:2.2
Requires:	fribidi-devel >= 0.19.2
Requires:	harfbuzz-devel >= 0.9.0
Provides:	%{name}-devel(%{xapi}) = %{version}-%{release}

%description devel
Header files for Evas.

%description devel -l pl.UTF-8
Pliki nagłówkowe Evas.

%package static
Summary:	Static Evas library
Summary(pl.UTF-8):	Statyczna biblioteka Evas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Evas library.

%description static -l pl.UTF-8
Statyczna biblioteka Evas.

##### MODULES #####
# engines:
%package engine-buffer
Summary:	Buffer rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego do bufora dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-buffer
Memory Buffer rendering engine module for Evas.

%description engine-buffer -l pl.UTF-8
Moduł silnika renderującego do bufora dla Evas.

%package engine-directfb
Summary:	DirectFB rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego na DirectFB dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB >= 0.9.16

%description engine-directfb
DirectFB rendering engine module for Evas.

%description engine-directfb -l pl.UTF-8
Moduł silnika renderującego na DirectFB dla Evas.

%package engine-fb
Summary:	Framebuffer rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego na framebuffer dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-fb
Framebuffer rendering engine module for Evas.

%description engine-fb -l pl.UTF-8
Moduł silnika renderującego na framebuffer dla Evas.

%package engine-gl_sdl
Summary:	SDL OpenGL rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego na SDL OpenGL dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}
Requires:	SDL >= 1.2.0

%description engine-gl_sdl
SDL OpenGL rendering engine module for Evas.

%description engine-gl_sdl -l pl.UTF-8
Moduł silnika renderującego na SDL OpenGL dla Evas.

%package engine-gl_x11
Summary:	OpenGL under X11 rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego na OpenGL pod X11 dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}
Provides:	%{name}-engine-gl_x11(%{xapi}) = %{version}-%{release}

%description engine-gl_x11
OpenGL under X11 rendering engine module for Evas.

%description engine-gl_x11 -l pl.UTF-8
Moduł silnika renderującego na OpenGL pod X11 dla Evas.

%package engine-software_8
Summary:	8-bit software rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika programowego renderującego 8-bitowego dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-software_8
8-bit software rendering engine module for Evas.

%description engine-software_8 -l pl.UTF-8
Moduł silnika programowego renderującego 8-bitowego dla Evas.

%package engine-software_8_x11
Summary:	8-bit X11 software rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika programowego renderującego 8-bitowego na X11 dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_8 = %{version}-%{release}

%description engine-software_8_x11
8-bit X11 (XCB) software rendering engine module for Evas.

%description engine-software_8_x11 -l pl.UTF-8
Moduł silnika programowego renderującego 8-bitowego na X11 (XCB) dla
Evas.

%package engine-software_16
Summary:	16-bit software rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika programowego renderującego 16-bitowego dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-software_16
16-bit software rendering engine module for Evas.

%description engine-software_16 -l pl.UTF-8
Moduł silnika programowego renderującego 16-bitowego dla Evas.

%package engine-software_16_sdl
Summary:	16-bit SDL software rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika programowego renderującego 16-bitowego na SDL dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_16 = %{version}-%{release}
Requires:	SDL >= 1.2.0
Obsoletes:	evas-engine-software_sdl

%description engine-software_16_sdl
16-bit SDL software rendering engine module for Evas.

%description engine-software_16_sdl -l pl.UTF-8
Moduł silnika programowego renderującego 16-bitowego na SDL dla Evas.

%package engine-software_16_x11
Summary:	16-bit X11 software rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika programowego renderującego 16-bitowego na X11 dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_16 = %{version}-%{release}

%description engine-software_16_x11
16-bit X11 (Xlib) software rendering engine module for Evas.

%description engine-software_16_x11 -l pl.UTF-8
Moduł silnika programowego renderującego 16-bitowego na X11 (Xlib) dla
Evas.

%package engine-software_generic
Summary:		Software rendering common engine module for Evas
Summary(pl.UTF-8):	Moduł wspólnego programowego silnika renderującego dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description engine-software_generic
Software rendering common engine module for Evas.

%description engine-software_generic -l pl.UTF-8
Moduł wspólnego programowego silnika renderującego dla Evas.

%package engine-software_x11
Summary:	Software X11 rendering engine module for Evas
Summary(pl.UTF-8):	Moduł programowego silnika renderującego X11 dla Evas
Group:		X11/Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}
Obsoletes:	evas-engine-software_xcb

%description engine-software_x11
Software X11 rendering engine module for Evas.

%description engine-software_x11 -l pl.UTF-8
Moduł programowego silnika renderującego X11 dla Evas.

%package engine-wayland_egl
Summary:	Wayland EGL rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego Wayland EGL dla Evas
Group:		Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-wayland_egl
Wayland EGL rendering engine module for Evas.

%description engine-wayland_egl -l pl.UTF-8
Moduł silnika renderującego Wayland EGL dla Evas.

%package engine-wayland_shm
Summary:	Wayland SHM rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego Wayland SHM dla Evas
Group:		Libraries
Requires:	%{name}-engine-software_generic = %{version}-%{release}

%description engine-wayland_shm
Wayland SHM rendering engine module for Evas.

%description engine-wayland_shm -l pl.UTF-8
Moduł silnika renderującego Wayland SHM dla Evas.

# loaders:
%package loader-edb
Summary:	EDB Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów EDB dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-edb
EDB Image loader module for Evas.

%description loader-edb -l pl.UTF-8
Moduł wczytywania obrazów EDB dla Evas.

%package loader-eet
Summary:	EET Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów EET dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-eet
EET Image loader module for Evas.

%description loader-eet -l pl.UTF-8
Moduł wczytywania obrazów EET dla Evas.

%package loader-gif
Summary:	GIF Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów GIF dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-gif
GIF Image loader module for Evas.

%description loader-gif -l pl.UTF-8
Moduł wczytywania obrazów GIF dla Evas.

%package loader-jpeg
Summary:	JPEG Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów JPEG dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-jpeg
JPEG Image loader module for Evas.

%description loader-jpeg -l pl.UTF-8
Moduł wczytywania obrazów JPEG dla Evas.

%package loader-pmaps
Summary:	PMAPS Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów PMAPS dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-pmaps
PMAPS Image loader module for Evas.

%description loader-pmaps -l pl.UTF-8
Moduł wczytywania obrazów PMAPS dla Evas.

%package loader-png
Summary:	PNG Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów PNG dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-png
PNG Image loader module for Evas.

%description loader-png -l pl.UTF-8
Moduł wczytywania obrazów PNG dla Evas.

%package loader-svg
Summary:	SVG Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów SVG dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	esvg >= 0.0.16

%description loader-svg
SVG Image loader module for Evas.

%description loader-svg -l pl.UTF-8
Moduł wczytywania obrazów SVG dla Evas.

%package loader-tiff
Summary:	TIFF Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów TIFF dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-tiff
TIFF Image loader module for Evas.

%description loader-tiff -l pl.UTF-8
Moduł wczytywania obrazów TIFF dla Evas.

%package loader-xpm
Summary:	XPM Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów XPM dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description loader-xpm
XPM Image loader module for Evas.

%description loader-xpm -l pl.UTF-8
Moduł wczytywania obrazów XPM dla Evas.

# savers:
%package saver-edb
Summary:	EDB Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów EDB dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description saver-edb
EDB Image saver module for Evas.

%description saver-edb -l pl.UTF-8
Moduł zapisywania obrazów EDB dla Evas.

%package saver-eet
Summary:	EET Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów EET dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description saver-eet
EET Image saver module for Evas.

%description saver-eet -l pl.UTF-8
Moduł zapisywania obrazów EET dla Evas.

%package saver-jpeg
Summary:	JPEG Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów JPEG dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description saver-jpeg
JPEG Image saver module for Evas.

%description saver-jpeg -l pl.UTF-8
Moduł zapisywania obrazów JPEG dla Evas.

%package saver-png
Summary:	PNG Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów PNG dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description saver-png
PNG Image saver module for Evas.

%description saver-png -l pl.UTF-8
Moduł zapisywania obrazów PNG dla Evas.

%package saver-tiff
Summary:	TIFF Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów TIFF dla Evas
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description saver-tiff
TIFF Image saver module for Evas.

%description saver-tiff -l pl.UTF-8
Moduł zapisywania obrazów TIFF dla Evas.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	%{!?with_static_libs:--disable-static} \
	--enable-buffer \
	--enable-cpu-altivec%{!?with_altivec:=no} \
	--enable-cpu-c \
	--enable-cpu-mmx%{!?with_mmx:=no} \
	--enable-cpu-sse%{!?with_sse:=no} \
	--enable-directfb%{!?with_directfb:=no} \
	--enable-fb%{!?with_fb:=no} \
	--enable-font-loader-eet	\
	--enable-gl-sdl%{!?with_sdl:=no} \
	--enable-gl-xcb%{!?with_xcb_api:=no} \
	--enable-gl-xlib \
	--enable-image-loader-edb	\
	--enable-image-loader-eet	\
	--enable-image-loader-gif	\
	--enable-image-loader-jpeg	\
	--enable-image-loader-png	\
	--enable-image-loader-svg%{!?with_svg:=no} \
	--enable-image-loader-tiff	\
	--enable-image-loader-xpm	\
	--enable-pixman			\
	--enable-software-8-x11%{!?with_xcb:=no} \
	--enable-software-16-sdl%{!?with_sdl:=no} \
	--enable-software-16-x11 \
	--enable-software-xcb%{!?with_xcb_api:=no} \
	--enable-software-xlib \
	--enable-wayland-egl%{!?with_wayland:=no} \
	--enable-wayland-shm%{!?with_wayland:=no} \
	--disable-valgrind

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/cserve2/*/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/engines/software_16_sdl/linux-gnu-*/module.a

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/evas/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/evas_cserve2_client
%attr(755,root,root) %{_bindir}/evas_cserve2_debug
%attr(755,root,root) %{_bindir}/evas_cserve2_usage
%attr(755,root,root) %{_libdir}/libevas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevas.so.1
%attr(755,root,root) %{_libexecdir}/dummy_slave
%attr(755,root,root) %{_libexecdir}/evas_cserve2
%attr(755,root,root) %{_libexecdir}/evas_cserve2_slave
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/cserve2
%dir %{_libdir}/%{name}/cserve2/loaders
# loaders without additional dependencies
%dir %{_libdir}/%{name}/cserve2/loaders/bmp
%dir %{_libdir}/%{name}/cserve2/loaders/bmp/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/bmp/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/cserve2/loaders/ico
%dir %{_libdir}/%{name}/cserve2/loaders/ico/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/ico/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/cserve2/loaders/psd
%dir %{_libdir}/%{name}/cserve2/loaders/psd/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/psd/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/cserve2/loaders/tga
%dir %{_libdir}/%{name}/cserve2/loaders/tga/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/tga/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/cserve2/loaders/wbmp
%dir %{_libdir}/%{name}/cserve2/loaders/wbmp/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/wbmp/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/engines
%dir %{_libdir}/%{name}/modules/loaders
%dir %{_libdir}/%{name}/modules/savers
# loaders without additional dependencies
%dir %{_libdir}/%{name}/modules/loaders/bmp
%dir %{_libdir}/%{name}/modules/loaders/bmp/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/bmp/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/generic
%dir %{_libdir}/%{name}/modules/loaders/generic/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/generic/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/ico
%dir %{_libdir}/%{name}/modules/loaders/ico/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/ico/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/psd
%dir %{_libdir}/%{name}/modules/loaders/psd/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/psd/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/tga
%dir %{_libdir}/%{name}/modules/loaders/tga/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/tga/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/wbmp
%dir %{_libdir}/%{name}/modules/loaders/wbmp/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/wbmp/linux-gnu-*/module.so
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevas.so
%{_libdir}/libevas.la
%{_includedir}/evas-1
%{_pkgconfigdir}/evas.pc
# engine private structures
%{?with_directfb:%{_pkgconfigdir}/evas-directfb.pc}
%{_pkgconfigdir}/evas-fb.pc
%{?with_sdl:%{_pkgconfigdir}/evas-opengl-sdl.pc}
%{_pkgconfigdir}/evas-opengl-x11.pc
%{?with_xcb:%{_pkgconfigdir}/evas-software-8-x11.pc}
%{_pkgconfigdir}/evas-software-16-x11.pc
%{_pkgconfigdir}/evas-software-buffer.pc
%{?with_sdl:%{_pkgconfigdir}/evas-software-sdl.pc}
%{_pkgconfigdir}/evas-software-x11.pc
%if %{with wayland}
%{_pkgconfigdir}/evas-wayland-egl.pc
%{_pkgconfigdir}/evas-wayland-shm.pc
%endif
%{_examplesdir}/%{name}-%{version}

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

%if %{with directfb}
%files engine-directfb
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/directfb
%dir %{_libdir}/%{name}/modules/engines/directfb/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/directfb/linux-gnu-*/module.so
%endif

%if %{with fb}
%files engine-fb
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/fb
%dir %{_libdir}/%{name}/modules/engines/fb/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/fb/linux-gnu-*/module.so
%endif

%if %{with sdl}
%files engine-gl_sdl
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/gl_sdl
%dir %{_libdir}/%{name}/modules/engines/gl_sdl/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/gl_sdl/linux-gnu-*/module.so
%endif

%files engine-gl_x11
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/gl_x11
%dir %{_libdir}/%{name}/modules/engines/gl_x11/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/gl_x11/linux-gnu-*/module.so

%if %{with xcb}
%files engine-software_8
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_8
%dir %{_libdir}/%{name}/modules/engines/software_8/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_8/linux-gnu-*/module.so

%files engine-software_8_x11
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_8_x11
%dir %{_libdir}/%{name}/modules/engines/software_8_x11/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_8_x11/linux-gnu-*/module.so
%endif

%files engine-software_16
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_16
%dir %{_libdir}/%{name}/modules/engines/software_16/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_16/linux-gnu-*/module.so

%files engine-software_16_x11
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_16_x11
%dir %{_libdir}/%{name}/modules/engines/software_16_x11/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_16_x11/linux-gnu-*/module.so

%if %{with sdl}
%files engine-software_16_sdl
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_16_sdl
%dir %{_libdir}/%{name}/modules/engines/software_16_sdl/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_16_sdl/linux-gnu-*/module.so
%endif

%files engine-software_generic
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_generic
%dir %{_libdir}/%{name}/modules/engines/software_generic/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_generic/linux-gnu-*/module.so

%files engine-software_x11
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/software_x11
%dir %{_libdir}/%{name}/modules/engines/software_x11/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/software_x11/linux-gnu-*/module.so

%if %{with wayland}
%files engine-wayland_egl
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/wayland_egl
%dir %{_libdir}/%{name}/modules/engines/wayland_egl/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/wayland_egl/linux-gnu-*/module.so

%files engine-wayland_shm
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/engines/wayland_shm
%dir %{_libdir}/%{name}/modules/engines/wayland_shm/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/engines/wayland_shm/linux-gnu-*/module.so
%endif

%files loader-edb
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/loaders/edb
%dir %{_libdir}/%{name}/modules/loaders/edb/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/edb/linux-gnu-*/module.so

%files loader-eet
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/cserve2/loaders/eet
%dir %{_libdir}/%{name}/cserve2/loaders/eet/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/eet/linux-gnu-*/module.so
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
%dir %{_libdir}/%{name}/cserve2/loaders/jpeg
%dir %{_libdir}/%{name}/cserve2/loaders/jpeg/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/jpeg/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/jpeg
%dir %{_libdir}/%{name}/modules/loaders/jpeg/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/jpeg/linux-gnu-*/module.so

%files loader-pmaps
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/cserve2/loaders/pmaps
%dir %{_libdir}/%{name}/cserve2/loaders/pmaps/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/pmaps/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/pmaps
%dir %{_libdir}/%{name}/modules/loaders/pmaps/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/pmaps/linux-gnu-*/module.so

%files loader-png
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/cserve2/loaders/png
%dir %{_libdir}/%{name}/cserve2/loaders/png/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/png/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/png
%dir %{_libdir}/%{name}/modules/loaders/png/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/png/linux-gnu-*/module.so

%if %{with svg}
%files loader-svg
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/modules/loaders/svg
%dir %{_libdir}/%{name}/modules/loaders/svg/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/svg/linux-gnu-*/module.so
%endif

%files loader-tiff
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/cserve2/loaders/tiff
%dir %{_libdir}/%{name}/cserve2/loaders/tiff/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/tiff/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/tiff
%dir %{_libdir}/%{name}/modules/loaders/tiff/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/tiff/linux-gnu-*/module.so

%files loader-xpm
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/cserve2/loaders/xpm
%dir %{_libdir}/%{name}/cserve2/loaders/xpm/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/cserve2/loaders/xpm/linux-gnu-*/module.so
%dir %{_libdir}/%{name}/modules/loaders/xpm
%dir %{_libdir}/%{name}/modules/loaders/xpm/linux-gnu-*
%attr(755,root,root) %{_libdir}/%{name}/modules/loaders/xpm/linux-gnu-*/module.so

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
