Name:           telepathy-sofiasip
Version:        0.6.0
Release:        %mkrel 1
Summary:        A SIP protocol implementation for the Telepathy stack

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://%{name}.sf.net
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  libtelepathy-glib-devel
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
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_libdir}/%{name}
%{_mandir}/man*/*.lzma
%{_includedir}/telepathy-sofiasip-0.6/tpsip/*.h


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot
