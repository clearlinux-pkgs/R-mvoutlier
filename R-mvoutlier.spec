#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mvoutlier
Version  : 2.0.9
Release  : 28
URL      : https://cran.r-project.org/src/contrib/mvoutlier_2.0.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mvoutlier_2.0.9.tar.gz
Summary  : Multivariate Outlier Detection Based on Robust Methods
Group    : Development/Tools
License  : GPL-3.0
Requires: R-robCompositions
Requires: R-robustbase
Requires: R-sgeostat
BuildRequires : R-robCompositions
BuildRequires : R-robustbase
BuildRequires : R-sgeostat
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n mvoutlier
cd %{_builddir}/mvoutlier

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589788171

%install
export SOURCE_DATE_EPOCH=1589788171
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvoutlier
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvoutlier
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvoutlier
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mvoutlier/DESCRIPTION
/usr/lib64/R/library/mvoutlier/INDEX
/usr/lib64/R/library/mvoutlier/Meta/Rd.rds
/usr/lib64/R/library/mvoutlier/Meta/data.rds
/usr/lib64/R/library/mvoutlier/Meta/features.rds
/usr/lib64/R/library/mvoutlier/Meta/hsearch.rds
/usr/lib64/R/library/mvoutlier/Meta/links.rds
/usr/lib64/R/library/mvoutlier/Meta/nsInfo.rds
/usr/lib64/R/library/mvoutlier/Meta/package.rds
/usr/lib64/R/library/mvoutlier/NAMESPACE
/usr/lib64/R/library/mvoutlier/R/mvoutlier
/usr/lib64/R/library/mvoutlier/R/mvoutlier.rdb
/usr/lib64/R/library/mvoutlier/R/mvoutlier.rdx
/usr/lib64/R/library/mvoutlier/data/Rdata.rdb
/usr/lib64/R/library/mvoutlier/data/Rdata.rds
/usr/lib64/R/library/mvoutlier/data/Rdata.rdx
/usr/lib64/R/library/mvoutlier/help/AnIndex
/usr/lib64/R/library/mvoutlier/help/aliases.rds
/usr/lib64/R/library/mvoutlier/help/mvoutlier.rdb
/usr/lib64/R/library/mvoutlier/help/mvoutlier.rdx
/usr/lib64/R/library/mvoutlier/help/paths.rds
/usr/lib64/R/library/mvoutlier/html/00Index.html
/usr/lib64/R/library/mvoutlier/html/R.css
