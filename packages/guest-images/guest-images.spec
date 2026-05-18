Name: %{_cross_os}guest-images
Version: 0.1.0
Release: 1%{?dist}
Summary: Pre-built guest VM images for testing
License: Apache-2.0 OR MIT

Source100: bottlerocket-aws-nitro-guest-x86_64.eif
Source101: bottlerocket-aws-nitro-guest-x86_64-kernel
Source102: bottlerocket-aws-nitro-guest-x86_64-rootfs.erofs

%description
Pre-built guest VM images for launching in Nitro Enclaves or Firecracker.

%install
install -d %{buildroot}%{_cross_datadir}/guest-images
install -p -m 0644 %{S:100} %{buildroot}%{_cross_datadir}/guest-images/
install -p -m 0644 %{S:101} %{buildroot}%{_cross_datadir}/guest-images/
install -p -m 0644 %{S:102} %{buildroot}%{_cross_datadir}/guest-images/

%files
%license attribution.txt
%dir %{_cross_datadir}/guest-images
%{_cross_datadir}/guest-images/*
