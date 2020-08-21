Summary: nethserver-wapt  is an helpdesk for IT assets
%define name nethserver-wapt
Name: %{name}
%define version 0.0.1
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
#BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: wapt >= 1.8.0, wapt < 1.9.0
Requires: msktutil nginx-mod-http-auth-spnego
Requires: nethserver-postgresql
BuildRequires: nethserver-devtools
BuildArch: noarch
Conflicts: nethserver-nginx

%description
centralized management console for IT assets


%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post

%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Fri Aug 21 2020 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial
