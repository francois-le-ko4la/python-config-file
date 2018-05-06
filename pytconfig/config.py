#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 #####                                                #
#     #   ####   #    #  ######     #     ####        #   ####    ####   #    #
#        #    #  ##   #  #          #    #    #       #  #       #    #  ##   #
#        #    #  # #  #  #####      #    #            #   ####   #    #  # #  #
#        #    #  #  # #  #          #    #  ### #     #       #  #    #  #  # #
#     #  #    #  #   ##  #          #    #    # #     #  #    #  #    #  #   ##
 #####    ####   #    #  #          #     ####   #####    ####    ####   #    #

"""

import json
import yaml
from pytconfig.file import PytFile


class Default:
    encode = 'utf-8'
    msg_cantload = "Can't load the file..."
    key_filename = 'filename'
    key_data = 'data'


class PytConfigFile(dict):
    """
    This Class provides a dict from a JSON File.
    You can use it to avoid a lot of CONST in your scripts.

    Use:
       >>> # pathlib to run the test everywhere
       >>> import pathlib
       >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
       >>> cur_file = path + '../tests/facebook.jso'
       >>> config = PytConfigFile(cur_file, PytConfigFile.isjson)
       Traceback (most recent call last):
       ...
       OSError: File not found !
       >>> cur_file = path + '../LICENSE'
       >>> config = PytConfigFile(cur_file, PytConfigFile.isjson)
       Traceback (most recent call last):
       ...
       ValueError: Can't load the file...
       >>> cur_file = path + '../tests/facebook.json'
       >>> config = PytConfigFile(cur_file, PytConfigFile.isjson)
       >>> print(config['debug'])
       True
       >>> print(config.keys())
       dict_keys(['description', 'debug', 'data'])
       >>> print(len(config))
       3
       >>> cur_file = path + '../tests/facebook.yaml'
       >>> configyaml = PytConfigFile(cur_file, PytConfigFile.isyaml)
       >>> print(configyaml['debug'])
       True
       >>> print(configyaml.keys())
       dict_keys(['description', 'debug', 'data'])
       >>> print(len(configyaml))
       3
    """

    def __init__(self, filename, filetype):
        super().__init__()
        self.__configfile = PytFile(filename)
        self.__loader = filetype(self)
        self.__load()

    def isjson(self):
        return json.loads

    def isyaml(self):
        return yaml.load

    def __load(self):
        try:
            self[Default.key_filename] = str(self.__configfile)
            self[Default.key_data] = self.__loader(self.__configfile.read())
        except ValueError as error:
            raise ValueError(Default.msg_cantload)

    def __getitem__(self, key):
        current_data = super().__getitem__(Default.key_data)
        return current_data[key]

    def __len__(self):
        return len(super().__getitem__(Default.key_data))

    def __iter__(self):
        return iter(super().__getitem__(Default.key_data))

    def keys(self):
        return super().__getitem__(Default.key_data).keys()

    def items(self):
        return super().__getitem__(Default.key_data).items()
