Name:           telepathy-sofiasip
Version:        0.5.4
Release:        %mkrel 1
Summary:        XXX

Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://%{name}.sf.net
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  telepathy-glib
BuildRequires:  pkgconfig(sofia-sip-ua-glib)
Requires:       telepathy-filesystem

%description

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_libdir}/%{name}
%{_mandir}/man*/*.lzma

#--------------------------------------------------------------------

%prep
%setup -q


%build
%configure 
%make


%install
rm -rf %buildroot
make install DESTDIR=%buildroot


%clean
rm -rf %buildroot
