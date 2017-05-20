# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from contextlib import closing

import requests

from .constants import NASA_TLE_URL
from .log import logger as module_logger
from .parser import tle_list
from .utils import basestring


class NasaTLELoader(object):
    __slots__ = (
        'url',
        'logger',
    )

    def __init__(self, url=NASA_TLE_URL, logger=None):
        if not isinstance(url, basestring):
            raise TypeError('Argument `url` must be subclass `basestring` (`str` for PY3)')

        self.url = url
        self.logger = logger or logging.getLogger('{}.{}'.format(module_logger.name, self.__class__.__name__))

    def load(self):
        with closing(requests.get(self.url)) as resp:
            return resp.text

    def get(self, text=None):
        if not isinstance(text, basestring):
            text = self.load()
        return tle_list(text)

    __call__ = get
