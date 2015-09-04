%global pypi_name Pint


%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-pint
Version:        0.6
Release:        4%{?dist}
Summary:        Physical quantities module

License:        BSD
URL:            https://github.com/hgrecco/pint
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

%description
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants.

%package -n python2-%{pypi_name}
Summary:        Physical quantities module
Provides:       python-%{pypi_name} = %{upstream_version}
Obsoletes:      python-%{pypi_name} < %{upstream_version}

BuildRequires:  python2-devel
BuildRequires:  python-sphinx
BuildRequires:  python-setuptools

# python_provide does not exist in CBS Cloud buildroot
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants.

%package -n python2-%{pypi_name}-doc
Summary:        Documentation for the pint module
%{?python_provide:%python_provide python2-%{pypi_name}-doc}
# python_provide does not exist in CBS Cloud buildroot
Provides:       python-%{pypi_name}-doc = %{upstream_version}
Obsoletes:      python-%{pypi_name}-doc < %{upstream_version}

%description -n python2-%{pypi_name}-doc
Documentation for the pint module

#python3 subpackage
%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Physical quantities module
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants.
%endif

%if 0%{?with_python3}
%package -n python3-%{pypi_name}-doc
Summary:        Documentation for the pint module
%{?python_provide:%python_provide python3-%{pypi_name}-doc}
BuildRequires:  python3-sphinx

%description -n python3-%{pypi_name}-doc
Documentation for the pint module
%endif

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%{__python2} setup.py build

# generate html docs

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build docs html

%if 0%{?with_python3}
%{__python3} setup.py build
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%check
%{__python2} setup.py test

%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-%{pypi_name}
%doc README
%license LICENSE
%{python2_sitelib}/pint
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}-doc
%doc html
%license docs/_themes/LICENSE

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README
%license LICENSE
%{python3_sitelib}/pint
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-%{pypi_name}-doc
%doc html
%license docs/_themes/LICENSE
%endif

%changelog
* Fri Sep 04 2015 Chandan Kumar <chkumar246@gmail.com> - 0.6-4
- Add python2 and python3 subpackages

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Matthias Runge <mrunge@redhat.com> - 0.6-2
- change BR python-devel to python2-devel (rhbz#1173109)

* Thu Dec 11 2014 Matthias Runge <mrunge@redhat.com> - 0.6-1
- Initial package.
