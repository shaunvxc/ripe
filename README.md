# ripe [![PyPI version](https://badge.fury.io/py/ripe.svg)](https://badge.fury.io/py/ripe) [![forthebadge](https://img.shields.io/badge/warning-NSFW-orange.svg)](http://forthebadge.com)
An unnecessary micro-optimization for those who (like me) spend too much time using `--force-reinstall` or `pip uninstall`/`install` while testing every little incremental change to their packages. 

## Why?
While `pip` itself offers equivalent functionality with its `--force-reinstall` flag, `ripe` will accomplish the same thing in fewer keystrokes.  

If you find yourself in a workflow where you are continuously reinstalling local copies of your packages to test out changes, you might find `ripe` to be a useful little hack.

## Installation

`$ pip install ripe`

### Usage
To uninstall the currently installed version of your package, and reinstall using your local changes, simply run (from the root-dir of your package):

`$ ripe`

`ripe` will automatically pass `y` to the `Proceed (y/n)` prompt for uninstalling, uninstall the package, and then reinstalls your local copy of the package using `pip install .` 

#### Disclaimer
This is a little tool that uses os.system() to `pip uninstall` and `pip install .` the local copy of your packages onto your system (or current virtual environment).  As such this package should **only** be used locally and properly. 
