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
Requires: tis-waptserver >= 1.8.0, tis-waptserver < 1.9.0
Requires: tis-waptsetup >= 1.8.0, tis-waptsetup < 1.9.0
Requires: postgresql96-server postgresql96-contrib
Requires: cabextract
Requires: msktutil
Requires: nginx-mod-http-auth-spnego
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
