%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


%global package_name python-masakariclient
%global srcname masakariclient

%define debug_package %{nil}

Name:       %{package_name}
Version:    2.0.0
Release:    CROC1%{?dist}
Summary:    Python client for Masakari REST API.

License:    ASL 2.0
URL:        http://docs.openstack.org/developer/masakari

Source0:    https://tarballs.openstack.org/%{package_name}/%{package_name}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  rdo-rpm-macros

BuildRequires:  python-oslo-sphinx
BuildRequires:  python-sphinx

# Python requires
Requires:   python-argparse
Requires:   python-pbr
Requires:   python-prettytable
Requires:   python-six

## Openstack requires
Requires:   python-openstacksdk
Requires:   python-osc-lib
Requires:   python-oslo-serialization
Requires:   python-oslo-utils


%description
masakariclient module and a CLI tool for masakari


%prep
%setup -q -n %{package_name}-%{upstream_version}

export PBR_VERSION=%{version}

# Let's handle dependencies ourseleves
rm -f *requirements.txt


%build
%py2_build
%{__python2} setup.py build_sphinx


%install
%py2_install


%files
%{_bindir}/*
%{python2_sitelib}/%{srcname}/*
%{python2_sitelib}/python_%{srcname}*egg-info/


%changelog
* Mon Dec 12 2016 Vladislav Odintsov <odivlad@gmail.com> - 2.0.0-1
- Initial packaging.
