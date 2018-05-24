#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
from pkg_resources import get_distribution
import json


__pkg_name__ = __name__.split(".")[0]
__pkg_name__ = "pytconfig"

try:
    about = json.loads(get_distribution(__pkg_name__).get_metadata("metadata.json"))
    __version__ = about["version"]
    __author__ = about["extensions"]["python.details"]["contacts"][0]["name"]
    __email__ = about["extensions"]["python.details"]["contacts"][0]["email"]
    __url__ = about["download_url"]
    __license__ = about["license"]
    __description__ = about["summary"]

except FileNotFoundError:
    try:
        pkgInfo = get_distribution(__pkg_name__).get_metadata('METADATA')
    except FileNotFoundError:
        pkgInfo = get_distribution(__pkg_name__).get_metadata('PKG-INFO')

    __version__ = get_distribution(__pkg_name__).version

    from email import message_from_string
    msg = message_from_string(pkgInfo)
    for key, value in msg.items():
        print("{}-{}".format(key, value))
        if key.startswith("Author-email"):
            __email__ = value
        elif key.startswith("Author"):
            __author__ = value
        elif key.startswith("Download-URL"):
            __url__ = value
        elif key.startswith("License"):
            __license__ = value
        elif key.startswith("Summary"):
            __description__ = value
