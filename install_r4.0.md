# install procedure for r4.0 in linux

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9

## R base
https://rtask.thinkr.fr/installation-of-r-3-5-on-ubuntu-18-04-lts-and-tips-for-spatial-packages/

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
sudo apt-get install libcurl4-openssl-dev
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

