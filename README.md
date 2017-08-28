# dataviz.andrewheiss.com

This repository contains the code for generating [dataviz.andrewheiss.com](https://dataviz.andrewheiss.com).

## Pelican

The site is generated with [Pelican](http://docs.getpelican.com/en/stable/), a static site generator written in Python. It's easiest to run with a virtual environment:

```
cd path-to-this-directory
virtualenv -p python3 pelican
source pelican/bin/activate
pip3 install -r requirements.txt
```

Once the virtual environment is running, you can use the Makefile to generate the site. Here are the most common options:

- `make devserver`: Generate the site and serve locally at http://localhost:8000
- `make html`: Generate the site without serving it
- `make rsync_upload`: Generate the site and upload it to a remote server via ssh and rsync. Configure the server destination in the Makefile

To stop the virtual environment, run `deactivate`. To restart it, run `source pelican/bin/activate` from this directory.

Also, `rpy2` has to be installed, and because R 3.4.x uses a different C compiler on macOS, Python+pip need to use that same compiler:

    brew install --with-toolchain llvm
    export PATH="/usr/local/opt/llvm/bin:$PATH"
    export LDFLAGS="-L/usr/local/opt/llvm/lib -Wl,-rpath,/usr/local/opt/llvm/lib"
    pip3 install rpy2

(see https://bitbucket.org/rpy2/rpy2/issues/403/cannot-pip-install-rpy2-with-latest-r-340#comment-38101006)
