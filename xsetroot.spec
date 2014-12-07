Name:		xsetroot
Version:	1.1.1
Release:	9
Summary:	Root window parameter setting utility for X
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: x11-data-bitmaps >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(xcursor)

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
%makeinstall_std

%files
%{_bindir}/xsetroot
%{_mandir}/man1/xsetroot.1*



%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2011.0
+ Revision: 671366
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 592560
- BR libxcursor-devel instead of x11-data-cursor-themes
- BR x11-data-cursor-themes
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 464750
- New version: 1.0.3

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-4mdv2009.1
+ Revision: 350772
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 226080
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 154300
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 76608
- rebuild for 2008
- minor spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - revert
    - new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - new upstream release: 1.0.3


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:15:56 (31710)
- fill in a few more missing descriptions

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

