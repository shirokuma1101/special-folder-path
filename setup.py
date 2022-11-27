# -*- coding: UTF-8 -*-

# setup
from setuptools import setup, find_packages


setup(
    name='specialfolderpath',
    version='1.0',
    description='Get the path of a special folder',

    author='shirokuma1101',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)

