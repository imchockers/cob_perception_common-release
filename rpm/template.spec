Name:           ros-kinetic-cob-vision-utils
Version:        0.6.9
Release:        0%{?dist}
Summary:        ROS cob_vision_utils package

Group:          Development/Libraries
License:        LGPL
URL:            http://wiki.ros.org/cob_vision_utils
Source0:        %{name}-%{version}.tar.gz

Requires:       opencv-devel
Requires:       ros-kinetic-cmake-modules
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-visualization-msgs
Requires:       tinyxml-devel
BuildRequires:  opencv-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  tinyxml-devel

%description
Contains utilities used within the object detection tool chain.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jul 18 2017 Richard Bormann <rmb@ipa.fhg.de> - 0.6.9-0
- Autogenerated by Bloom

