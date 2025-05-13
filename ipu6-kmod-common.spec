%global date 20250508
%global commit 1a884d5124dc149af4a645aa1493873bf796d677
%global shortcommit %{sub %{commit} 1 7}

Name:           ipu6-kmod-common
Version:        0.1^%{date}git%{shortcommit}
Release:        4%{?dist}
Summary:        IPU6 common package
License:        GPLv2
URL:            https://github.com/jwrdegoede/ipu6-drivers
BuildArch:      noarch

Requires:       ipu6-kmod = %{version}

%description
Common package for the IPU 6 kernel module and sensors. Currently empty to
satisfy akmod dependency.

%files

%changelog
* Tue May 13 2025 Simone Caronni <negativo17@gmail.com> - 0.1^20250508git1a884d5-4
- Bump to 0.1.

* Sat Feb 15 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250215git40f5283-3
- Update to match driver snapshot.

* Fri Feb 07 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250205git032c59c-2
- Update to match driver snapshot.

* Tue Jan 21 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250119gitf2a1b54-1
- Initial packaging.
