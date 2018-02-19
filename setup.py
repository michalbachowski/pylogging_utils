#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.0.1'


def read(fname):
    return codecs.open(
        os.path.join(os.path.dirname(__file__), fname), 'r', 'utf-8').read()

readme = read('README.rst')

setup(
    name='logging_utils',
    version=__version__,
    description='',
    long_description=readme,
    author='Michał Bachowski',
    author_email='michalbachowski@gmail.com',
    url='https://github.com/michalbachowski/pylogging_utils',
    py_modules=['logging_utils'],
    include_package_data=True,
    license="BSD",
    zip_safe=False,
    keywords='logging_utils',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Topic :: System :: Logging',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

