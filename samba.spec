#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : samba
Version  : 4.7.9
Release  : 62
URL      : https://github.com/samba-team/samba/archive/samba-4.7.9.tar.gz
Source0  : https://github.com/samba-team/samba/archive/samba-4.7.9.tar.gz
Source1  : samba.tmpfiles
Summary  : Generate parsers / DCE/RPC-clients from IDL
Group    : Development/Tools
License  : BSL-1.0 EPL-1.0 GPL-3.0 HPND ISC MIT Public-Domain X11
Requires: samba-bin = %{version}-%{release}
Requires: samba-config = %{version}-%{release}
Requires: samba-data = %{version}-%{release}
Requires: samba-lib = %{version}-%{release}
Requires: samba-libexec = %{version}-%{release}
Requires: samba-license = %{version}-%{release}
Requires: samba-man = %{version}-%{release}
Requires: samba-python = %{version}-%{release}
Requires: samba-services = %{version}-%{release}
BuildRequires : LVM2-dev
BuildRequires : Linux-PAM-dev
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-qmake
BuildRequires : cups-dev
BuildRequires : dbus-dev
BuildRequires : e2fsprogs-dev
BuildRequires : fuse-dev
BuildRequires : gdb
BuildRequires : gmp-dev
BuildRequires : gnutls-dev
BuildRequires : gpgme-dev
BuildRequires : intltool-dev
BuildRequires : iso8601
BuildRequires : krb5-dev
BuildRequires : ldb-dev
BuildRequires : libaio-dev
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libgpg-error-dev
BuildRequires : libunwind-dev
BuildRequires : ncurses-dev
BuildRequires : openldap-dev
BuildRequires : openssl-dev
BuildRequires : popt-dev
BuildRequires : python-dev
BuildRequires : readline-dev
BuildRequires : systemd-dev
BuildRequires : talloc-dev
BuildRequires : tdb-dev
BuildRequires : tdb-legacypython
BuildRequires : zlib-dev
Patch1: 0001-add-mock-disable-static-option.patch
Patch2: timestamps.patch
Patch3: 0002-Force-build-using-python2.patch

%description
This is the release version of Samba, the free SMB and CIFS client and
server and Domain Controller for UNIX and other operating
systems. Samba is maintained by the Samba Team, who support the
original author, Andrew Tridgell.

%package bin
Summary: bin components for the samba package.
Group: Binaries
Requires: samba-data = %{version}-%{release}
Requires: samba-libexec = %{version}-%{release}
Requires: samba-config = %{version}-%{release}
Requires: samba-license = %{version}-%{release}
Requires: samba-man = %{version}-%{release}
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

%description dev
dev components for the samba package.


%package extras
Summary: extras components for the samba package.
Group: Default

%description extras
extras components for the samba package.


%package legacypython
Summary: legacypython components for the samba package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the samba package.


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


%package man
Summary: man components for the samba package.
Group: Default

%description man
man components for the samba package.


%package python
Summary: python components for the samba package.
Group: Default

%description python
python components for the samba package.


%package services
Summary: services components for the samba package.
Group: Systemd services

%description services
services components for the samba package.


%prep
%setup -q -n samba-samba-4.7.9
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541178270
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --with-systemd --enable-fhs --with-system-mitkrb5 --nopyc --nopyo
make  %{?_smp_mflags} PYTHON=python2

