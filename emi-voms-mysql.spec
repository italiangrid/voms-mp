Name: emi-voms-mysql
Version: 1.1.0
Release: 2%{?dist}
Summary: Virtual Organization Mebership Service (MySQL metapackage)

Group:          System Environment/Libraries
License:        ASL 2.0
URL: http://italiangrid.github.com/voms

Requires: voms-admin-server
Requires: voms-admin-client
Requires: glite-info-provider-service
Requires: fetch-crl
Requires: voms-server
Requires: voms-mysql-plugin
Requires: bdii
Requires: mysql-server
Requires: emi-version

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Packager: Andrea Ceccanti <andrea.ceccanti@cnaf.infn.it>
Source : voms-mp.tar.gz

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This is a metapackage for an MySQL-based VOMS server installation.

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)


%changelog
* Tue Feb 19 2013 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.1.0-2
- Readded lost dependency on emi-version

* Fri Jan 18 2013 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.1.0-1
- EMI 3 metapackage drops dependency on YAIM

* Thu Dec 15 2011 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 1.0.2-1
- First packaging.
