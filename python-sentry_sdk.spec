Name:		python-sentry-sdk
Version:	2.47.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/sentry_sdk/sentry_sdk-%{version}.tar.gz
Summary:	Python client for Sentry (https://sentry.io)
URL:		https://pypi.org/project/sentry_sdk/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Python client for Sentry (https://sentry.io)

%files
%{py_sitedir}/sentry_sdk
%{py_sitedir}/sentry_sdk-*.*-info
