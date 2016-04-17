#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function, unicode_literals)

import argparse
import os

from ripe import VERSION


def run(package):
    os.system('echo y | pip uninstall {}'.format(package.split('/')[-1]))

    if point_install_to_current_dir(package):
        os.system('pip install .')
    elif point_install_to_child_dir(package):
        os.system('pip install ./{}'.format(package))
    else:
        # for longhand paths, ie `ripe ../../app_name`
        os.system('pip install {}'.format(os.path.expanduser(package)))


def point_install_to_current_dir(package):
    return (package == os.getcwd().split('/')[-1] or package is None)


def point_install_to_child_dir(package):
    return os.path.exists(os.getcwd() + '/{}'.format(package))


def prepare_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('package', nargs='?', default=os.getcwd().split('/')[-1])
    parser.add_argument('--extra-index-url', nargs='?', default = "")
    parser.add_argument('--version', action='version', version='%(prog)s ' + VERSION)

    return parser


def main():
    parser = prepare_parser()
    args = parser.parse_args()

    if not os.path.isfile(os.getcwd() + '/setup.py') and not os.path.isfile(os.getcwd() + "/{}/setup.py".format(args.package)):
        print ("Error -- ripe should only be used when testing out versions of a local package, and hence NEEDS")
        print ("to be run from or pointed towards a  `pip install .`-able location" )
    else:
        command = "{} {}".format(args.extra_index_url, args.package)
        run(command.strip())
