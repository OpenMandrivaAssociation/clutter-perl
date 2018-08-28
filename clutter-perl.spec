%define module Clutter
%define oname Clutter

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
%setup -q -n %oname-%version

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
