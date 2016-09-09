topdir := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DEPS = condor.conf glite-info-dynamic-condor \
       info-dynamic-scheduler-condor.spec lrmsinfo-condor

rpm: RPMS/noarch/lcg-info-dynamic-scheduler-condor-1.0-1.el7.noarch.rpm

RPMS/noarch/lcg-info-dynamic-scheduler-condor-1.0-1.el7.noarch.rpm: $(DEPS)
	[ -d ./BUILD ] || mkdir BUILD ;\
	[ -d ./RPMS/noarch ] || mkdir -p RPMS/noarch ;\
	rpmbuild --define "_topdir $(topdir)" -bb info-dynamic-scheduler-condor.spec

clean:
	rm -rf BUILD RPMS
