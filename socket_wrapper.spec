Name:           socket_wrapper
Version:        1.3.3
Release:        1
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
%ifarch riscv64
ctest -V --timeout 240
%else
ctest -V
%endif
LD_PRELOAD=src/libsocket_wrapper.so bash -c '>/dev/null'

%files
%doc AUTHORS LICENSE
%{_libdir}/libsocket_wrapper.so*
%{_libdir}/libsocket_wrapper_noop.so*
%dir %{_libdir}/cmake/socket_wrapper
%{_libdir}/cmake/socket_wrapper/socket_wrapper-config*.cmake
%{_libdir}/cmake/socket_wrapper/socket_wrapper_noop-config*.cmake
%{_libdir}/pkgconfig/socket_wrapper.pc
%{_libdir}/pkgconfig/socket_wrapper_noop.pc
%{_includedir}/socket_wrapper.h

%files help
%{_mandir}/man1/socket_wrapper.1*

%changelog
* Wed Mar 30 2022 YukariChiba <i@0x7f.cc> - 1.3.3-1
- Upgrade version to 1.3.3

* Thu Feb 24 2022 YukariChiba <i@0x7f.cc> - 1.1.9-5
- Add more timeout for riscv64

* Wed Nov 27 2019 zhouyihang <zhouyihang1@huawei.com> - 1.1.9-4
- Package init
