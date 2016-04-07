#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

import argparse
import os

from ripe import VERSION

def run(package):
    os.system('echo y | pip uninstall {}'.format(package.split('/')[-1]))

    if package == os.getcwd().split('/')[-1] or package is None:
        os.system('pip install .')
    elif os.path.exists(os.getcwd() + '/{}'.format(package)):
        # for shorthand, ie `ripe app_name -> pip install ./app_name`
        os.system('pip install ./{}'.format(package))
    else:
        # for longhand paths, ie `ripe ../../app_name`
        os.system('pip install {}'.format(os.path.expanduser(package)))


def prepare_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('package', nargs='?', default=os.getcwd().split('/')[-1])
    parser.add_argument('--version', action='version', version='%(prog)s ' + VERSION)
    return parser


def main():
    parser = prepare_parser()
    args = parser.parse_args()

    if not os.path.isfile(os.getcwd() + '/setup.py') and not os.path.isfile(os.getcwd() + "/{}/setup.py".format(args.package)):
        print ("Error -- ripe should only be used when testing out versions of a local package, and hence NEEDS")
        print ("to be run from or pointed towards a  `pip install .`-able location" )
    else:
        run(args.package)
