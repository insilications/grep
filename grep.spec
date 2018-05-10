#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7FD9FCCB000BEEEE (meyering@fb.com)
#
Name     : grep
Version  : 3.1
Release  : 32
URL      : https://mirrors.kernel.org/gnu/grep/grep-3.1.tar.xz
Source0  : https://mirrors.kernel.org/gnu/grep/grep-3.1.tar.xz
Source99 : https://mirrors.kernel.org/gnu/grep/grep-3.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: grep-bin
Requires: grep-doc
Requires: grep-locales
BuildRequires : pcre-dev

%description
This is GNU grep, the "fastest grep in the west" (we hope).  All
bugs reported in previous releases have been fixed.  Many exciting new
bugs have probably been introduced in this revision.

%package bin
Summary: bin components for the grep package.
Group: Binaries

%description bin
bin components for the grep package.


%package doc
Summary: doc components for the grep package.
Group: Documentation

%description doc
doc components for the grep package.


%package locales
Summary: locales components for the grep package.
Group: Default

%description locales
locales components for the grep package.


%prep
%setup -q -n grep-3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520542008
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --with-packager="Clear Linux"
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1520542008
rm -rf %{buildroot}
%make_install
%find_lang grep
## make_install_append content
chmod +x ./tests/kwset-abuse
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/egrep
/usr/bin/fgrep
/usr/bin/grep

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files locales -f grep.lang
%defattr(-,root,root,-)

