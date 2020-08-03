# install procedure for r4.0 in linux

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9

## R base
https://rtask.thinkr.fr/installation-of-r-3-5-on-ubuntu-18-04-lts-and-tips-for-spatial-packages/
```
sudo apt purge r-base* r-recommended r-cran-*
sudo apt autoremove
sudo apt update

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo apt update
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
sudo apt install r-base r-base-core r-recommended
```

## rstan
https://github.com/stan-dev/rstan/wiki/Installing-RStan-on-Linux

Note: **4.0** seems too early
https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-18-04-quickstart

## Bulk install (re-install) of packages
```
pkgs <- installed.packages()
ii <- is.na(pkgs[, "Priority"])
pkgs <- pkgs[ii, 1]
install.packages(pkgs)
```

## package libcurl was not found (pkg-config)
- `libcurl` is not an R package, but a linux package!
```
sudo apt-get install libcurl4-openssl-dev libssl libxml2-dev libgdal-dev
```
After this, perform in `R`
```
install.package('curl')
install.package('V8')
```

## Install RStan from source
- after `r-cran-v8` errors unsolved, I installed it this way
```
install.packages("rstan", type = "source")
```
- tested the examples at the following site and worked.
- Details are in [Installing RStan on Linux](https://github.com/stan-dev/rstan/wiki/Installing-RStan-on-Linux).


# Windows 10 install for R-4.0.2
1. remove previous installation `remove/install programs`
1. Download and install `R-4.0.2-win.exe`
1. Download and install `RStudio-1.3.1056.exe`
1. open `RStudio`
1. `pkgbuild::has_build_tools(debug = TRUE)`
  - click 'Yes' if asked to install tools, which installs 'RTools' in C:.
1. Configuration of C++ toolchain (https://github.com/stan-dev/rstan/wiki/RStan-Getting-Started)
```
dotR <- file.path(Sys.getenv("HOME"), ".R")
if (!file.exists(dotR)) dir.create(dotR)
M <- file.path(dotR, ifelse(.Platform$OS.type == "windows", "Makevars.win", "Makevars"))
if (!file.exists(M)) file.create(M)
cat("\nCXX14FLAGS=-O3 -march=native -mtune=native",
    if( grepl("^darwin", R.version$os)) "CXX14FLAGS += -arch x86_64 -ftemplate-depth-256" else 
    if (.Platform$OS.type == "windows") "CXX11FLAGS=-O3 -march=corei7 -mtune=corei7" else
    "CXX14FLAGS += -fPIC",
    file = M, sep = "\n", append = TRUE)
```
1. Install `RStan`
```
install.packages("rstan", repos = "https://cloud.r-project.org/", dependencies = TRUE)
```
1. Try `shools` example in https://github.com/stan-dev/rstan/wiki/RStan-Getting-Started

# ubuntu 18.04 for R 4.0+
1. 
``` 
sudo add-apt-repository ppa:c2d4u.team/c2d4u4.0+
sudo apt update
```
2. 
``` sudo vi /etc/apt/sources.list ```
and add
``` 
deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/ 
```
3. install R 4.0+ version
```
sudo apt-get update
sudo apt-get install r-base
sudo apt-get install r-base-dev
```
4. remove all files in `/usr/local/lib/R/shared...`
