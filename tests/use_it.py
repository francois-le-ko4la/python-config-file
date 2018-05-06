#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""
import pathlib
from configjson import ConfigJSON


path = pathlib.Path(__file__).resolve().parent

json_file = pathlib.PurePath(path, 'facebook.json')
config = ConfigJSON(json_file)
print(config)
