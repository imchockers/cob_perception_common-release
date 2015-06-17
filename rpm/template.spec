Name:           ros-indigo-cob-perception-common
Version:        0.6.5
Release:        0%{?dist}
Summary:        ROS cob_perception_common package

Group:          Development/Libraries
License:        LGPL
URL:            http://wiki.ros.org/cob_perception_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-cob-cam3d-throttle
Requires:       ros-indigo-cob-image-flip
Requires:       ros-indigo-cob-object-detection-msgs
Requires:       ros-indigo-cob-object-detection-visualizer
Requires:       ros-indigo-cob-perception-msgs
Requires:       ros-indigo-cob-vision-utils
BuildRequires:  ros-indigo-catkin

%description
This stack provides utilities commonly needed for a variety of computer vision
tasks.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jun 17 2015 Richard Bormann <rmb@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

