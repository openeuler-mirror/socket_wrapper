Name:           socket_wrapper
Version:        1.1.9
Release:        4
Summary:        A library passing all socket communications through unix sockets.
License:        BSD
URL:            http://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz

BuildRequires:  cmake gcc libcmocka-devel >= 1.1.0

Recommends:     cmake pkgconfig

%description
socket_wrapper aims to help client/server software development teams
willing to gain full functional test coverage. It makes possible to
run several instances of the full software stack on the same machine
and perform locally functional testing of complex network configurations.
It provides featrues as follow:
1)Redirects all network communication to happen over unix sockets.
2)Support for IPv4 and IPv6 socket and addressing emulation.
3)Ablility to capture network traffic in pcap format.

%package        help
Summary:        Documents for socket_wrapper
Buildarch:      noarch

%description    help
Man pages and other related documents.

%prep
%autosetup -n %{name}-%{version} -p1

%build
mkdir build
cd build
%cmake -DUNIT_TESTING=ON %{_builddir}/%{name}-%{version}
%make_build VERBOSE=1

%install
cd build
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
cd build
ctest -V
LD_PRELOAD=src/libsocket_wrapper.so bash -c '>/dev/null'

%files
%doc AUTHORS COPYING
%{_libdir}/libsocket_wrapper.so*
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config*.cmake
%{_libdir}/pkgconfig/socket_wrapper.pc

%files help
%doc ChangeLog README
%{_mandir}/man1/socket_wrapper.1*

%changelog
* Wed Nov 27 2019 zhouyihang <zhouyihang1@huawei.com> - 1.1.9-4
- Package init
