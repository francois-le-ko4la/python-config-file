#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A setuptools based setup module.

Example:
    ./python test
    ./python install

Test:
    This script has been tested and validated on Ubuntu.

"""
import os
from setuptools import setup, find_packages
from setuptools.config import read_configuration
import warnings


warnings.filterwarnings("ignore")
packages=find_packages()
print("PKG Found: {} ".format(packages))
cfg = read_configuration('./setup.cfg')
# print(cfg)
cfg["options"].update(cfg["metadata"])
cfg = cfg["options"]
setup(use_scm_version=True, **cfg)
