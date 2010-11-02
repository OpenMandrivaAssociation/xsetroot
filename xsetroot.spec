Name:		xsetroot
Version:	1.1.0
Release:	%mkrel 1
Summary:	Root window parameter setting utility for X
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-data-bitmaps >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libxcursor-devel

%description
The setroot program allows to tailor the appearance of the background
("root") window on a workstation display running X.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xsetroot
%{_mandir}/man1/xsetroot.1*

