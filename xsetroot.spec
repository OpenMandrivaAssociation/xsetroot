Name:		xsetroot
Version:	1.1.2
Release:	2
Summary:	Root window parameter setting utility for X
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: x11-data-bitmaps >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xbitmaps)

%description
The setroot program allows to tailor the appearance of the background
("root") window on a workstation display running X.

%prep
%autosetup -p1

%build
%configure	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xsetroot
%{_mandir}/man1/xsetroot.1*
