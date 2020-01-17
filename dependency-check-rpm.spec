Name:    dependency-check-rpm
Version: 5.3.0
Release: 1
Summary: OWASP dependency-check is a software composition analysis utility that detects publicly disclosed vulnerabilities in application dependencies.
Group:   Development Tools
License: ASL 2.0
Source0: build.sh
Source1: https://dl.bintray.com/jeremy-long/owasp/dependency-check-%{version}-release.zip

%description
OWASP dependency-check-cli is an command line tool that uses dependency-check-core to detect
publicly disclosed vulnerabilities associated with the scanned project dependencies. The
tool will generate a report listing the dependency, any identified Common Platform Enumeration
(CPE) identifiers, and the associated Common Vulnerability and Exposure (CVE) entries.

%prep
ls
unzip dependency-check-%{version}-release.zip
ls

%install
ls
pwd
install -d -m 0775 %{buildroot}/var/lib/dependency-check
#install -d -m 0775 %{buildroot}/etc/nginx/conf.d
#install -p -m 0664 %{SOURCE1} %{buildroot}/var/www/repos/retire-js-repository/jsrepository.json
#install -p -m 0664 %{SOURCE2} %{buildroot}/var/www/repos/retire-js-repository/npmrepository.json
#install -p -m 0664 %{SOURCE3} %{buildroot}/etc/nginx/conf.d/retire-js-repository.conf

#%files
#/var/www/repos/retire-js-repository/jsrepository.json
#/var/www/repos/retire-js-repository/npmrepository.json
#/etc/nginx/conf.d/retire-js-repository.conf
