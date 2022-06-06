%define debug_package %{nil}

%define mybuildnumber %{?build_number}%{?!build_number:1}

Name:           flirc-util
Version:        0.20191027
Release:        %{mybuildnumber}%{?dist}
Summary:        FLIRC command-line utility
Group:          Applications/Audio

License:        Proprietary
URL:            https://github.com/flirc/sdk
Source0:        flirc-sdk-%{version}.tar.gz

BuildRequires:  libusb-devel
BuildRequires:  readline-devel
BuildRequires:  hidapi-devel
BuildRequires:  binutils
BuildRequires:  make
BuildRequires:  gcc

%description
Small command-line program to poke at ALSA bits.

%prep
%setup -q

%build
cd cli
make flirc_util CONFIG=debug

%install
mkdir -p "$RPM_BUILD_ROOT/%{_bindir}"
cp -f cli/buildresults/Linux_x86_64/gcc/flirc_util/debug/flirc_util "$RPM_BUILD_ROOT/%{_bindir}/flirc_util"
chmod 755 "$RPM_BUILD_ROOT/%{_bindir}/flirc_util"

%files
%defattr(-, root, root)
%attr(0755, root, root) %_bindir/flirc_util

%changelog
* Fri Mar 15 2019  Manuel Amador (Rudd-O) <rudd-o@rudd-o.com>
- Port to generic pipeline build.
