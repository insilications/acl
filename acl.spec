#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x41633B9FE837F581 (vapier@gentoo.org)
#
%define keepstatic 1
Name     : acl
Version  : 2.2.53
Release  : 38
URL      : https://download-mirror.savannah.gnu.org/releases/acl/acl-2.2.53.tar.gz
Source0  : https://download-mirror.savannah.gnu.org/releases/acl/acl-2.2.53.tar.gz
Source1  : https://download-mirror.savannah.gnu.org/releases/acl/acl-2.2.53.tar.gz.sig
Summary  : A library for POSIX Access Control Lists
Group    : Development/Tools
License  : GPL-2.0+
Requires: acl-bin = %{version}-%{release}
Requires: acl-lib = %{version}-%{release}
Requires: acl-locales = %{version}-%{release}
Requires: acl-man = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : attr-dev32
BuildRequires : buildreq-configure
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-acl-2.2.53-test-runwrapper.patch
Patch2: 0002-acl-2.2.53-setattr-segv.patch

%description
__________________________________
Package home: http://savannah.nongnu.org/projects/acl

%package bin
Summary: bin components for the acl package.
Group: Binaries

%description bin
bin components for the acl package.


%package dev
Summary: dev components for the acl package.
Group: Development
Requires: acl-lib = %{version}-%{release}
Requires: acl-bin = %{version}-%{release}
Provides: acl-devel = %{version}-%{release}
Requires: acl = %{version}-%{release}

%description dev
dev components for the acl package.


%package dev32
Summary: dev32 components for the acl package.
Group: Default
Requires: acl-lib32 = %{version}-%{release}
Requires: acl-bin = %{version}-%{release}
Requires: acl-dev = %{version}-%{release}

%description dev32
dev32 components for the acl package.


%package doc
Summary: doc components for the acl package.
Group: Documentation
Requires: acl-man = %{version}-%{release}

%description doc
doc components for the acl package.


%package lib
Summary: lib components for the acl package.
Group: Libraries

%description lib
lib components for the acl package.


%package lib32
Summary: lib32 components for the acl package.
Group: Default

%description lib32
lib32 components for the acl package.


%package locales
Summary: locales components for the acl package.
Group: Default

%description locales
locales components for the acl package.


%package man
Summary: man components for the acl package.
Group: Default

%description man
man components for the acl package.


%package staticdev
Summary: staticdev components for the acl package.
Group: Default
Requires: acl-dev = %{version}-%{release}

%description staticdev
staticdev components for the acl package.


%package staticdev32
Summary: staticdev32 components for the acl package.
Group: Default
Requires: acl-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the acl package.


%prep
%setup -q -n acl-2.2.53
cd %{_builddir}/acl-2.2.53
%patch1 -p1
%patch2 -p1
pushd ..
cp -a acl-2.2.53 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599707014
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%define _lto_cflags 1
#%define _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags_pgo end
##
%define _lto_cflags 1
##
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
 %configure --enable-nls --libexecdir=%{_libdir} --enable-static --enable-shared
make  %{?_smp_mflags}

make VERBOSE=1 V=1 %{?_smp_mflags} check || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%configure --enable-nls --libexecdir=%{_libdir} --enable-static --enable-shared
make  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="-g -O2 -fuse-linker-plugin -pipe"
export CXXFLAGS="-g -O2 -fuse-linker-plugin -fvisibility-inlines-hidden -pipe"
export LDFLAGS="-g -O2 -fuse-linker-plugin -pipe"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --enable-nls --libexecdir=%{_libdir} --enable-static --enable-shared  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1599707014
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang acl

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chacl
/usr/bin/getfacl
/usr/bin/setfacl

%files dev
%defattr(-,root,root,-)
/usr/include/acl/libacl.h
/usr/include/sys/acl.h
/usr/lib64/libacl.so
/usr/lib64/pkgconfig/libacl.pc
/usr/share/man/man3/acl_add_perm.3
/usr/share/man/man3/acl_calc_mask.3
/usr/share/man/man3/acl_check.3
/usr/share/man/man3/acl_clear_perms.3
/usr/share/man/man3/acl_cmp.3
/usr/share/man/man3/acl_copy_entry.3
/usr/share/man/man3/acl_copy_ext.3
/usr/share/man/man3/acl_copy_int.3
/usr/share/man/man3/acl_create_entry.3
/usr/share/man/man3/acl_delete_def_file.3
/usr/share/man/man3/acl_delete_entry.3
/usr/share/man/man3/acl_delete_perm.3
/usr/share/man/man3/acl_dup.3
/usr/share/man/man3/acl_entries.3
/usr/share/man/man3/acl_equiv_mode.3
/usr/share/man/man3/acl_error.3
/usr/share/man/man3/acl_extended_fd.3
/usr/share/man/man3/acl_extended_file.3
/usr/share/man/man3/acl_extended_file_nofollow.3
/usr/share/man/man3/acl_free.3
/usr/share/man/man3/acl_from_mode.3
/usr/share/man/man3/acl_from_text.3
/usr/share/man/man3/acl_get_entry.3
/usr/share/man/man3/acl_get_fd.3
/usr/share/man/man3/acl_get_file.3
/usr/share/man/man3/acl_get_perm.3
/usr/share/man/man3/acl_get_permset.3
/usr/share/man/man3/acl_get_qualifier.3
/usr/share/man/man3/acl_get_tag_type.3
/usr/share/man/man3/acl_init.3
/usr/share/man/man3/acl_set_fd.3
/usr/share/man/man3/acl_set_file.3
/usr/share/man/man3/acl_set_permset.3
/usr/share/man/man3/acl_set_qualifier.3
/usr/share/man/man3/acl_set_tag_type.3
/usr/share/man/man3/acl_size.3
/usr/share/man/man3/acl_to_any_text.3
/usr/share/man/man3/acl_to_text.3
/usr/share/man/man3/acl_valid.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libacl.so
/usr/lib32/pkgconfig/32libacl.pc
/usr/lib32/pkgconfig/libacl.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/acl/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libacl.so.1
/usr/lib64/libacl.so.1.1.2253

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libacl.so.1
/usr/lib32/libacl.so.1.1.2253

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/chacl.1
/usr/share/man/man1/getfacl.1
/usr/share/man/man1/setfacl.1
/usr/share/man/man5/acl.5

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libacl.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libacl.a

%files locales -f acl.lang
%defattr(-,root,root,-)

