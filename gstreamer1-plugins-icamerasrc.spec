%global commit 1baecb1a466ad610042e437d963cb38a4cfcf592
%global commitdate 20240606
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# The gstreamer provides generator causes libhal_adaptor.so init/constructor
# function to run which fails on systems without an IPU6, do not run it on
# the gstreamer plugin
%global __provides_exclude_from ^(%{_libdir}/gstreamer-1\\.0/libgsticamerasrc\\.so)$

Name:           gstreamer1-plugins-icamerasrc
Summary:        GStreamer 1.0 Intel IPU6 camera plug-in
Version:        0.0
Release:        11.%{commitdate}git%{shortcommit}%{?dist}
License:        LGPLv2
URL:            https://github.com/intel/icamerasrc/tree/icamerasrc_slim_api

Source0:        https://github.com/intel/icamerasrc/archive/%{commit}/icamerasrc-%{shortcommit}.tar.gz

BuildRequires:  ipu6-camera-bins-devel
BuildRequires:  ipu6-camera-hal-devel >= 0.0-18
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  libdrm-devel
BuildRequires:  libva-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  pkgconfig(gstreamer-va-1.0)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

ExclusiveArch:  x86_64

%description
This package provides the GStreamer 1.0 plug-in for MIPI camera.

%package devel
Summary:        GStreamer plug-in development files for Intel IPU6 camera
Requires:       gstreamer1-devel
Requires:       ipu6-camera-bins-devel
Requires:       ipu6-camera-hal-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This provides the necessary header files for IPU6 GStreamer plugin development.

%prep
%autosetup -p1 -n icamerasrc-%{commit}
autoreconf --verbose --force --install --make

%build
export CHROME_SLIM_CAMHAL=ON
export STRIP_VIRTUAL_CHANNEL_CAMHAL=ON
%configure --with-haladaptor
%make_build

%install
%make_install

%files
%license LICENSE
%{_libdir}/gstreamer-1.0/*
%{_libdir}/libgsticamerainterface-1.0.so.1
%{_libdir}/libgsticamerainterface-1.0.so.1.0.0

%files devel
%{_libdir}/libgsticamerainterface-1.0.so
%{_includedir}/gstreamer-1.0/gst/*
%{_libdir}/pkgconfig/*

%changelog
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0-11.20240606git1baecb1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Hans de Goede <hdegoede@redhat.com> - 0.0-10.20240606git1baecb1
- Update to commit 1baecb1a466ad610042e437d963cb38a4cfcf592
- Switch to using hal-adaptor to dispatch between different libcamhal builds

* Fri Mar 15 2024 Kate Hsuan <hpa@redhat.com> - 0.0-9.20231023git528a6f1
- Update to the latest upstream commit

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0-8.20220926git3b7cdb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.0-7.20220926git3b7cdb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 17 2023 Kate Hsuan <hpa@redhat.com> - 0.0-5.20220926git3b7cdb9
- A few minor revisions includes
- Removed unnecessary %%dir
- Removed .so file from devel package

* Wed Feb 15 2023 Kate Hsuan <hpa@redhat.com> - 0.0-4.20220926git3b7cdb9
- Updated the build and installation scripts

* Tue Dec 20 2022 Kate Hsuan <hpa@redhat.com> - 0.0-3.20220926git3b7cdb9
- Modify library path for build

* Tue Dec 20 2022 Kate Hsuan <hpa@redhat.com> - 0.0-2.20220926git3b7cdb9
- File placement fixes
- Format for style fixes

* Tue Nov 29 2022 Kate Hsuan <hpa@redhat.com> - 0.0-1.20220926git3b7cdb9
- First commit
