# ripe  [![Build Status](https://travis-ci.org/shaunvxc/ripe.svg?branch=master)](https://travis-ci.org/shaunvxc/ripe) [![PyPI version](https://badge.fury.io/py/ripe.svg)](https://badge.fury.io/py/ripe) 

A <s>useless</s> useful micro-optimization for those who (like me) spend too much time using `--force-reinstall` or `pip uninstall`/`install` while testing every incremental change to their packages. 

## Why?
If you find yourself in a workflow where you are continuously reinstalling local copies of your packages to test out changes, you might find `ripe` to be a useful little hack.

While `pip` itself offers equivalent functionality with its `--force-reinstall` flag, `ripe` will accomplish the same thing in fewer keystrokes.  

## Usage

- Run from the root-level of a package to uninstall the currently installed version, and reinstall using your local changes:

    `$ ripe` 

- You can also point ripe to the package you wish to reinstall with your local changes:

    `$ ripe packagename`
 
- For more complicated paths:

    `$ ripe /path/to/local/package`
    
- For packages with dependencies not available on pypi:
    
    `$ ripe --extra-index-url index_url [path_to_package]`

In all cases, `ripe` will automatically pass `y` to the `Proceed (y/n)` prompt for uninstalling.

***Note*** `ripe` must either be run from or pointed to a `pip-installable` location (it checks for `setup.py`. If it is run from elsewhere, it will tell you as much before exiting) 

## Installation

`$ pip install ripe`


#### Disclaimer
This is a little tool that uses `os.system()` to `pip uninstall` and `pip install` the local copy of your package onto your system (or current virtual environment).  As such this package should **only** be used locally and properly. 
