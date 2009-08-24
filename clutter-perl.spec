%define module Clutter

%define name clutter-perl
%define version 1.0.0
%define rel 1
%define svn 0
%if %svn
%define release %mkrel 0.%svn.%rel
%else
%define release %mkrel %rel
%endif

%define apiver 1.0
%define api 1.0

Summary:       Perl bindings for clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
%if %svn
Source0:       %{name}-%{svn}.tar.bz2
%else
Source0:       http://www.clutter-project.org/sources/clutter-perl/%api/%{name}-%{version}.tar.bz2
%endif
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
%if %svn
%setup -q -n %name
./autogen.sh -V
%else
%setup -q -n %name-%version
%endif

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
