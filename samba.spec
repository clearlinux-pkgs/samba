#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : samba
Version  : 4.14.7
Release  : 140
URL      : https://download.samba.org/pub/samba/stable/samba-4.14.7.tar.gz
Source0  : https://download.samba.org/pub/samba/stable/samba-4.14.7.tar.gz
Source1  : samba.tmpfiles
Summary  : Generate parsers / DCE/RPC-clients from IDL
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 CC-BY-4.0 EPL-1.0 GPL-3.0 HPND ISC MIT Public-Domain X11
Requires: samba-bin = %{version}-%{release}
Requires: samba-config = %{version}-%{release}
Requires: samba-data = %{version}-%{release}
Requires: samba-lib = %{version}-%{release}
Requires: samba-libexec = %{version}-%{release}
Requires: samba-license = %{version}-%{release}
Requires: samba-python = %{version}-%{release}
Requires: samba-python3 = %{version}-%{release}
Requires: samba-services = %{version}-%{release}
BuildRequires : LVM2-dev
BuildRequires : Linux-PAM-dev
BuildRequires : Markdown
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : cups-dev
BuildRequires : dbus-dev
BuildRequires : dnspython
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : fuse-dev
BuildRequires : gdb
BuildRequires : gmp-dev
BuildRequires : gnutls-dev
BuildRequires : gpgme-dev
BuildRequires : intltool-dev
BuildRequires : iso8601
BuildRequires : jansson-dev
BuildRequires : kdoctools-dev
BuildRequires : krb5-dev
BuildRequires : ldb-dev
BuildRequires : ldb-extras
BuildRequires : libaio-dev
BuildRequires : libarchive-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libgpg-error-dev
BuildRequires : libtirpc-dev
BuildRequires : libunwind-dev
BuildRequires : lmdb-dev
BuildRequires : ncurses-dev
BuildRequires : openldap-dev
BuildRequires : openssl-dev
BuildRequires : perl-Parse-Yapp
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : systemd-dev
BuildRequires : talloc-dev
BuildRequires : talloc-extras
BuildRequires : tdb-dev
BuildRequires : tevent-dev
BuildRequires : zlib-dev
Patch1: 0001-add-mock-disable-static-option.patch
Patch2: 0002-timestamps.patch
Patch3: 0003-docbook-fix.patch
Patch4: 0004-no-man-pages.patch
Patch5: 0005-Removed-stropts.h-checking.patch

%description
Please see the wiki page at:
http://wiki.samba.org/index.php/WinTest
for details on configuring and running wintest

%package bin
Summary: bin components for the samba package.
Group: Binaries
Requires: samba-data = %{version}-%{release}
Requires: samba-libexec = %{version}-%{release}
Requires: samba-config = %{version}-%{release}
Requires: samba-license = %{version}-%{release}
Requires: samba-services = %{version}-%{release}

%description bin
bin components for the samba package.


%package config
Summary: config components for the samba package.
Group: Default

%description config
config components for the samba package.


%package data
Summary: data components for the samba package.
Group: Data

%description data
data components for the samba package.


%package dev
Summary: dev components for the samba package.
Group: Development
Requires: samba-lib = %{version}-%{release}
Requires: samba-bin = %{version}-%{release}
Requires: samba-data = %{version}-%{release}
Provides: samba-devel = %{version}-%{release}
Requires: samba = %{version}-%{release}

%description dev
dev components for the samba package.


%package lib
Summary: lib components for the samba package.
Group: Libraries
Requires: samba-data = %{version}-%{release}
Requires: samba-libexec = %{version}-%{release}
Requires: samba-license = %{version}-%{release}

%description lib
lib components for the samba package.


%package libexec
Summary: libexec components for the samba package.
Group: Default
Requires: samba-config = %{version}-%{release}
Requires: samba-license = %{version}-%{release}

%description libexec
libexec components for the samba package.


%package license
Summary: license components for the samba package.
Group: Default

%description license
license components for the samba package.


%package python
Summary: python components for the samba package.
Group: Default
Requires: samba-python3 = %{version}-%{release}

%description python
python components for the samba package.


%package python3
Summary: python3 components for the samba package.
Group: Default
Requires: python3-core

%description python3
python3 components for the samba package.


%package services
Summary: services components for the samba package.
Group: Systemd services

%description services
services components for the samba package.


%prep
%setup -q -n samba-4.14.7
cd %{_builddir}/samba-4.14.7
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629848052
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --with-systemd \
--systemd-install-services \
--enable-fhs \
--with-system-mitkrb5 \
--with-experimental-mit-ad-dc \
--accel-aes=intelaesni \
--nopyc \
--nopyo \
--with-cluster-support \
--with-shared-modules=idmap_rid,idmap_tdb2,idmap_ad
make  %{?_smp_mflags}  PYTHON=python3

