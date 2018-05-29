#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 ######  #####   #####    ####   #####
 #       #    #  #    #  #    #  #    #
 #####   #    #  #    #  #    #  #    #
 #       #####   #####   #    #  #####
 #       #   #   #   #   #    #  #   #
 ######  #    #  #    #   ####   #    #

"""


class PytConfigError(Exception):
    """
    Generic exception for pytconfig
    """
    pass


class PytConfigFileNotFound(PytConfigError):
    """
    Config file is not found
    """
    def __init__(self, value):
        super().__init__("File \"{}\" not found!".format(value))


class PytConfigLoadError(PytConfigError):
    """
    Content cannot be loaded.
    """
    def __init__(self):
        super().__init__("Can't load the configuration...")


__all__ = ['PytConfigError', 'PytConfigFileNotFound', 'PytConfigLoadError']


if __name__ == "__main__":
    import doctest
    doctest.testmod()
