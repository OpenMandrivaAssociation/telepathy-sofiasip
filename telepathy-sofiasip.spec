Name:           telepathy-sofiasip
Version:        0.7.1
Release:        2
Summary:        A SIP protocol implementation for the Telepathy stack

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            https://%{name}.sf.net
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  libxslt-proc
BuildRequires:  pkgconfig(sofia-sip-ua-glib)
BuildRequires:  python
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       telepathy-filesystem

%description
telepathy-sofiasip is a SIP-protocol connection manager (protocol plugin)
for the Telepathy (http://telepathy.freedesktop.org) framework based on
SofiaSIP-stack.

%files
%doc COPYING AUTHORS
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_libdir}/%{name}
%{_mandir}/man*/*
%{_includedir}/telepathy-sofiasip-0.6/tpsip/*.h


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std