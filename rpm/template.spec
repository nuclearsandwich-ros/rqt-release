%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rqt
Version:        1.1.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt package

License:        BSD
URL:            http://ros.org/wiki/rqt
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-rqt-gui >= 0.3.0
Requires:       ros-rolling-rqt-gui-cpp >= 0.3.0
Requires:       ros-rolling-rqt-gui-py >= 0.3.0
Requires:       ros-rolling-rqt-py-common
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt is a Qt-based framework for GUI development for ROS. It consists of three
parts/metapackages rqt (you're here) rqt_common_plugins - ROS backend tools
suite that can be used on/off of robot runtime. rqt_robot_plugins - Tools for
interacting with robots during their runtime. rqt metapackage provides a widget
rqt_gui that enables multiple `rqt` widgets to be docked in a single window.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Aug 31 2021 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.1.2-1
- Autogenerated by Bloom

* Mon Apr 12 2021 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.1.1-1
- Autogenerated by Bloom

* Wed Apr 07 2021 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.1.0-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 1.0.7-1
- Autogenerated by Bloom

