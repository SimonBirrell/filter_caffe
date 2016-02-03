#!/usr/bin/env python

# -- from rosgraph --
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['filter_caffe'],
    package_dir={'': 'src/filter_caffe'},
)

setup(**setup_args)
