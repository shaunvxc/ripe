# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ripe import point_install_to_child_dir, point_install_to_current_dir
from mock import patch

@patch('os.getcwd', return_value='somepath/some_package')
def test_point_install_to_current_dir(mock):
    assert point_install_to_current_dir('some_package') == True
    assert point_install_to_current_dir(None) == True

@patch('os.path.exists', return_value=True)
def test_point_install_to_child_dir(mock):
    assert point_install_to_child_dir('some_package') == True
