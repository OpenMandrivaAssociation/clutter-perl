%define module Clutter

%define apiver 1.0
%define api 1.0

Summary:       Perl bindings for clutter
Name:          clutter-perl
Version:       1.110
Release:       1
Source0:       https://cpan.metacpan.org/authors/id/E/EB/EBASSI/Clutter-%{version}.tar.gz
License:       LGPLv2+
Group:         Graphics
Url:           https://metacpan.org/pod/Clutter
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel >= 1.0
BuildRequires: perl-devel
#BuildRequires: perl-Gtk2 >= 1.140
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig


%description
Perl bindings for clutter

#----------------------------------------------------------------------------

%package -n perl-%{module}
Summary:       Perl bindings for clutter
Group:         Graphics
Provides:      clutter-perl = %{version}-%{release}

%description -n perl-%{module}
Perl bindings for clutter

#----------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %buildroot

%makeinstall_std

%clean
rm -rf %buildroot

%files -n perl-%{module}
%defattr(-,root,root)
%{perl_vendorarch}/%module
%{perl_vendorarch}/%module.pm
%{perl_vendorarch}/auto/*
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.1-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 1.0.1-3mdv2011.0
+ Revision: 556960
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild

* Fri Sep 04 2009 Götz Waschk <waschk@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 431069
- update to new version 1.0.1

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 420324
- new version
- update deps
- update file list

* Thu Feb 12 2009 Funda Wang <fwang@mandriva.org> 0.8.2.0-1mdv2009.1
+ Revision: 339770
- New version 0.8.2.0

* Sat Sep 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.8.0.1-1mdv2009.0
+ Revision: 284377
- New version: 0.8.0.1

* Wed Feb 20 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.0.0-1mdv2008.1
+ Revision: 173179
- New version

* Thu Jan 24 2008 Colin Guthrie <cguthrie@mandriva.org> 0.4.1.0-2mdv2008.1
+ Revision: 157488
- Bump release for buildsystem lock.
- New upstream version 0.4..01

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 09 2007 Colin Guthrie <cguthrie@mandriva.org> 0.4.1-1mdv2008.0
+ Revision: 60732
- Add BuildRequires for perl-devel
- Add perl-Gtk2 build deps
- Import clutter-perl

