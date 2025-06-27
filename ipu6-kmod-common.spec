%global date 20250627
%global commit 9bff73689ea2502f6e3bc34769fd699cde3ffeea
%global shortcommit %{sub %{commit} 1 7}

Name:           ipu6-kmod-common
Version:        0.1^%{date}git%{shortcommit}
Release:        5%{?dist}
Summary:        IPU6 common package
License:        GPLv2
URL:            https://github.com/jwrdegoede/ipu6-drivers
BuildArch:      noarch

Source0:        60-intel-ipu6.rules

# UDev rule location (_udevrulesdir)
BuildRequires:  systemd-rpm-macros

Requires:       ipu6-kmod = %{version}

%install
install -p -m 644 -D %{SOURCE0} %{buildroot}%{_udevrulesdir}/60-intel-ipu6.rules

%description
Common package for the IPU 6 kernel module and sensors. Currently empty to
satisfy akmod dependency.

%files
%{_udevrulesdir}/60-intel-ipu6.rules

%changelog
* Fri Jun 27 2025 Simone Caronni <negativo17@gmail.com> - 0.1^20250627git9bff736-5
- Add udev rule, align snapshot with kernel modules.

* Tue May 13 2025 Simone Caronni <negativo17@gmail.com> - 0.1^20250508git1a884d5-4
- Bump to 0.1.

* Sat Feb 15 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250215git40f5283-3
- Update to match driver snapshot.

* Fri Feb 07 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250205git032c59c-2
- Update to match driver snapshot.

* Tue Jan 21 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250119gitf2a1b54-1
- Initial packaging.
