#!/bin/bash

list_dependencies=(rpm-build rpmdevtools)

for i in ${list_dependencies[*]}
do
    if ! rpm -qa | grep -qw $i; then
        echo "__________Dont installed '$i'__________"
        #yum -y install $i
    fi
done

mkdir -p ./{RPMS,SRPMS,BUILD,SOURCES,SPECS}
spectool -g -C SOURCES dependency-check-rpm.spec
rpmbuild --quiet --define "_topdir `pwd`" -bb dependency-check-rpm.spec
