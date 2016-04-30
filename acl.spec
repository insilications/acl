Name:           acl
Version:        2.2.52
Release:        25
License:        LGPL-2.1+ GPL-2.0+
Summary:        Utilities for managing POSIX Access Control Lists
Url:            http://savannah.nongnu.org/projects/acl/
Group:          libs
Source0:        http://savannah.spinellicreations.com/acl/acl-2.2.52.src.tar.gz
Patch0:         e98ce8acf84d12ea67a3ac76bf63c6d87d9af86d.patch
BuildRequires:  attr-dev gettext

%description
Utilities for managing POSIX Access Control Lists.

%package lib
License:        LGPL-2.1+
Summary:        Utilities for managing POSIX Access Control Lists
Group:          libs

%description lib
Utilities for managing POSIX Access Control Lists.

%package dev
Summary:        Utilities for managing POSIX Access Control Lists
Group:          libs
Requires:       acl-lib

%description dev
Utilities for managing POSIX Access Control Lists.


%package doc
Summary:        Utilities for managing POSIX Access Control Lists
Group:          doc

%description doc
Utilities for managing POSIX Access Control Lists.

%package locale
Summary:        Utilities for managing POSIX Access Control Lists
Group:          libs

%description locale
Utilities for managing POSIX Access Control Lists.

%prep
%setup -q
%patch0 -p1

%build
%configure \
 --enable-nls \
 --libexecdir=%{_libdir} \
 --disable-static \
 --enable-shared

make %{?_smp_mflags}

%install
%make_install install-lib install-dev DIST_ROOT=%{buildroot} DESTDIR=%{buildroot}

# library must have executable bits set for rpm4 ELF provides to work correctly
chmod 0755 %{buildroot}/%{_libdir}/libacl.so.*

%find_lang %{name}

%check
make -k %{?_smp_mflags} tests

%files
%{_bindir}/setfacl
%{_bindir}/chacl
%{_bindir}/getfacl

%files lib
%{_libdir}/libacl.so.*

%files dev
%{_includedir}/sys/acl.h
%{_includedir}/acl/libacl.h
%{_libdir}/libacl.so


%files doc
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_datadir}/doc/acl/*

%files locale -f %{name}.lang
