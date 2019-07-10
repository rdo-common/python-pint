%global pypi_name Pint
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-pint
Version:        0.9
Release:        3%{?dist}
Summary:        Physical quantities module

License:        BSD
URL:            https://github.com/hgrecco/pint
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# Use context manager for assertWarns and fix DeprecationWarning
Patch0: https://github.com/hgrecco/pint/commit/955102b318a4ecc34afd0f366e826ef174fe647b.patch

BuildArch:      noarch

%description
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants.

%package -n python3-pint
Summary:        Physical quantities module
%{?python_provide:%python_provide python3-pint}

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools

%description -n python3-pint
Pint is Python module/package to define, operate and manipulate physical
quantities: the product of a numerical value and a unit of measurement.
It allows arithmetic operations between them and conversions from and
to different units.

It is distributed with a comprehensive list of physical units, prefixes
and constants.

%package -n python3-pint-doc
Summary:        Documentation for the pint module
%{?python_provide:%python_provide python3-pint-doc}
BuildRequires:  python3-sphinx
BuildRequires:  python3-matplotlib

%description -n python3-pint-doc
Documentation for the pint module

%prep
%setup -q -n %{pypi_name}-%{version}

# Babel tests are not ready, see https://github.com/hgrecco/pint/issues/663
rm pint/testsuite/test_babel.py

%build
%py3_build
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-pint
%doc README
%license LICENSE
%{python3_sitelib}/pint
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-pint-doc
%doc html
%license docs/_themes/LICENSE

%changelog
* Wed Jul 10 2019 Matthias Runge <mrunge@redhat.com> - 0.9-3
- Use context manager for assertWarns and fix DeprecationWarning
  resolves: rhbz#1706212

* Sun Mar 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-2
- Subpackages python2-pint, python2-pint-doc have been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Feb 25 2019 Yatin Karel <ykarel@redhat.com> - 0.9-1
- Update to 0.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sun Sep 06 2015 Matthias Runge <mrunge@redhat.com> - 0.6-5
- fix uppercase/lowercase naming, fix obsoletes

* Fri Sep 04 2015 Chandan Kumar <chkumar246@gmail.com> - 0.6-4
- Add python2 and python3 subpackages

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 15 2014 Matthias Runge <mrunge@redhat.com> - 0.6-2
- change BR python-devel to python2-devel (rhbz#1173109)

* Thu Dec 11 2014 Matthias Runge <mrunge@redhat.com> - 0.6-1
- Initial package.
