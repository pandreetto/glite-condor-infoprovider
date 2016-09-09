topdir := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
rpm: condor.conf glite-info-dynamic-condor info-dynamic-scheduler-condor.spec lrmsinfo-condor
	[ -d ./BUILD ] || mkdir BUILD ;\
	[ -d ./RPMS/noarch ] || mkdir -p RPMS/noarch ;\
	rpmbuild --define "_topdir $(topdir)" -bb info-dynamic-scheduler-condor.spec
clean:
	rm -rf BUILD RPMS
