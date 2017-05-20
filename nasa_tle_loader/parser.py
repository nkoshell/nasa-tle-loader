# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from datetime import datetime, timedelta

from .serialize import TLE

TLE_EXP = re.compile(r"(?:^|\n)\s*"
                     r"(?P<TLE_LINE0>.{,24})"
                     r"\s*\n\s*"
                     r"(?P<TLE_LINE1>"
                     r"1 [ 0-9]{5}[A-Z] [ 0-9]{5}[ A-Z]{3} [ 0-9]{5}[.][ 0-9]{8} "
                     r"(?:(?:[ +-][.][ 0-9]{8})|(?: [ +-][.][ 0-9]{7})) "
                     r"[ +-][ 0-9]{5}[+-][ 0-9] [ +-][ 0-9]{5}[+-][ 0-9] [ 0-9] [ 0-9]{4}[ 0-9])"
                     r"\s*\n\s*"
                     r"(?P<TLE_LINE2>"
                     r"2 (?P<NORAD_CAT_ID>[ 0-9]{5}) [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{7} "
                     r"[ 0-9]{3}[.][ 0-9]{4} [ 0-9]{3}[.][ 0-9]{4} [ 0-9]{2}[.][ 0-9]{13}[ 0-9])"
                     r"\s*(?:\n|$)")

TLE_DATE_EXP = re.compile(r"^.{18}([ 0-9]{5}[.][ 0-9]{8}).*$")


def find_tle(text):
    for i in TLE_EXP.finditer(text):
        yield i.groupdict()


def tle_date(tle_line_1):
    dm = TLE_DATE_EXP.match(tle_line_1)
    d = dm and dm.group(1)
    year = 2000 + int(d[0:2])
    days_since_year_start = float(d[2:])
    return datetime(year, 1, 1, 0, 0, 0, 0) + timedelta(days=days_since_year_start - 1)


def tle_list(text):
    result = []
    for tle in find_tle(text):
        dt = tle_date(tle['TLE_LINE1'])
        result.append(TLE(EPOCH=dt.strftime('%Y-%m-%d %H:%M:%S'), EPOCH_MICROSECONDS=dt.strftime('%f'), **tle))
    return result
