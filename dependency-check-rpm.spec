Name:    dependency-check-rpm
Version: 5.3.0
Release: 2
Summary: OWASP dependency-check is a software composition analysis utility that detects publicly disclosed vulnerabilities in application dependencies.
Group:   Development Tools
License: ASL 2.0
Source0: build.sh
URL:     https://dl.bintray.com/jeremy-long/owasp/dependency-check-%{version}-release.zip

%description
OWASP dependency-check-cli is an command line tool that uses dependency-check-core to detect
publicly disclosed vulnerabilities associated with the scanned project dependencies. The
tool will generate a report listing the dependency, any identified Common Platform Enumeration
(CPE) identifiers, and the associated Common Vulnerability and Exposure (CVE) entries.

%prep
echo "curl -L %{url} > dependency-check-release.zip"
curl -L %{url} > dependency-check-release.zip
ls
find . -name dependency-check-release.zip
unzip -q dependency-check-release.zip
ls
ls dependency-check

%install
install -d -m 0775 %{buildroot}/var/lib/dependency-check
mv dependency-check/* %{buildroot}/var/lib/dependency-check

%files
/var/lib/dependency-check
