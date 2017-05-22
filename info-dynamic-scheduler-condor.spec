Summary: Plugins for the lcg-info-dynamic-scheduler GIP plugin
Name: lcg-info-dynamic-scheduler-condor
Version: 1.1
Release: 1%{?dist}
License: Apache Software License
Vendor: EMI
URL: http://glite.cern.ch/
Group: Applications/Internet
BuildArch: noarch
Requires: condor
Requires: dynsched-generic  >= 2.5.3
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes
Source: /home/rebatto/glite-condor-infoprovider

%description
HTCondor specific plugins for the lcg-info-dynamic-scheduler GIP plugin.

%prep
cp -p ../glite-info-dynamic-condor ../lrmsinfo-condor ../condor.conf .

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/libexec
mkdir -p %{buildroot}/etc/lrms
cp glite-info-dynamic-condor lrmsinfo-condor %{buildroot}/usr/libexec
cp condor.conf %{buildroot}/etc/lrms

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/libexec/glite-info-dynamic-condor
/usr/libexec/lrmsinfo-condor
%config /etc/lrms/condor.conf

%post
TMPVAR=`grep -Eo '\[LRMS\]' /etc/lrms/scheduler.conf`
if [ "x${TMPVAR}" == "x" ] ; then
    cat << EOF >> /etc/lrms/scheduler.conf
[LRMS]
lrms_backend_cmd: /usr/libexec/lrmsinfo-condor
[Scheduler]
cycle_time: 0
EOF
fi
