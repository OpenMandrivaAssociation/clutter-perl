%define module Clutter
%define modulever 0.820

%define name clutter-perl
%define version 0.8.2.0
%define rel 1
%define svn 0
%if %svn
%define release %mkrel 0.%svn.%rel
%else
%define release %mkrel %rel
%endif

%define apiver 0.8
%define api 1.0

Summary:       Perl bindings for clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
%if %svn
Source0:       %{name}-%{svn}.tar.bz2
%else
Source0:       http://www.clutter-project.org/sources/clutter-perl/0.8/%{name}-%{version}.tar.bz2
%endif
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel >= 0.8.2
BuildRequires: clutter-cairo-devel >= 0.8.0
BuildRequires: clutter-gst-devel >= 0.8.0
BuildRequires: clutter-gtk-devel >= 0.8.0
BuildRequires: perl-devel
BuildRequires: perl-Gtk2 >= 1.140
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
%setup -q -n %{module}-%{modulever}
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
%{perl_vendorarch}/Gtk2/%{module}Texture.pod
%{perl_vendorarch}/Gtk2/%{module}Util.pod
%{_mandir}/*/*
