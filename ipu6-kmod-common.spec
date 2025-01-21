%global commit0 f2a1b54afd8537f52f17adcadd7d3e064cf704a3
%global date 20250119
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           ipu6-kmod-common
Version:        0.0^%{date}git%{shortcommit0}
Release:        1%{?dist}
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
* Tue Jan 21 2025 Simone Caronni <negativo17@gmail.com> - 0.0^20250119gitf2a1b54-1
- Initial packaging.
