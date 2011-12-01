%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: python-pylons
Version: 0.9.7
Release: 2%{?dist}
Summary: Pylons web framework

Group: Development/Languages
License: BSD
URL: http://www.pylonshq.com/
Source0: http://pypi.python.org/packages/source/P/Pylons/Pylons-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: python-setuptools-devel

# For the test suite
BuildRequires: python-routes python-webhelpers python-beaker
BuildRequires: python-paste python-paste-script python-paste-deploy
BuildRequires: python-formencode python-simplejson python-decorator
BuildRequires: python-nose python-mako python-webob python-weberror
BuildRequires: python-tempita python-webtest python-turbocheetah
BuildRequires: python-turbokid python-myghty python-genshi python-jinja2
BuildRequires: python-coverage

Requires: python-routes >= 1.10.3
Requires: python-webhelpers >= 0.6.4
# Some versions of Beaker caused FTBFS bug 511511
Requires: python-beaker >= 1.3.1-5
Requires: python-paste >= 1.7.2
Requires: python-paste-script >= 1.7.3
Requires: python-paste-deploy >= 1.3.3
Requires: python-formencode >= 1.2.1
Requires: python-simplejson >= 2.0.8
Requires: python-decorator >= 2.3.2
Requires: python-nose >= 0.10.4
Requires: python-mako >= 0.2.4
Requires: python-webob >= 0.9.6.1
Requires: python-weberror >= 0.10.1
Requires: python-webtest >= 1.1
Requires: python-tempita >= 0.2
# TurboGears hooks pylons (if present) and barfs w/o myghty (Bug 497244)
Requires: python-myghty >= 1.1


%description
The Pylons web framework is aimed at making webapps and large programmatic
website development in Python easy. Several key points:

* A framework to make writing web applications in Python easy
* Inspired by Rails and TurboGears
* Utilizes a minimalist, component-based philosophy that makes it easy to
  expand on
* Harness existing knowledge about Python


%prep
%setup -q -n Pylons-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check
PYTHONPATH=$(pwd) nosetests -v


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE README.txt
%{python_sitelib}/*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Kyle VanderBeek <kylev@kylev.com> - 0.9.7-1
- Update to 0.9.7 final
- Remove some cleanups that have been fixed upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-0.2.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 0.9.7-0.1.rc4
- Update to 0.9.7rc4
- Update all requirements, and add python-webtest
- Run the test suite

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.6.2-2
- Rebuild for Python 2.6

* Fri Jun 13 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.6.2-1
- Update to 0.9.6.2
- remove now-gone docs/ tree
- Use find to get rid of OSX packaging artifacts ("._" files)

* Thu May 29 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.6.1-3
- Use new style buildroot macro instead of RPM_BUILD_ROOT

* Sun May 11 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.6.1-2
- Fix rpmlint errors.
- Add docs.

* Wed Apr  9 2008 Kyle VanderBeek <kylev@kylev.com> - 0.9.6.1-1
- Initial version.
