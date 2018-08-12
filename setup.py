#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Mancala",
    version = "0.0.1",
    author = "Leonie",
    description = ("Mancala for Python"),
    license = "NONE",
    keywords = "mancala",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=('tests', 'docs'))
)