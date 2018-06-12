#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-princurve
Version  : 2.0.2
Release  : 10
URL      : https://cran.r-project.org/src/contrib/princurve_2.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/princurve_2.0.2.tar.gz
Summary  : Fits a Principal Curve in Arbitrary Dimension
Group    : Development/Tools
License  : GPL-2.0
Requires: R-princurve-lib
BuildRequires : clr-R-helpers

%description
princurve
=========
[![Build
Status](https://travis-ci.org/dynverse/princurve.svg?branch=master)](https://travis-ci.org/dynverse/princurve)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/dynverse/princurve?branch=master&svg=true)](https://ci.appveyor.com/project/dynverse/princurve)
[![CRAN\_Status\_Badge](https://www.r-pkg.org/badges/version/princurve)](https://cran.r-project.org/package=princurve)
[![Coverage
Status](https://codecov.io/gh/dynverse/princurve/branch/master/graph/badge.svg)](https://codecov.io/gh/dynverse/princurve?branch=master)

%package lib
Summary: lib components for the R-princurve package.
Group: Libraries

%description lib
lib components for the R-princurve package.


%prep
%setup -q -c -n princurve

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528835522

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1528835522
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library princurve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library princurve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library princurve
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library princurve|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/princurve/DESCRIPTION
/usr/lib64/R/library/princurve/INDEX
/usr/lib64/R/library/princurve/Meta/Rd.rds
/usr/lib64/R/library/princurve/Meta/features.rds
/usr/lib64/R/library/princurve/Meta/hsearch.rds
/usr/lib64/R/library/princurve/Meta/links.rds
/usr/lib64/R/library/princurve/Meta/nsInfo.rds
/usr/lib64/R/library/princurve/Meta/package.rds
/usr/lib64/R/library/princurve/NAMESPACE
/usr/lib64/R/library/princurve/R/princurve
/usr/lib64/R/library/princurve/R/princurve.rdb
/usr/lib64/R/library/princurve/R/princurve.rdx
/usr/lib64/R/library/princurve/help/AnIndex
/usr/lib64/R/library/princurve/help/aliases.rds
/usr/lib64/R/library/princurve/help/figures/README_example_plot-1.png
/usr/lib64/R/library/princurve/help/paths.rds
/usr/lib64/R/library/princurve/help/princurve.rdb
/usr/lib64/R/library/princurve/help/princurve.rdx
/usr/lib64/R/library/princurve/html/00Index.html
/usr/lib64/R/library/princurve/html/R.css
/usr/lib64/R/library/princurve/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/princurve/libs/princurve.so
/usr/lib64/R/library/princurve/libs/princurve.so.avx2
/usr/lib64/R/library/princurve/libs/princurve.so.avx512
