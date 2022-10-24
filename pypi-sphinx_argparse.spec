#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinx_argparse
Version  : 0.3.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/66/f7/eb647af84adeaa2536acfe281cf37e20b4b5c5e3b34db3705e3f37b1a81f/sphinx-argparse-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/66/f7/eb647af84adeaa2536acfe281cf37e20b4b5c5e3b34db3705e3f37b1a81f/sphinx-argparse-0.3.2.tar.gz
Summary  : A sphinx extension that automatically documents argparse commands and options
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx_argparse-license = %{version}-%{release}
Requires: pypi-sphinx_argparse-python = %{version}-%{release}
Requires: pypi-sphinx_argparse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
[![Documentation Status](https://readthedocs.org/projects/sphinx-argparse/badge/?version=stable)](http://sphinx-argparse.readthedocs.org/)
[![PyPI version](https://badge.fury.io/py/sphinx-argparse.svg)](https://badge.fury.io/py/sphinx-argparse)
[![Install with conda](https://anaconda.org/conda-forge/sphinx-argparse/badges/installer/conda.svg)](https://github.com/conda-forge/sphinx-argparse-feedstock)
![Conda downloads](https://anaconda.org/conda-forge/sphinx-argparse/badges/downloads.svg)

%package license
Summary: license components for the pypi-sphinx_argparse package.
Group: Default

%description license
license components for the pypi-sphinx_argparse package.


%package python
Summary: python components for the pypi-sphinx_argparse package.
Group: Default
Requires: pypi-sphinx_argparse-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_argparse package.


%package python3
Summary: python3 components for the pypi-sphinx_argparse package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_argparse)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinx_argparse package.


%prep
%setup -q -n sphinx-argparse-0.3.2
cd %{_builddir}/sphinx-argparse-0.3.2
pushd ..
cp -a sphinx-argparse-0.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664807827
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_argparse
cp %{_builddir}/sphinx-argparse-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_argparse/67de873c1e71bb7719e25d2209dc44bdfc755db4 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_argparse/67de873c1e71bb7719e25d2209dc44bdfc755db4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
