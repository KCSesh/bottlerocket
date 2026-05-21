Name: %{_cross_os}guest-images
Version: 0.1.0
Release: 1%{?dist}
Summary: Pre-built guest VM images for testing
License: Apache-2.0 OR MIT

Source100: bottlerocket-aws-nitro-guest-x86_64.eif
Source101: bottlerocket-aws-nitro-guest-x86_64-kernel
Source102: bottlerocket-aws-nitro-guest-x86_64-rootfs.erofs
Source103: test-upstream.eif
Source104: bottlerocket-aws-nitro-guest-x86_64-vmlinux
Source105: selinux-module.cil

%description
Pre-built guest VM images for launching in Nitro Enclaves or Firecracker.

%install
install -d %{buildroot}%{_cross_datadir}/guest-images
install -p -m 0644 %{S:100} %{buildroot}%{_cross_datadir}/guest-images/
install -p -m 0644 %{S:101} %{buildroot}%{_cross_datadir}/guest-images/
install -p -m 0644 %{S:102} %{buildroot}%{_cross_datadir}/guest-images/
install -p -m 0644 %{S:103} %{buildroot}%{_cross_datadir}/guest-images/
install -p -m 0644 %{S:104} %{buildroot}%{_cross_datadir}/guest-images/
install -d %{buildroot}%{_cross_datarootdir}/selinux/modules
install -p -m 0644 %{S:105} %{buildroot}%{_cross_datarootdir}/selinux/modules/selinux-module.cil

%files
%license attribution.txt
%dir %{_cross_datadir}/guest-images
%{_cross_datadir}/guest-images/*
%dir %{_cross_datarootdir}/selinux/modules
%{_cross_datarootdir}/selinux/modules/selinux-module.cil
