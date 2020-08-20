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
Requires: wapt msktutil nginx-mod-http-auth-spnego
Requires: nethserver-postgresql
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
centralized management console for IT assets


%prep
%setup

%build
%{makedocs}
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
* Tue May 09 2017 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial
