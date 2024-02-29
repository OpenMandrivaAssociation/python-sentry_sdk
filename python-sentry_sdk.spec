Name:		python-sentry-sdk
Version:	1.40.6
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/sentry-sdk/sentry-sdk-%{version}.tar.gz
Summary:	Python client for Sentry (https://sentry.io)
URL:		https://pypi.org/project/sentry_sdk/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python client for Sentry (https://sentry.io)

%prep
%autosetup -p1 -n sentry-sdk-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/sentry_sdk
%{py_sitedir}/sentry_sdk-*.*-info
