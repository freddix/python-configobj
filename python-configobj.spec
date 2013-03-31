%define		module	configobj

Summary:	Reading and writing config files
Name:		python-%{module}
Version:	4.7.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://www.voidspace.org.uk/downloads/%{module}-%{version}.zip
# Source0-md5:	51cee395cfbf831339b03f72706de18e
URL:		http://www.voidspace.org.uk/python/configobj.html
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reading and writing config files.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install	\
	--optimize=2		\
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*

