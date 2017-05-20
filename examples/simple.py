# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import json

from nasa_tle_loader import NasaTLELoader


def main():
    # Loader initializing
    loader = NasaTLELoader()

    # Getting list `nasa_tle_loader.TLE`(namedtuple like) objects
    tle_list = loader()

    # Print result as JSON
    print(json.dumps([tle.as_dict() for tle in tle_list[:3]], indent=2))


if __name__ == '__main__':
    main()
