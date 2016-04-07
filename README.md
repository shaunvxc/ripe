# ripe [![PyPI version](https://badge.fury.io/py/ripe.svg)](https://badge.fury.io/py/ripe) [![forthebadge](https://img.shields.io/badge/warning-NSFW-orange.svg)](http://forthebadge.com)
An unnecessary micro-optimization for those who (like me) spend too much time using `--force-reinstall` or `pip uninstall`/`install` while testing every little incremental change to their packages. 

## Why?
If you find yourself in a workflow where you are continuously reinstalling local copies of your packages to test out changes, you might find `ripe` to be a useful little hack.

While `pip` itself offers equivalent functionality with its `--force-reinstall` flag, `ripe` will accomplish the same thing in fewer keystrokes.  

## Installation

`$ pip install ripe`

## Usage
When run from the root folder of a package (on the same level as the `setup.py` file) as:

`$ ripe` 

uninstalls the currently installed version of your package, and reinstalls it using your local changes.

You can also point ripe to the package you wish to `ripen` up with your local changes. IE:

`$ ripe packagename`
 
 or

`$ ripe /path/to/local/package`

In all cases, `ripe` will automatically pass `y` to the `Proceed (y/n)` prompt for uninstalling.

***Note*** `ripe` must either be run from or pointed to a `pip-installable` location (it checks for `setup.py`. If it is run from elsewhere, it will tell you as much before exiting) 

#### Disclaimer
This is a little tool that uses `os.system()` to `pip uninstall` and `pip install .` the local copy of your packages onto your system (or current virtual environment).  As such this package should **only** be used locally and properly. 
