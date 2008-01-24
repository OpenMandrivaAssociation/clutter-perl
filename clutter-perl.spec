%define module Clutter

%define name clutter-perl
%define version 0.4.1.0
%define rel 2
%define svn 0
%if %svn
%define release %mkrel 0.%svn.%rel
%else
%define release %mkrel %rel
%endif

%define api 1.0

Summary:       Perl bindings for clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
%if %svn
Source0:       %{name}-%{svn}.tar.bz2
%else
Source0:       %{name}-%{version}.tar.bz2
%endif
License:       LGPL
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel
BuildRequires: clutter-cairo-devel
BuildRequires: clutter-gst-devel
BuildRequires: clutter-gtk-devel
BuildRequires: perl-devel
BuildRequires: perl-Gtk2
BuildRequires: perl-GStreamer
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig


%description
Perl bindings for clutter

#----------------------------------------------------------------------------

%package -n perl-%{module}
Summary:       Perl bindings for clutter
Group:         Graphics
Provides:      pyclutter = %{version}-%{release}

%description -n perl-%{module}
Perl bindings for clutter

#----------------------------------------------------------------------------

%prep
%if %svn
%setup -q -n %name
./autogen.sh -V
%else
%setup -q -n %{module}-0.410
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
%{perl_vendorarch}/Gtk2/%{module}Embed.pod
%{_mandir}/*/*
