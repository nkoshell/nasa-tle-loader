NasaTLELoader
_____________

Small TLE loader from NASA.


Requirements
------------

- requests >= 2.14.2


Installing
__________

::

    pip install nasa-tle-loader


Getting started
---------------

To retrieve something from Space-Track:

.. code-block:: python

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

Result::

  [
    {
      "EPOCH": "2017-05-17 13:16:58",
      "EPOCH_MICROSECONDS": "124064",
      "NORAD_CAT_ID": "25544",
      "TLE_LINE0": "ISS",
      "TLE_LINE1": "1 25544U 98067A   17137.55345051  .00016717  00000-0  10270-3 0  9004",
      "TLE_LINE2": "2 25544  51.6389 191.0057 0005051 169.7469 190.3787 15.54030000 16987"
    },
    {
      "EPOCH": "2017-05-17 22:32:35",
      "EPOCH_MICROSECONDS": "151072",
      "NORAD_CAT_ID": "25544",
      "TLE_LINE0": "ISS",
      "TLE_LINE1": "1 25544U 98067A   17137.93929573  .00016717  00000-0  10270-3 0  9014",
      "TLE_LINE2": "2 25544  51.6398 189.0848 0005258 166.2909 193.8387 15.53887043 17040"
    },
    {
      "EPOCH": "2017-05-18 01:37:47",
      "EPOCH_MICROSECONDS": "963136",
      "NORAD_CAT_ID": "25544",
      "TLE_LINE0": "ISS",
      "TLE_LINE1": "1 25544U 98067A   17138.06791624  .00016717  00000-0  10270-3 0  9024",
      "TLE_LINE2": "2 25544  51.6394 188.4430 0005111 170.0057 190.1198 15.53888284 17061"
    }
  ]

Source code
-----------

The latest developer version is available in a github repository:
https://github.com/nkoshell/nasa-tle-loader
