Summary:	Multi-platform Canvas Library
Name:		evas
Version:	1.0.0
#%define _pre	pre13
%define _snap	20050106
Release:	0.%{_snap}.0.1
License:	BSD
Group:		Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}_%{_pre}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	90bf34e3e6aaedaaa20856b2b5bbf6ad
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	DirectFB-devel
BuildRequires:	X11-OpenGL-devel
#BuildRequires:	cairo-devel
BuildRequires:	edb-devel
BuildRequires:	eet-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%package devel
Summary:	Evas headers, documentation and test programs
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	DirectFB-devel
Requires:	X11-OpenGL-devel
#Requires:	cairo-devel
Requires:	edb-devel
Requires:	eet-devel
Requires:	freetype-devel
Requires:	libjpeg-devel
Requires:	libpng-devel

%description devel
Headers, static libraries, test programs and documentation for Evas.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for Evas.

%prep
#%%setup -q -n %{name}-%{version}_%{_pre}
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-cairo-x11
#/usr/lib/libcairo.so: undefined reference to `pixman_image_get_format'
#/usr/lib/libcairo.so: undefined reference to `pixman_format_get_masks'
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
%attr(755,root,root) %{_libdir}/libevas.so.*
%attr(755,root,root) %{_bindir}/evas_*
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
