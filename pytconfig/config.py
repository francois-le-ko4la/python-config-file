#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0903
"""

  ####    ####   #    #  ######
 #    #  #    #  ##   #  #
 #       #    #  # #  #  #####
 #       #    #  #  # #  #
 #    #  #    #  #   ##  #
  ####    ####   #    #  #

"""

import json
import yaml
from pytconfig.__about__ import FILENAME, DATA
from pytconfig.file import PytFile
from pytconfig.exceptions import PytConfigLoadError


class PytConfigFile(dict):
    """
    This Class provides a dict from a JSON File or YAML file.
    You can use it to avoid a lot of CONST in your scripts.

    Use:
       >>> # pathlib to run the test everywhere
       >>> import pathlib
       >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
       >>> cur_file = '/etc/fst'
       >>> config = PytConfigFile(cur_file, PytConfigFile.isjson)
       Traceback (most recent call last):
       ...
       pytconfig.exceptions.PytConfigFileNotFound: File "/etc/fst" not found!
       >>> cur_file = path + '../LICENSE'
       >>> config = PytConfigFile(cur_file, PytConfigFile.isjson)
       Traceback (most recent call last):
       ...
       pytconfig.exceptions.PytConfigLoadError: Can't load the configuration...
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
        self.__loader = filetype()
        self.__load()

    @staticmethod
    def isjson():
        """
        use it to define the file type
        """
        return json.loads

    @staticmethod
    def isyaml():
        """
        use it to define the file type
        """
        return yaml.load

    def __load(self):
        try:
            self[FILENAME] = str(self.__configfile)
            self[DATA] = self.__loader(self.__configfile.read())
        except ValueError:
            raise PytConfigLoadError()

    def __getitem__(self, key):
        current_data = super().__getitem__(DATA)
        return current_data[key]

    def __len__(self):
        return len(super().__getitem__(DATA))

    def __iter__(self):
        return iter(super().__getitem__(DATA))

    def keys(self):
        return super().__getitem__(DATA).keys()

    def items(self):
        return super().__getitem__(DATA).items()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
