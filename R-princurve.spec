#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-princurve
Version  : 2.1.6
Release  : 50
URL      : https://cran.r-project.org/src/contrib/princurve_2.1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/princurve_2.1.6.tar.gz
Summary  : Fit a Principal Curve in Arbitrary Dimension
Group    : Development/Tools
License  : GPL-2.0
Requires: R-princurve-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
# princurve
[![CRAN
Status](https://www.r-pkg.org/badges/version/princurve)](https://cran.r-project.org/package=princurve)
[![CRAN
Downloads](https://cranlogs.r-pkg.org/badges/princurve)](https://cran.r-project.org/package=princurve)
[![DOI](https://zenodo.org/badge/125849601.svg)](https://zenodo.org/badge/latestdoi/125849601)
[![R-CMD-check](https://github.com/rcannood/princurve/workflows/R-CMD-check/badge.svg)](https://github.com/rcannood/princurve/actions?query=workflow%3AR-CMD-check)
[![Coverage
Status](https://codecov.io/gh/rcannood/princurve/branch/master/graph/badge.svg)](https://codecov.io/gh/rcannood/princurve?branch=master)

%package lib
Summary: lib components for the R-princurve package.
Group: Libraries

%description lib
lib components for the R-princurve package.


%prep
%setup -q -c -n princurve
cd %{_builddir}/princurve

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610999545

%install
export SOURCE_DATE_EPOCH=1610999545
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library princurve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library princurve
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc princurve || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/princurve/CITATION
/usr/lib64/R/library/princurve/DESCRIPTION
/usr/lib64/R/library/princurve/INDEX
/usr/lib64/R/library/princurve/Meta/Rd.rds
/usr/lib64/R/library/princurve/Meta/features.rds
/usr/lib64/R/library/princurve/Meta/hsearch.rds
/usr/lib64/R/library/princurve/Meta/links.rds
/usr/lib64/R/library/princurve/Meta/nsInfo.rds
/usr/lib64/R/library/princurve/Meta/package.rds
/usr/lib64/R/library/princurve/NAMESPACE
/usr/lib64/R/library/princurve/NEWS.md
/usr/lib64/R/library/princurve/R/princurve
/usr/lib64/R/library/princurve/R/princurve.rdb
/usr/lib64/R/library/princurve/R/princurve.rdx
/usr/lib64/R/library/princurve/help/AnIndex
/usr/lib64/R/library/princurve/help/aliases.rds
/usr/lib64/R/library/princurve/help/figures/README_example-1.png
/usr/lib64/R/library/princurve/help/figures/README_princurve-1.png
/usr/lib64/R/library/princurve/help/paths.rds
/usr/lib64/R/library/princurve/help/princurve.rdb
/usr/lib64/R/library/princurve/help/princurve.rdx
/usr/lib64/R/library/princurve/html/00Index.html
/usr/lib64/R/library/princurve/html/R.css
/usr/lib64/R/library/princurve/tests/testthat.R
/usr/lib64/R/library/princurve/tests/testthat/test-deprecated.R
/usr/lib64/R/library/princurve/tests/testthat/test-legacy_princurve.R
/usr/lib64/R/library/princurve/tests/testthat/test-principal_curve.R
/usr/lib64/R/library/princurve/tests/testthat/test-project_to_curve.R
/usr/lib64/R/library/princurve/tests/testthat/test-smoother_functions.R
/usr/lib64/R/library/princurve/tests/testthat/test-start_circle.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/princurve/libs/princurve.so
/usr/lib64/R/library/princurve/libs/princurve.so.avx2
/usr/lib64/R/library/princurve/libs/princurve.so.avx512
