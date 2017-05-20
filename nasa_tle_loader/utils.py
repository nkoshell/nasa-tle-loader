# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from .constants import PY3

if PY3:
    basestring = str
    unicode = str
else:
    basestring = basestring
    unicode = unicode

CLEAN_EXP = re.compile(r' +')


def clean_line(line):
    return CLEAN_EXP.sub(' ', line)