%install
export SOURCE_DATE_EPOCH=1629848052
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/samba
cp %{_builddir}/samba-4.14.7/COPYING %{buildroot}/usr/share/package-licenses/samba/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/samba-4.14.7/ctdb/COPYING %{buildroot}/usr/share/package-licenses/samba/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/samba-4.14.7/examples/pcap2nbench/COPYING %{buildroot}/usr/share/package-licenses/samba/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/samba-4.14.7/librpc/idl/IDL_LICENSE.txt %{buildroot}/usr/share/package-licenses/samba/41bb27089429d9d6febf18e4237cf04d81fcc737
cp %{_builddir}/samba-4.14.7/source3/librpc/idl/IDL_LICENSE.txt %{buildroot}/usr/share/package-licenses/samba/41bb27089429d9d6febf18e4237cf04d81fcc737
cp %{_builddir}/samba-4.14.7/source4/heimdal/HEIMDAL-LICENCE.txt %{buildroot}/usr/share/package-licenses/samba/2004537f8b8c3aee21a03133e1f4aaed6dc9a90c
cp %{_builddir}/samba-4.14.7/source4/librpc/idl/IDL_LICENSE.txt %{buildroot}/usr/share/package-licenses/samba/41bb27089429d9d6febf18e4237cf04d81fcc737
cp %{_builddir}/samba-4.14.7/source4/setup/adprep/WindowsServerDocs/LICENSE %{buildroot}/usr/share/package-licenses/samba/8ea3090863330c454ba0f536177bc1a8ee5de1b0
cp %{_builddir}/samba-4.14.7/source4/setup/adprep/WindowsServerDocs/LICENSE-CODE %{buildroot}/usr/share/package-licenses/samba/c75814379854cf0de2911449fca8c9138520f140
cp %{_builddir}/samba-4.14.7/third_party/pep8/LICENSE %{buildroot}/usr/share/package-licenses/samba/37984ab2838de7795cd108336e00844e490457cb
cp %{_builddir}/samba-4.14.7/third_party/popt/COPYING %{buildroot}/usr/share/package-licenses/samba/61bb7a8ea669080cfc9e7dbf37079eae70b535fb
%make_install PYTHON=python3 "%{?_smp_mflags}"
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/samba.conf
## Remove excluded files
rm -f %{buildroot}/usr/bin/ldbadd
rm -f %{buildroot}/usr/bin/ldbdel
rm -f %{buildroot}/usr/bin/ldbedit
rm -f %{buildroot}/usr/bin/ldbmodify
rm -f %{buildroot}/usr/bin/ldbrename
rm -f %{buildroot}/usr/bin/ldbsearch
rm -f %{buildroot}/usr/lib/python3*/site-packages/_tevent.cpython-3*-x86_64-linux-gnu.so
rm -f %{buildroot}/usr/lib/python3*/site-packages/ldb.cpython-3*-x86_64-linux-gnu.so
rm -f %{buildroot}/usr/lib/python3*/site-packages/talloc.cpython-3*-x86_64-linux-gnu.so
rm -f %{buildroot}/usr/lib/python3*/site-packages/tdb.cpython-3*-x86_64-linux-gnu.so
rm -f %{buildroot}/usr/lib64/ldb/libpytalloc-util.cpython-3*-x86-64-linux-gnu.so.*
## install_append content
install -d -m 755 %{buildroot}/usr/lib/systemd/system
install -m 644 ./bin/default/packaging/systemd/*.service %{buildroot}/usr/lib/systemd/system
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cifsdd
/usr/bin/ctdb
/usr/bin/ctdb_diagnostics
/usr/bin/ctdbd
/usr/bin/ctdbd_wrapper
/usr/bin/dbwrap_tool
/usr/bin/dumpmscat
/usr/bin/eventlogadm
/usr/bin/findsmb
/usr/bin/gentest
/usr/bin/locktest
/usr/bin/ltdbtool
/usr/bin/masktest
/usr/bin/mdfind
/usr/bin/mvxattr
/usr/bin/ndrdump
/usr/bin/net
/usr/bin/nmbd
/usr/bin/nmblookup
/usr/bin/ntlm_auth
/usr/bin/oLschema2ldif
/usr/bin/onnode
/usr/bin/pdbedit
/usr/bin/ping_pong
/usr/bin/profiles
/usr/bin/regdiff
/usr/bin/regpatch
/usr/bin/regshell
/usr/bin/regtree
/usr/bin/rpcclient
/usr/bin/samba
/usr/bin/samba-gpupdate
/usr/bin/samba-regedit
/usr/bin/samba-tool
/usr/bin/samba_dnsupdate
/usr/bin/samba_downgrade_db
/usr/bin/samba_kcc
/usr/bin/samba_spnupdate
/usr/bin/samba_upgradedns
/usr/bin/sharesec
/usr/bin/smbcacls
/usr/bin/smbclient
/usr/bin/smbcontrol
/usr/bin/smbcquotas
/usr/bin/smbd
/usr/bin/smbget
/usr/bin/smbpasswd
/usr/bin/smbspool
/usr/bin/smbstatus
/usr/bin/smbtar
/usr/bin/smbtorture
/usr/bin/smbtree
/usr/bin/testparm
/usr/bin/wbinfo
/usr/bin/winbindd

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/samba.conf

%files data
%defattr(-,root,root,-)
/usr/share/ctdb/events/legacy/00.ctdb.script
/usr/share/ctdb/events/legacy/01.reclock.script
/usr/share/ctdb/events/legacy/05.system.script
/usr/share/ctdb/events/legacy/06.nfs.script
/usr/share/ctdb/events/legacy/10.interface.script
/usr/share/ctdb/events/legacy/11.natgw.script
/usr/share/ctdb/events/legacy/11.routing.script
/usr/share/ctdb/events/legacy/13.per_ip_routing.script
/usr/share/ctdb/events/legacy/20.multipathd.script
/usr/share/ctdb/events/legacy/31.clamd.script
/usr/share/ctdb/events/legacy/40.vsftpd.script
/usr/share/ctdb/events/legacy/41.httpd.script
/usr/share/ctdb/events/legacy/48.netbios.script
/usr/share/ctdb/events/legacy/49.winbind.script
/usr/share/ctdb/events/legacy/50.samba.script
/usr/share/ctdb/events/legacy/60.nfs.script
/usr/share/ctdb/events/legacy/70.iscsi.script
/usr/share/ctdb/events/legacy/91.lvs.script
/usr/share/samba/admx/en-US/samba.adml
/usr/share/samba/admx/samba.admx
/usr/share/samba/setup/ad-schema/AD_DS_Attributes__Windows_Server_2012_R2.ldf
/usr/share/samba/setup/ad-schema/AD_DS_Attributes__Windows_Server_2016.ldf
/usr/share/samba/setup/ad-schema/AD_DS_Classes__Windows_Server_2012_R2.ldf
/usr/share/samba/setup/ad-schema/AD_DS_Classes__Windows_Server_2016.ldf
/usr/share/samba/setup/ad-schema/Attributes_for_AD_DS__Windows_Server_2008_R2.ldf
/usr/share/samba/setup/ad-schema/Attributes_for_AD_DS__Windows_Server_2012.ldf
/usr/share/samba/setup/ad-schema/Classes_for_AD_DS__Windows_Server_2008_R2.ldf
/usr/share/samba/setup/ad-schema/Classes_for_AD_DS__Windows_Server_2012.ldf
/usr/share/samba/setup/ad-schema/MS-AD_Schema_2K8_Attributes.txt
/usr/share/samba/setup/ad-schema/MS-AD_Schema_2K8_Classes.txt
/usr/share/samba/setup/ad-schema/MS-AD_Schema_2K8_R2_Attributes.txt
/usr/share/samba/setup/ad-schema/MS-AD_Schema_2K8_R2_Classes.txt
/usr/share/samba/setup/ad-schema/licence.txt
/usr/share/samba/setup/adprep/WindowsServerDocs/Forest-Wide-Updates.md
/usr/share/samba/setup/adprep/WindowsServerDocs/Sch49.ldf.diff
/usr/share/samba/setup/adprep/WindowsServerDocs/Sch50.ldf.diff
/usr/share/samba/setup/adprep/WindowsServerDocs/Sch51.ldf.diff
/usr/share/samba/setup/adprep/WindowsServerDocs/Sch57.ldf.diff
/usr/share/samba/setup/adprep/WindowsServerDocs/Sch59.ldf.diff
/usr/share/samba/setup/adprep/WindowsServerDocs/Schema-Updates.md
/usr/share/samba/setup/adprep/fix-forest-rev.ldf
/usr/share/samba/setup/aggregate_schema.ldif
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k0.txt
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k3.txt
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k3R2.txt
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k8.txt
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k8R2.txt
/usr/share/samba/setup/dns_update_list
/usr/share/samba/setup/extended-rights.ldif
/usr/share/samba/setup/idmap_init.ldif
/usr/share/samba/setup/krb5.conf
/usr/share/samba/setup/named.conf
/usr/share/samba/setup/named.conf.dlz
/usr/share/samba/setup/named.conf.update
/usr/share/samba/setup/named.txt
/usr/share/samba/setup/prefixMap.txt
/usr/share/samba/setup/provision.ldif
/usr/share/samba/setup/provision.reg
/usr/share/samba/setup/provision.zone
/usr/share/samba/setup/provision_basedn.ldif
/usr/share/samba/setup/provision_basedn_modify.ldif
/usr/share/samba/setup/provision_basedn_options.ldif
/usr/share/samba/setup/provision_basedn_references.ldif
/usr/share/samba/setup/provision_computers_add.ldif
/usr/share/samba/setup/provision_computers_modify.ldif
/usr/share/samba/setup/provision_configuration.ldif
/usr/share/samba/setup/provision_configuration_basedn.ldif
/usr/share/samba/setup/provision_configuration_modify.ldif
/usr/share/samba/setup/provision_configuration_references.ldif
/usr/share/samba/setup/provision_dns_accounts_add.ldif
/usr/share/samba/setup/provision_dns_add_samba.ldif
/usr/share/samba/setup/provision_dnszones_add.ldif
/usr/share/samba/setup/provision_dnszones_modify.ldif
/usr/share/samba/setup/provision_dnszones_partitions.ldif
/usr/share/samba/setup/provision_group_policy.ldif
/usr/share/samba/setup/provision_init.ldif
/usr/share/samba/setup/provision_partitions.ldif
/usr/share/samba/setup/provision_privilege.ldif
/usr/share/samba/setup/provision_rootdse_add.ldif
/usr/share/samba/setup/provision_rootdse_modify.ldif
/usr/share/samba/setup/provision_schema_basedn.ldif
/usr/share/samba/setup/provision_schema_basedn_modify.ldif
/usr/share/samba/setup/provision_self_join.ldif
/usr/share/samba/setup/provision_self_join_config.ldif
/usr/share/samba/setup/provision_self_join_modify.ldif
/usr/share/samba/setup/provision_self_join_modify_config.ldif
/usr/share/samba/setup/provision_self_join_modify_schema.ldif
/usr/share/samba/setup/provision_users.ldif
/usr/share/samba/setup/provision_users_add.ldif
/usr/share/samba/setup/provision_users_modify.ldif
/usr/share/samba/setup/provision_well_known_sec_princ.ldif
/usr/share/samba/setup/schema_samba4.ldif
/usr/share/samba/setup/secrets.ldif
/usr/share/samba/setup/secrets_dns.ldif
/usr/share/samba/setup/secrets_init.ldif
/usr/share/samba/setup/share.ldif
/usr/share/samba/setup/spn_update_list
/usr/share/samba/setup/ypServ30.ldif

%files dev
%defattr(-,root,root,-)
/usr/include/samba-4.0/charset.h
/usr/include/samba-4.0/core/doserr.h
/usr/include/samba-4.0/core/error.h
/usr/include/samba-4.0/core/hresult.h
/usr/include/samba-4.0/core/ntstatus.h
/usr/include/samba-4.0/core/ntstatus_gen.h
/usr/include/samba-4.0/core/werror.h
/usr/include/samba-4.0/core/werror_gen.h
/usr/include/samba-4.0/credentials.h
/usr/include/samba-4.0/dcerpc.h
/usr/include/samba-4.0/dcerpc_server.h
/usr/include/samba-4.0/dcesrv_core.h
/usr/include/samba-4.0/domain_credentials.h
/usr/include/samba-4.0/gen_ndr/atsvc.h
/usr/include/samba-4.0/gen_ndr/auth.h
/usr/include/samba-4.0/gen_ndr/dcerpc.h
/usr/include/samba-4.0/gen_ndr/drsblobs.h
/usr/include/samba-4.0/gen_ndr/drsuapi.h
/usr/include/samba-4.0/gen_ndr/krb5pac.h
/usr/include/samba-4.0/gen_ndr/lsa.h
/usr/include/samba-4.0/gen_ndr/misc.h
/usr/include/samba-4.0/gen_ndr/nbt.h
/usr/include/samba-4.0/gen_ndr/ndr_atsvc.h
/usr/include/samba-4.0/gen_ndr/ndr_dcerpc.h
/usr/include/samba-4.0/gen_ndr/ndr_drsblobs.h
/usr/include/samba-4.0/gen_ndr/ndr_drsuapi.h
/usr/include/samba-4.0/gen_ndr/ndr_krb5pac.h
/usr/include/samba-4.0/gen_ndr/ndr_misc.h
/usr/include/samba-4.0/gen_ndr/ndr_nbt.h
/usr/include/samba-4.0/gen_ndr/ndr_samr.h
/usr/include/samba-4.0/gen_ndr/ndr_samr_c.h
/usr/include/samba-4.0/gen_ndr/ndr_svcctl.h
/usr/include/samba-4.0/gen_ndr/ndr_svcctl_c.h
/usr/include/samba-4.0/gen_ndr/netlogon.h
/usr/include/samba-4.0/gen_ndr/samr.h
/usr/include/samba-4.0/gen_ndr/security.h
/usr/include/samba-4.0/gen_ndr/server_id.h
/usr/include/samba-4.0/gen_ndr/svcctl.h
/usr/include/samba-4.0/ldb_wrap.h
/usr/include/samba-4.0/libsmbclient.h
/usr/include/samba-4.0/lookup_sid.h
/usr/include/samba-4.0/machine_sid.h
/usr/include/samba-4.0/ndr.h
/usr/include/samba-4.0/ndr/ndr_dcerpc.h
/usr/include/samba-4.0/ndr/ndr_drsblobs.h
/usr/include/samba-4.0/ndr/ndr_drsuapi.h
/usr/include/samba-4.0/ndr/ndr_krb5pac.h
/usr/include/samba-4.0/ndr/ndr_nbt.h
/usr/include/samba-4.0/ndr/ndr_svcctl.h
/usr/include/samba-4.0/netapi.h
/usr/include/samba-4.0/param.h
/usr/include/samba-4.0/passdb.h
/usr/include/samba-4.0/policy.h
/usr/include/samba-4.0/rpc_common.h
/usr/include/samba-4.0/samba/session.h
/usr/include/samba-4.0/samba/version.h
/usr/include/samba-4.0/share.h
/usr/include/samba-4.0/smb2_lease_struct.h
/usr/include/samba-4.0/smb_ldap.h
/usr/include/samba-4.0/smbconf.h
/usr/include/samba-4.0/smbldap.h
/usr/include/samba-4.0/tdr.h
/usr/include/samba-4.0/tsocket.h
/usr/include/samba-4.0/tsocket_internal.h
/usr/include/samba-4.0/util/attr.h
/usr/include/samba-4.0/util/blocking.h
/usr/include/samba-4.0/util/data_blob.h
/usr/include/samba-4.0/util/debug.h
/usr/include/samba-4.0/util/discard.h
/usr/include/samba-4.0/util/fault.h
/usr/include/samba-4.0/util/genrand.h
/usr/include/samba-4.0/util/idtree.h
/usr/include/samba-4.0/util/idtree_random.h
/usr/include/samba-4.0/util/signal.h
/usr/include/samba-4.0/util/substitute.h
/usr/include/samba-4.0/util/tevent_ntstatus.h
/usr/include/samba-4.0/util/tevent_unix.h
/usr/include/samba-4.0/util/tevent_werror.h
/usr/include/samba-4.0/util/tfork.h
/usr/include/samba-4.0/util/time.h
/usr/include/samba-4.0/util_ldb.h
/usr/include/samba-4.0/wbclient.h
/usr/lib64/libdcerpc-binding.so
/usr/lib64/libdcerpc-samr.so
/usr/lib64/libdcerpc-server-core.so
/usr/lib64/libdcerpc-server.so
/usr/lib64/libdcerpc.so
/usr/lib64/libndr-krb5pac.so
/usr/lib64/libndr-nbt.so
/usr/lib64/libndr-standard.so
/usr/lib64/libndr.so
/usr/lib64/libnetapi.so
/usr/lib64/libnss_winbind.so
/usr/lib64/libnss_wins.so
/usr/lib64/libsamba-credentials.so
/usr/lib64/libsamba-errors.so
/usr/lib64/libsamba-hostconfig.so
/usr/lib64/libsamba-passdb.so
/usr/lib64/libsamba-policy.cpython-39-x86-64-linux-gnu.so
/usr/lib64/libsamba-util.so
/usr/lib64/libsamdb.so
/usr/lib64/libsmbclient.so
/usr/lib64/libsmbconf.so
/usr/lib64/libsmbldap.so
/usr/lib64/libtevent-util.so
/usr/lib64/libwbclient.so
/usr/lib64/pkgconfig/dcerpc.pc
/usr/lib64/pkgconfig/dcerpc_samr.pc
/usr/lib64/pkgconfig/dcerpc_server.pc
/usr/lib64/pkgconfig/ndr.pc
/usr/lib64/pkgconfig/ndr_krb5pac.pc
/usr/lib64/pkgconfig/ndr_nbt.pc
/usr/lib64/pkgconfig/ndr_standard.pc
/usr/lib64/pkgconfig/netapi.pc
/usr/lib64/pkgconfig/samba-credentials.pc
/usr/lib64/pkgconfig/samba-hostconfig.pc
/usr/lib64/pkgconfig/samba-policy.cpython-39-x86_64-linux-gnu.pc
/usr/lib64/pkgconfig/samba-util.pc
/usr/lib64/pkgconfig/samdb.pc
/usr/lib64/pkgconfig/smbclient.pc
/usr/lib64/pkgconfig/wbclient.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/krb5/plugins/kdb/samba.so
/usr/lib64/libdcerpc-binding.so.0
/usr/lib64/libdcerpc-binding.so.0.0.1
/usr/lib64/libdcerpc-samr.so.0
/usr/lib64/libdcerpc-samr.so.0.0.1
/usr/lib64/libdcerpc-server-core.so.0
/usr/lib64/libdcerpc-server-core.so.0.0.1
/usr/lib64/libdcerpc-server.so.0
/usr/lib64/libdcerpc-server.so.0.0.1
/usr/lib64/libdcerpc.so.0
/usr/lib64/libdcerpc.so.0.0.1
/usr/lib64/libndr-krb5pac.so.0
/usr/lib64/libndr-krb5pac.so.0.0.1
/usr/lib64/libndr-nbt.so.0
/usr/lib64/libndr-nbt.so.0.0.1
/usr/lib64/libndr-standard.so.0
/usr/lib64/libndr-standard.so.0.0.1
/usr/lib64/libndr.so.1
/usr/lib64/libndr.so.1.0.1
/usr/lib64/libnetapi.so.0
/usr/lib64/libnss_winbind.so.2
/usr/lib64/libnss_wins.so.2
/usr/lib64/libsamba-credentials.so.1
/usr/lib64/libsamba-credentials.so.1.0.0
/usr/lib64/libsamba-errors.so.1
/usr/lib64/libsamba-hostconfig.so.0
/usr/lib64/libsamba-hostconfig.so.0.0.1
/usr/lib64/libsamba-passdb.so.0
/usr/lib64/libsamba-passdb.so.0.28.0
/usr/lib64/libsamba-policy.cpython-39-x86-64-linux-gnu.so.0
/usr/lib64/libsamba-policy.cpython-39-x86-64-linux-gnu.so.0.0.1
/usr/lib64/libsamba-util.so.0
/usr/lib64/libsamba-util.so.0.0.1
/usr/lib64/libsamdb.so.0
/usr/lib64/libsamdb.so.0.0.1
/usr/lib64/libsmbclient.so.0
/usr/lib64/libsmbclient.so.0.7.0
/usr/lib64/libsmbconf.so.0
/usr/lib64/libsmbldap.so.2
/usr/lib64/libsmbldap.so.2.1.0
/usr/lib64/libtevent-util.so.0
/usr/lib64/libtevent-util.so.0.0.1
/usr/lib64/libwbclient.so.0
/usr/lib64/libwbclient.so.0.15
/usr/lib64/samba/bind9/dlz_bind9.so
/usr/lib64/samba/bind9/dlz_bind9_10.so
/usr/lib64/samba/bind9/dlz_bind9_11.so
/usr/lib64/samba/bind9/dlz_bind9_12.so
/usr/lib64/samba/bind9/dlz_bind9_14.so
/usr/lib64/samba/bind9/dlz_bind9_16.so
/usr/lib64/samba/bind9/dlz_bind9_9.so
/usr/lib64/samba/gensec/krb5.so
/usr/lib64/samba/idmap/ad.so
/usr/lib64/samba/idmap/autorid.so
/usr/lib64/samba/idmap/hash.so
/usr/lib64/samba/idmap/rfc2307.so
/usr/lib64/samba/idmap/rid.so
/usr/lib64/samba/idmap/script.so
/usr/lib64/samba/idmap/tdb2.so
/usr/lib64/samba/krb5/async_dns_krb5_locator.so
/usr/lib64/samba/krb5/winbind_krb5_localauth.so
/usr/lib64/samba/krb5/winbind_krb5_locator.so
/usr/lib64/samba/ldb/acl.so
/usr/lib64/samba/ldb/aclread.so
/usr/lib64/samba/ldb/anr.so
/usr/lib64/samba/ldb/audit_log.so
/usr/lib64/samba/ldb/count_attrs.so
/usr/lib64/samba/ldb/descriptor.so
/usr/lib64/samba/ldb/dirsync.so
/usr/lib64/samba/ldb/dns_notify.so
/usr/lib64/samba/ldb/dsdb_notification.so
/usr/lib64/samba/ldb/encrypted_secrets.so
/usr/lib64/samba/ldb/extended_dn_in.so
/usr/lib64/samba/ldb/extended_dn_out.so
/usr/lib64/samba/ldb/extended_dn_store.so
/usr/lib64/samba/ldb/group_audit_log.so
/usr/lib64/samba/ldb/ildap.so
/usr/lib64/samba/ldb/instancetype.so
/usr/lib64/samba/ldb/lazy_commit.so
/usr/lib64/samba/ldb/ldbsamba_extensions.so
/usr/lib64/samba/ldb/linked_attributes.so
/usr/lib64/samba/ldb/new_partition.so
/usr/lib64/samba/ldb/objectclass.so
/usr/lib64/samba/ldb/objectclass_attrs.so
/usr/lib64/samba/ldb/objectguid.so
/usr/lib64/samba/ldb/operational.so
/usr/lib64/samba/ldb/paged_results.so
/usr/lib64/samba/ldb/partition.so
/usr/lib64/samba/ldb/password_hash.so
/usr/lib64/samba/ldb/ranged_results.so
/usr/lib64/samba/ldb/repl_meta_data.so
/usr/lib64/samba/ldb/resolve_oids.so
/usr/lib64/samba/ldb/rootdse.so
/usr/lib64/samba/ldb/samba3sam.so
/usr/lib64/samba/ldb/samba3sid.so
/usr/lib64/samba/ldb/samba_dsdb.so
/usr/lib64/samba/ldb/samba_secrets.so
/usr/lib64/samba/ldb/samldb.so
/usr/lib64/samba/ldb/schema_data.so
/usr/lib64/samba/ldb/schema_load.so
/usr/lib64/samba/ldb/secrets_tdb_sync.so
/usr/lib64/samba/ldb/show_deleted.so
/usr/lib64/samba/ldb/subtree_delete.so
/usr/lib64/samba/ldb/subtree_rename.so
/usr/lib64/samba/ldb/tombstone_reanimate.so
/usr/lib64/samba/ldb/unique_object_sids.so
/usr/lib64/samba/ldb/update_keytab.so
/usr/lib64/samba/ldb/vlv.so
/usr/lib64/samba/ldb/wins_ldb.so
/usr/lib64/samba/libCHARSET3-samba4.so
/usr/lib64/samba/libLIBWBCLIENT-OLD-samba4.so
/usr/lib64/samba/libMESSAGING-SEND-samba4.so
/usr/lib64/samba/libMESSAGING-samba4.so
/usr/lib64/samba/libaddns-samba4.so
/usr/lib64/samba/libads-samba4.so
/usr/lib64/samba/libasn1util-samba4.so
/usr/lib64/samba/libauth-samba4.so
/usr/lib64/samba/libauth-unix-token-samba4.so
/usr/lib64/samba/libauth4-samba4.so
/usr/lib64/samba/libauthkrb5-samba4.so
/usr/lib64/samba/libcli-cldap-samba4.so
/usr/lib64/samba/libcli-ldap-common-samba4.so
/usr/lib64/samba/libcli-ldap-samba4.so
/usr/lib64/samba/libcli-nbt-samba4.so
/usr/lib64/samba/libcli-smb-common-samba4.so
/usr/lib64/samba/libcli-spoolss-samba4.so
/usr/lib64/samba/libcliauth-samba4.so
/usr/lib64/samba/libclidns-samba4.so
/usr/lib64/samba/libcluster-samba4.so
/usr/lib64/samba/libcmdline-contexts-samba4.so
/usr/lib64/samba/libcmdline-credentials-samba4.so
/usr/lib64/samba/libcmocka-samba4.so
/usr/lib64/samba/libcommon-auth-samba4.so
/usr/lib64/samba/libctdb-event-client-samba4.so
/usr/lib64/samba/libdb-glue-samba4.so
/usr/lib64/samba/libdbwrap-samba4.so
/usr/lib64/samba/libdcerpc-samba-samba4.so
/usr/lib64/samba/libdcerpc-samba4.so
/usr/lib64/samba/libdfs-server-ad-samba4.so
/usr/lib64/samba/libdlz-bind9-for-torture-samba4.so
/usr/lib64/samba/libdnsserver-common-samba4.so
/usr/lib64/samba/libdsdb-garbage-collect-tombstones-samba4.so
/usr/lib64/samba/libdsdb-module-samba4.so
/usr/lib64/samba/libevents-samba4.so
/usr/lib64/samba/libflag-mapping-samba4.so
/usr/lib64/samba/libgenrand-samba4.so
/usr/lib64/samba/libgensec-samba4.so
/usr/lib64/samba/libgpext-samba4.so
/usr/lib64/samba/libgpo-samba4.so
/usr/lib64/samba/libgse-samba4.so
/usr/lib64/samba/libhttp-samba4.so
/usr/lib64/samba/libidmap-samba4.so
/usr/lib64/samba/libinterfaces-samba4.so
/usr/lib64/samba/libiov-buf-samba4.so
/usr/lib64/samba/libkrb5samba-samba4.so
/usr/lib64/samba/libldbsamba-samba4.so
/usr/lib64/samba/liblibcli-lsa3-samba4.so
/usr/lib64/samba/liblibcli-netlogon3-samba4.so
/usr/lib64/samba/liblibsmb-samba4.so
/usr/lib64/samba/libmessages-dgm-samba4.so
/usr/lib64/samba/libmessages-util-samba4.so
/usr/lib64/samba/libmscat-samba4.so
/usr/lib64/samba/libmsghdr-samba4.so
/usr/lib64/samba/libmsrpc3-samba4.so
/usr/lib64/samba/libndr-samba-samba4.so
/usr/lib64/samba/libndr-samba4.so
/usr/lib64/samba/libnet-keytab-samba4.so
/usr/lib64/samba/libnetif-samba4.so
/usr/lib64/samba/libnpa-tstream-samba4.so
/usr/lib64/samba/libnss-info-samba4.so
/usr/lib64/samba/libpac-samba4.so
/usr/lib64/samba/libpopt-samba3-cmdline-samba4.so
/usr/lib64/samba/libpopt-samba3-samba4.so
/usr/lib64/samba/libposix-eadb-samba4.so
/usr/lib64/samba/libprinter-driver-samba4.so
/usr/lib64/samba/libprinting-migrate-samba4.so
/usr/lib64/samba/libprocess-model-samba4.so
/usr/lib64/samba/libregistry-samba4.so
/usr/lib64/samba/libreplace-samba4.so
/usr/lib64/samba/libsamba-cluster-support-samba4.so
/usr/lib64/samba/libsamba-debug-samba4.so
/usr/lib64/samba/libsamba-modules-samba4.so
/usr/lib64/samba/libsamba-net.cpython-39-x86-64-linux-gnu-samba4.so
/usr/lib64/samba/libsamba-python.cpython-39-x86-64-linux-gnu-samba4.so
/usr/lib64/samba/libsamba-security-samba4.so
/usr/lib64/samba/libsamba-sockets-samba4.so
/usr/lib64/samba/libsamba3-util-samba4.so
/usr/lib64/samba/libsamdb-common-samba4.so
/usr/lib64/samba/libscavenge-dns-records-samba4.so
/usr/lib64/samba/libsecrets3-samba4.so
/usr/lib64/samba/libserver-id-db-samba4.so
/usr/lib64/samba/libserver-role-samba4.so
/usr/lib64/samba/libservice-samba4.so
/usr/lib64/samba/libshares-samba4.so
/usr/lib64/samba/libsmb-transport-samba4.so
/usr/lib64/samba/libsmbclient-raw-samba4.so
/usr/lib64/samba/libsmbd-base-samba4.so
/usr/lib64/samba/libsmbd-shim-samba4.so
/usr/lib64/samba/libsmbldaphelper-samba4.so
/usr/lib64/samba/libsmbpasswdparser-samba4.so
/usr/lib64/samba/libsocket-blocking-samba4.so
/usr/lib64/samba/libsys-rw-samba4.so
/usr/lib64/samba/libtalloc-report-printf-samba4.so
/usr/lib64/samba/libtalloc-report-samba4.so
/usr/lib64/samba/libtdb-wrap-samba4.so
/usr/lib64/samba/libtime-basic-samba4.so
/usr/lib64/samba/libtorture-samba4.so
/usr/lib64/samba/libtrusts-util-samba4.so
/usr/lib64/samba/libutil-cmdline-samba4.so
/usr/lib64/samba/libutil-reg-samba4.so
/usr/lib64/samba/libutil-setid-samba4.so
/usr/lib64/samba/libutil-tdb-samba4.so
/usr/lib64/samba/libwinbind-client-samba4.so
/usr/lib64/samba/libxattr-tdb-samba4.so
/usr/lib64/samba/nss_info/hash.so
/usr/lib64/samba/nss_info/rfc2307.so
/usr/lib64/samba/nss_info/sfu.so
/usr/lib64/samba/nss_info/sfu20.so
/usr/lib64/samba/process_model/prefork.so
/usr/lib64/samba/process_model/standard.so
/usr/lib64/samba/service/cldap.so
/usr/lib64/samba/service/dcerpc.so
/usr/lib64/samba/service/dns.so
/usr/lib64/samba/service/dns_update.so
/usr/lib64/samba/service/drepl.so
/usr/lib64/samba/service/kcc.so
/usr/lib64/samba/service/kdc.so
/usr/lib64/samba/service/ldap.so
/usr/lib64/samba/service/nbtd.so
/usr/lib64/samba/service/ntp_signd.so
/usr/lib64/samba/service/s3fs.so
/usr/lib64/samba/service/winbindd.so
/usr/lib64/samba/service/wrepl.so
/usr/lib64/samba/vfs/acl_tdb.so
/usr/lib64/samba/vfs/acl_xattr.so
/usr/lib64/samba/vfs/aio_fork.so
/usr/lib64/samba/vfs/aio_pthread.so
/usr/lib64/samba/vfs/audit.so
/usr/lib64/samba/vfs/btrfs.so
/usr/lib64/samba/vfs/cap.so
/usr/lib64/samba/vfs/catia.so
/usr/lib64/samba/vfs/commit.so
/usr/lib64/samba/vfs/crossrename.so
/usr/lib64/samba/vfs/default_quota.so
/usr/lib64/samba/vfs/dirsort.so
/usr/lib64/samba/vfs/expand_msdfs.so
/usr/lib64/samba/vfs/extd_audit.so
/usr/lib64/samba/vfs/fake_perms.so
/usr/lib64/samba/vfs/fileid.so
/usr/lib64/samba/vfs/fruit.so
/usr/lib64/samba/vfs/full_audit.so
/usr/lib64/samba/vfs/glusterfs_fuse.so
/usr/lib64/samba/vfs/gpfs.so
/usr/lib64/samba/vfs/linux_xfs_sgid.so
/usr/lib64/samba/vfs/media_harmony.so
/usr/lib64/samba/vfs/offline.so
/usr/lib64/samba/vfs/posix_eadb.so
/usr/lib64/samba/vfs/preopen.so
/usr/lib64/samba/vfs/readahead.so
/usr/lib64/samba/vfs/readonly.so
/usr/lib64/samba/vfs/recycle.so
/usr/lib64/samba/vfs/shadow_copy.so
/usr/lib64/samba/vfs/shadow_copy2.so
/usr/lib64/samba/vfs/shell_snap.so
/usr/lib64/samba/vfs/snapper.so
/usr/lib64/samba/vfs/streams_depot.so
/usr/lib64/samba/vfs/streams_xattr.so
/usr/lib64/samba/vfs/syncops.so
/usr/lib64/samba/vfs/time_audit.so
/usr/lib64/samba/vfs/unityed_media.so
/usr/lib64/samba/vfs/virusfilter.so
/usr/lib64/samba/vfs/widelinks.so
/usr/lib64/samba/vfs/worm.so
/usr/lib64/samba/vfs/xattr_tdb.so
/usr/lib64/security/pam_winbind.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/ctdb/ctdb-config
/usr/libexec/ctdb/ctdb-event
/usr/libexec/ctdb/ctdb-eventd
/usr/libexec/ctdb/ctdb-path
/usr/libexec/ctdb/ctdb_killtcp
/usr/libexec/ctdb/ctdb_lock_helper
/usr/libexec/ctdb/ctdb_lvs
/usr/libexec/ctdb/ctdb_mutex_fcntl_helper
/usr/libexec/ctdb/ctdb_natgw
/usr/libexec/ctdb/ctdb_recovery_helper
/usr/libexec/ctdb/ctdb_takeover_helper
/usr/libexec/ctdb/smnotify
/usr/libexec/samba/smbspool_krb5_wrapper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/samba/2004537f8b8c3aee21a03133e1f4aaed6dc9a90c
/usr/share/package-licenses/samba/37984ab2838de7795cd108336e00844e490457cb
/usr/share/package-licenses/samba/41bb27089429d9d6febf18e4237cf04d81fcc737
/usr/share/package-licenses/samba/61bb7a8ea669080cfc9e7dbf37079eae70b535fb
/usr/share/package-licenses/samba/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/samba/8ea3090863330c454ba0f536177bc1a8ee5de1b0
/usr/share/package-licenses/samba/c75814379854cf0de2911449fca8c9138520f140

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/nmb.service
/usr/lib/systemd/system/samba.service
/usr/lib/systemd/system/smb.service
/usr/lib/systemd/system/winbind.service
