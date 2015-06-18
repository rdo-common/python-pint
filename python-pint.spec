%global pypi_name Pint

Name:           python-pint
Version:        0.6
Release:        3%{?dist}
Summary:        Physical quantities module

License:        BSD
URL:            https://github.com/hgrecco/pint
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-sphinx
BuildRequires:  python-setuptools


%description
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants.


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%{__python2} setup.py build

# generate html docs

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%check
%{__python2} setup.py test


%files
%doc html LICENSE docs/_themes/LICENSE
%{python2_sitelib}/pint
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Matthias Runge <mrunge@redhat.com> - 0.6-2
- change BR python-devel to python2-devel (rhbz#1173109)

* Thu Dec 11 2014 Matthias Runge <mrunge@redhat.com> - 0.6-1
- Initial package.
