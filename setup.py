# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import re

import os
from setuptools import setup

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION_REGEXP = re.compile(r"^__version__ = [\'\"](.+?)[\'\"]$", re.MULTILINE)


def read(fn):
    with codecs.open(os.path.join(PROJECT_DIR, fn), encoding='utf-8') as f:
        return f.read().strip()


def version():
    try:
        return VERSION_REGEXP.findall(read(os.path.join('nasa_tle_loader', '__init__.py')))[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


vn = version()
url = 'https://github.com/nkoshell/nasa-tle-loader'

setup(
    name='nasa-tle-loader',
    description='Small TLE loader from NASA',
    long_description=read('README.rst'),
    version=vn,
    packages=['nasa_tle_loader'],
    url=url,
    download_url='{url}/archive/{version}.tar.gz'.format(url=url, version=vn),
    license='MIT',
    author='nkoshell',
    author_email='nikita.koshelev@gmail.com',
    install_requires=['requests>=2.14.2'],
)
