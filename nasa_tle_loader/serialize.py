# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import namedtuple, OrderedDict

fields = (
    'EPOCH',
    'EPOCH_MICROSECONDS',
    'NORAD_CAT_ID',
    'TLE_LINE0',
    'TLE_LINE1',
    'TLE_LINE2',
)

TLE_ = namedtuple('TLE', fields)


class TLE(TLE_):
    def as_dict(self):
        return OrderedDict((field, self[idx]) for idx, field in enumerate(fields))
