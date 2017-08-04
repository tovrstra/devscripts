#!/usr/bin/env python

from __future__ import print_function

from glob import glob
import subprocess

from setuptools import setup


git_describe = subprocess.check_output(["git", "describe", "--tags"])
version_words = git_describe.decode('utf-8').strip().split('-')[:2]
__version__ = version_words[0]
if len(version_words) > 1:
    __version__ += '.post' + version_words[1]


setup(name='devscripts',
    version=__version__,
    description='Scripts often used in software development.',
    author='Toon Verstraelen',
    author_email='Toon.Verstraelen@UGent.be',
    scripts=glob("scripts/*"),
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
