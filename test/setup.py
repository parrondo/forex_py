#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import codecs

from setuptools import setup, find_packages, Extension

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    # https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()

setup(
    name='frxpy',
    version='0.0.1.dev1',
    description='Python Scripts For Predicting Forex datas.',
    author='0h-n0',
    author_email='kbu94982@gmail.com',
    long_description=read('README.rst'),
    url='https://github.com/0h-n0/forex_py',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License (MIT)'
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    entry_points = {
        'console_scripts' : ['csv2db = forex_py.frxpy.commands.csv2db:csv2db'],
    },
    setup_requires=['pytest-runner'],
    test_require=['pytest'] 
)