%install
export SOURCE_DATE_EPOCH=1541178270
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/samba
cp COPYING %{buildroot}/usr/share/package-licenses/samba/COPYING
cp ctdb/COPYING %{buildroot}/usr/share/package-licenses/samba/ctdb_COPYING
cp examples/pcap2nbench/COPYING %{buildroot}/usr/share/package-licenses/samba/examples_pcap2nbench_COPYING
cp third_party/dnspython/LICENSE %{buildroot}/usr/share/package-licenses/samba/third_party_dnspython_LICENSE
cp third_party/dnspython/util/COPYRIGHT %{buildroot}/usr/share/package-licenses/samba/third_party_dnspython_util_COPYRIGHT
cp third_party/pep8/LICENSE %{buildroot}/usr/share/package-licenses/samba/third_party_pep8_LICENSE
cp third_party/popt/COPYING %{buildroot}/usr/share/package-licenses/samba/third_party_popt_COPYING
cp third_party/pyiso8601/LICENSE %{buildroot}/usr/share/package-licenses/samba/third_party_pyiso8601_LICENSE
cp third_party/zlib/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/samba/third_party_zlib_contrib_dotzlib_LICENSE_1_0.txt
%make_install PYTHON=python2
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/samba.conf
## install_append content
install -d -m 755 %{buildroot}/usr/lib/systemd/system
install -m 644 ./packaging/systemd/*.service %{buildroot}/usr/lib/systemd/system
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/CUtil.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Compat.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Dump.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Expr.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/IDL.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/NDR.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/ODL.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba3/ClientNDR.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba3/ServerNDR.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/COM/Header.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/COM/Proxy.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/COM/Stub.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/Header.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/NDR/Client.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/NDR/Parser.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/NDR/Server.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/Python.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/TDR.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Samba4/Template.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Typelist.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Util.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Wireshark/Conformance.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Pidl/Wireshark/NDR.pm
/usr/lib/perl5/vendor_perl/5.26.1/Parse/Yapp/Driver.pm

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/ldbadd
%exclude /usr/bin/ldbdel
%exclude /usr/bin/ldbedit
%exclude /usr/bin/ldbmodify
%exclude /usr/bin/ldbrename
%exclude /usr/bin/ldbsearch
/usr/bin/cifsdd
/usr/bin/dbwrap_tool
/usr/bin/eventlogadm
/usr/bin/findsmb
/usr/bin/gentest
/usr/bin/locktest
/usr/bin/masktest
/usr/bin/mvxattr
/usr/bin/ndrdump
/usr/bin/net
/usr/bin/nmbd
/usr/bin/nmblookup
/usr/bin/ntlm_auth
/usr/bin/oLschema2ldif
/usr/bin/pdbedit
/usr/bin/pidl
/usr/bin/profiles
/usr/bin/regdiff
/usr/bin/regpatch
/usr/bin/regshell
/usr/bin/regtree
/usr/bin/rpcclient
/usr/bin/samba
/usr/bin/samba-regedit
/usr/bin/samba-tool
/usr/bin/samba_dnsupdate
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
/usr/share/samba/setup/DB_CONFIG
/usr/share/samba/setup/ad-schema/MS-AD_Schema_2K8_Attributes.txt
/usr/share/samba/setup/ad-schema/MS-AD_Schema_2K8_Classes.txt
/usr/share/samba/setup/ad-schema/MS-AD_Schema_2K8_R2_Attributes.txt
/usr/share/samba/setup/ad-schema/MS-AD_Schema_2K8_R2_Classes.txt
/usr/share/samba/setup/ad-schema/licence.txt
/usr/share/samba/setup/aggregate_schema.ldif
/usr/share/samba/setup/cn=samba.ldif
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k0.txt
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k3.txt
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k3R2.txt
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k8.txt
/usr/share/samba/setup/display-specifiers/DisplaySpecifiers-Win2k8R2.txt
/usr/share/samba/setup/dns_update_list
/usr/share/samba/setup/fedora-ds-init.ldif
/usr/share/samba/setup/fedorads-dna.ldif
/usr/share/samba/setup/fedorads-index.ldif
/usr/share/samba/setup/fedorads-linked-attributes.ldif
/usr/share/samba/setup/fedorads-pam.ldif
/usr/share/samba/setup/fedorads-partitions.ldif
/usr/share/samba/setup/fedorads-refint-add.ldif
/usr/share/samba/setup/fedorads-refint-delete.ldif
/usr/share/samba/setup/fedorads-samba.ldif
/usr/share/samba/setup/fedorads-sasl.ldif
/usr/share/samba/setup/fedorads.inf
/usr/share/samba/setup/idmap_init.ldif
/usr/share/samba/setup/krb5.conf
/usr/share/samba/setup/memberof.conf
/usr/share/samba/setup/mmr_serverids.conf
/usr/share/samba/setup/mmr_syncrepl.conf
/usr/share/samba/setup/modules.conf
/usr/share/samba/setup/named.conf
/usr/share/samba/setup/named.conf.dlz
/usr/share/samba/setup/named.conf.update
/usr/share/samba/setup/named.txt
/usr/share/samba/setup/olc_mmr.conf
/usr/share/samba/setup/olc_seed.ldif
/usr/share/samba/setup/olc_serverid.conf
/usr/share/samba/setup/olc_syncrepl.conf
/usr/share/samba/setup/olc_syncrepl_seed.conf
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
/usr/share/samba/setup/provision_users.ldif
/usr/share/samba/setup/provision_users_add.ldif
/usr/share/samba/setup/provision_users_modify.ldif
/usr/share/samba/setup/provision_well_known_sec_princ.ldif
/usr/share/samba/setup/refint.conf
/usr/share/samba/setup/schema-map-fedora-ds-1.0
/usr/share/samba/setup/schema-map-openldap-2.3
/usr/share/samba/setup/schema_samba4.ldif
/usr/share/samba/setup/secrets.ldif
/usr/share/samba/setup/secrets_dns.ldif
/usr/share/samba/setup/secrets_init.ldif
/usr/share/samba/setup/secrets_sasl_ldap.ldif
/usr/share/samba/setup/secrets_simple_ldap.ldif
/usr/share/samba/setup/share.ldif
/usr/share/samba/setup/slapd.conf
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
/usr/include/samba-4.0/util/byteorder.h
/usr/include/samba-4.0/util/data_blob.h
/usr/include/samba-4.0/util/debug.h
/usr/include/samba-4.0/util/fault.h
/usr/include/samba-4.0/util/genrand.h
/usr/include/samba-4.0/util/idtree.h
/usr/include/samba-4.0/util/idtree_random.h
/usr/include/samba-4.0/util/memory.h
/usr/include/samba-4.0/util/safe_string.h
/usr/include/samba-4.0/util/signal.h
/usr/include/samba-4.0/util/string_wrappers.h
/usr/include/samba-4.0/util/substitute.h
/usr/include/samba-4.0/util/talloc_stack.h
/usr/include/samba-4.0/util/tevent_ntstatus.h
/usr/include/samba-4.0/util/tevent_unix.h
/usr/include/samba-4.0/util/tevent_werror.h
/usr/include/samba-4.0/util/tfork.h
/usr/include/samba-4.0/util/time.h
/usr/include/samba-4.0/util_ldb.h
/usr/include/samba-4.0/wbclient.h
/usr/lib64/libdcerpc-binding.so
/usr/lib64/libdcerpc-samr.so
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
/usr/lib64/libsamba-policy.so
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
/usr/lib64/pkgconfig/samba-policy.pc
/usr/lib64/pkgconfig/samba-util.pc
/usr/lib64/pkgconfig/samdb.pc
/usr/lib64/pkgconfig/smbclient.pc
/usr/lib64/pkgconfig/wbclient.pc
/usr/lib64/winbind_krb5_locator.so
/usr/share/man/man3/Parse::Pidl::Dump.3
/usr/share/man/man3/Parse::Pidl::NDR.3
/usr/share/man/man3/Parse::Pidl::Util.3
/usr/share/man/man3/Parse::Pidl::Wireshark::Conformance.3
/usr/share/man/man3/Parse::Pidl::Wireshark::NDR.3

%files extras
%defattr(-,root,root,-)
/usr/lib64/samba/libsamba-python-samba4.so

%files legacypython
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/_tdb_text.py
%exclude /usr/lib/python2.7/site-packages/tdb.so
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/samba/libsamba-python-samba4.so
/usr/lib64/krb5/plugins/kdb/samba.so
/usr/lib64/libdcerpc-binding.so.0
/usr/lib64/libdcerpc-binding.so.0.0.1
/usr/lib64/libdcerpc-samr.so.0
/usr/lib64/libdcerpc-samr.so.0.0.1
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
/usr/lib64/libndr.so.0
/usr/lib64/libndr.so.0.1.0
/usr/lib64/libnetapi.so.0
/usr/lib64/libnss_winbind.so.2
/usr/lib64/libnss_wins.so.2
/usr/lib64/libsamba-credentials.so.0
/usr/lib64/libsamba-credentials.so.0.0.1
/usr/lib64/libsamba-errors.so.1
/usr/lib64/libsamba-hostconfig.so.0
/usr/lib64/libsamba-hostconfig.so.0.0.1
/usr/lib64/libsamba-passdb.so.0
/usr/lib64/libsamba-passdb.so.0.27.0
/usr/lib64/libsamba-policy.so.0
/usr/lib64/libsamba-policy.so.0.0.1
/usr/lib64/libsamba-util.so.0
/usr/lib64/libsamba-util.so.0.0.1
/usr/lib64/libsamdb.so.0
/usr/lib64/libsamdb.so.0.0.1
/usr/lib64/libsmbclient.so.0
/usr/lib64/libsmbclient.so.0.2.3
/usr/lib64/libsmbconf.so.0
/usr/lib64/libsmbldap.so.2
/usr/lib64/libtevent-util.so.0
/usr/lib64/libtevent-util.so.0.0.1
/usr/lib64/libwbclient.so.0
/usr/lib64/libwbclient.so.0.14
/usr/lib64/samba/auth/script.so
/usr/lib64/samba/bind9/dlz_bind9.so
/usr/lib64/samba/bind9/dlz_bind9_10.so
/usr/lib64/samba/bind9/dlz_bind9_11.so
/usr/lib64/samba/bind9/dlz_bind9_9.so
/usr/lib64/samba/gensec/krb5.so
/usr/lib64/samba/idmap/ad.so
/usr/lib64/samba/idmap/autorid.so
/usr/lib64/samba/idmap/hash.so
/usr/lib64/samba/idmap/rfc2307.so
/usr/lib64/samba/idmap/rid.so
/usr/lib64/samba/idmap/script.so
/usr/lib64/samba/idmap/tdb2.so
/usr/lib64/samba/ldb/acl.so
/usr/lib64/samba/ldb/aclread.so
/usr/lib64/samba/ldb/anr.so
/usr/lib64/samba/ldb/asq.so
/usr/lib64/samba/ldb/descriptor.so
/usr/lib64/samba/ldb/dirsync.so
/usr/lib64/samba/ldb/dns_notify.so
/usr/lib64/samba/ldb/dsdb_notification.so
/usr/lib64/samba/ldb/extended_dn_in.so
/usr/lib64/samba/ldb/extended_dn_out.so
/usr/lib64/samba/ldb/extended_dn_store.so
/usr/lib64/samba/ldb/ildap.so
/usr/lib64/samba/ldb/instancetype.so
/usr/lib64/samba/ldb/lazy_commit.so
/usr/lib64/samba/ldb/ldbsamba_extensions.so
/usr/lib64/samba/ldb/linked_attributes.so
/usr/lib64/samba/ldb/local_password.so
/usr/lib64/samba/ldb/new_partition.so
/usr/lib64/samba/ldb/objectclass.so
/usr/lib64/samba/ldb/objectclass_attrs.so
/usr/lib64/samba/ldb/objectguid.so
/usr/lib64/samba/ldb/operational.so
/usr/lib64/samba/ldb/paged_results.so
/usr/lib64/samba/ldb/paged_searches.so
/usr/lib64/samba/ldb/partition.so
/usr/lib64/samba/ldb/password_hash.so
/usr/lib64/samba/ldb/ranged_results.so
/usr/lib64/samba/ldb/rdn_name.so
/usr/lib64/samba/ldb/repl_meta_data.so
/usr/lib64/samba/ldb/resolve_oids.so
/usr/lib64/samba/ldb/rootdse.so
/usr/lib64/samba/ldb/samba3sam.so
/usr/lib64/samba/ldb/samba3sid.so
/usr/lib64/samba/ldb/samba_dsdb.so
/usr/lib64/samba/ldb/samba_secrets.so
/usr/lib64/samba/ldb/samldb.so
/usr/lib64/samba/ldb/sample.so
/usr/lib64/samba/ldb/schema_data.so
/usr/lib64/samba/ldb/schema_load.so
/usr/lib64/samba/ldb/secrets_tdb_sync.so
/usr/lib64/samba/ldb/server_sort.so
/usr/lib64/samba/ldb/show_deleted.so
/usr/lib64/samba/ldb/simple_dn.so
/usr/lib64/samba/ldb/simple_ldap_map.so
/usr/lib64/samba/ldb/skel.so
/usr/lib64/samba/ldb/subtree_delete.so
/usr/lib64/samba/ldb/subtree_rename.so
/usr/lib64/samba/ldb/tdb.so
/usr/lib64/samba/ldb/tombstone_reanimate.so
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
/usr/lib64/samba/libcluster-samba4.so
/usr/lib64/samba/libcmdline-credentials-samba4.so
/usr/lib64/samba/libcmocka-samba4.so
/usr/lib64/samba/libcommon-auth-samba4.so
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
/usr/lib64/samba/libgpo-samba4.so
/usr/lib64/samba/libgse-samba4.so
/usr/lib64/samba/libhttp-samba4.so
/usr/lib64/samba/libidmap-samba4.so
/usr/lib64/samba/libinterfaces-samba4.so
/usr/lib64/samba/libiov-buf-samba4.so
/usr/lib64/samba/libkrb5samba-samba4.so
/usr/lib64/samba/libldb-cmdline-samba4.so
/usr/lib64/samba/libldb.so.1
/usr/lib64/samba/libldb.so.1.2.3
/usr/lib64/samba/libldbsamba-samba4.so
/usr/lib64/samba/liblibcli-lsa3-samba4.so
/usr/lib64/samba/liblibcli-netlogon3-samba4.so
/usr/lib64/samba/liblibsmb-samba4.so
/usr/lib64/samba/libmessages-dgm-samba4.so
/usr/lib64/samba/libmessages-util-samba4.so
/usr/lib64/samba/libmsghdr-samba4.so
/usr/lib64/samba/libmsrpc3-samba4.so
/usr/lib64/samba/libndr-samba-samba4.so
/usr/lib64/samba/libndr-samba4.so
/usr/lib64/samba/libnet-keytab-samba4.so
/usr/lib64/samba/libnetif-samba4.so
/usr/lib64/samba/libnon-posix-acls-samba4.so
/usr/lib64/samba/libnpa-tstream-samba4.so
/usr/lib64/samba/libnss-info-samba4.so
/usr/lib64/samba/libpac-samba4.so
/usr/lib64/samba/libpopt-samba3-samba4.so
/usr/lib64/samba/libposix-eadb-samba4.so
/usr/lib64/samba/libprinting-migrate-samba4.so
/usr/lib64/samba/libprocess-model-samba4.so
/usr/lib64/samba/libpyldb-util.so.1
/usr/lib64/samba/libpyldb-util.so.1.2.3
/usr/lib64/samba/libregistry-samba4.so
/usr/lib64/samba/libreplace-samba4.so
/usr/lib64/samba/libsamba-cluster-support-samba4.so
/usr/lib64/samba/libsamba-debug-samba4.so
/usr/lib64/samba/libsamba-modules-samba4.so
/usr/lib64/samba/libsamba-net-samba4.so
/usr/lib64/samba/libsamba-security-samba4.so
/usr/lib64/samba/libsamba-sockets-samba4.so
/usr/lib64/samba/libsamba3-util-samba4.so
/usr/lib64/samba/libsamdb-common-samba4.so
/usr/lib64/samba/libsecrets3-samba4.so
/usr/lib64/samba/libserver-id-db-samba4.so
/usr/lib64/samba/libserver-role-samba4.so
/usr/lib64/samba/libservice-samba4.so
/usr/lib64/samba/libshares-samba4.so
/usr/lib64/samba/libsmb-transport-samba4.so
/usr/lib64/samba/libsmbclient-raw-samba4.so
/usr/lib64/samba/libsmbd-base-samba4.so
/usr/lib64/samba/libsmbd-conn-samba4.so
/usr/lib64/samba/libsmbd-shim-samba4.so
/usr/lib64/samba/libsmbldaphelper-samba4.so
/usr/lib64/samba/libsmbpasswdparser-samba4.so
/usr/lib64/samba/libsocket-blocking-samba4.so
/usr/lib64/samba/libsys-rw-samba4.so
/usr/lib64/samba/libtalloc-report-samba4.so
/usr/lib64/samba/libtdb-wrap-samba4.so
/usr/lib64/samba/libtevent.so.0
/usr/lib64/samba/libtevent.so.0.9.36
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
/usr/lib64/samba/service/web.so
/usr/lib64/samba/service/winbindd.so
/usr/lib64/samba/service/wrepl.so
/usr/lib64/samba/vfs/acl_tdb.so
/usr/lib64/samba/vfs/acl_xattr.so
/usr/lib64/samba/vfs/aio_fork.so
/usr/lib64/samba/vfs/aio_linux.so
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
/usr/lib64/samba/vfs/linux_xfs_sgid.so
/usr/lib64/samba/vfs/media_harmony.so
/usr/lib64/samba/vfs/netatalk.so
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
/usr/lib64/samba/vfs/worm.so
/usr/lib64/samba/vfs/xattr_tdb.so
/usr/lib64/security/pam_winbind.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/samba/smbspool_krb5_wrapper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/samba/COPYING
/usr/share/package-licenses/samba/ctdb_COPYING
/usr/share/package-licenses/samba/examples_pcap2nbench_COPYING
/usr/share/package-licenses/samba/third_party_dnspython_LICENSE
/usr/share/package-licenses/samba/third_party_dnspython_util_COPYRIGHT
/usr/share/package-licenses/samba/third_party_pep8_LICENSE
/usr/share/package-licenses/samba/third_party_popt_COPYING
/usr/share/package-licenses/samba/third_party_pyiso8601_LICENSE
/usr/share/package-licenses/samba/third_party_zlib_contrib_dotzlib_LICENSE_1_0.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pidl.1

%files python
%defattr(-,root,root,-)

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/nmb.service
/usr/lib/systemd/system/samba.service
/usr/lib/systemd/system/smb.service
/usr/lib/systemd/system/winbind.service
