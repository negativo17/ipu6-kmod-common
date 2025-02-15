%global commit0 40f52831a1bd234961b989d921113bb7603233b2
%global date 20250215
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           ipu6-kmod-common
Version:        0.0^%{date}git%{shortcommit0}
Release:        3%{?dist}
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
* Sat Feb 15 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250215git40f5283-3
- Update to match driver snapshot.

* Fri Feb 07 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250205git032c59c-2
- Update to match driver snapshot.

* Tue Jan 21 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250119gitf2a1b54-1
- Initial packaging.
