%define module Clutter

%define apiver 1.0
%define api 1.0

Summary:       Perl bindings for clutter
Name:          clutter-perl
Version:       1.0.1
Release:       4
Source0:       http://www.clutter-project.org/sources/clutter-perl/%api/%{name}-%{version}.tar.bz2
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel >= 1.0
BuildRequires: perl-devel
BuildRequires: perl-Gtk2 >= 1.140
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
