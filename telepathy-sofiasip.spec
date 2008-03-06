Name:           telepathy-sofiasip
Version:        0.5.5
Release:        %mkrel 1
Summary:        A SIP protocol implementation for the Telepathy stack

Group:          Networking/Instant messaging
License:        LGPL
URL:            http://%{name}.sf.net
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  telepathy-glib
BuildRequires:  pkgconfig(sofia-sip-ua-glib)
Requires:       telepathy-filesystem

%description
telepathy-sofiasip is a SIP-protocol connection manager (protocol plugin) 
for the Telepathy (http://telepathy.freedesktop.org) framework based on 
SofiaSIP-stack.

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_libdir}/%{name}
%{_mandir}/man*/*.lzma

%prep
%setup -q -n telepathy-sofiasip-0.5.5.0

%build
%configure 
%make

%install
rm -rf %buildroot
make install DESTDIR=%buildroot

%clean
rm -rf %buildroot
