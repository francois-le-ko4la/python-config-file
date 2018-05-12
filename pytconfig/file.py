#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

 ######     #    #       ######
 #          #    #       #
 #####      #    #       #####
 #          #    #       #
 #          #    #       #
 #          #    ######  ######

"""

import pathlib


class PytFile(object):

    """
    >>> fstab = PytFile("/etc/fstab")
    >>> print(fstab.filename.stem)
    fstab
    >>> print(fstab)
    /etc/fstab
    >>> # pathlib to run the test everywhere
    >>> import pathlib
    >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
    >>> license = PytFile(path + "../LICENSE")
    >>> print(license.filename.stem)
    LICENSE
    >>> #print(license.read())

    """

    def __init__(self, filename):
        self.__path = pathlib.Path()
        self.filename = filename

    @property
    def filename(self):
        """
        /path/to/the/file
        """
        return self.__path

    @filename.setter
    def filename(self, value):
        self.__path = pathlib.Path()
        if pathlib.Path(value).exists():
            self.__path = pathlib.Path(value).resolve()
        else:
            raise IOError("File not found !")

    def __repr__(self):
        return str(self.__path)

    def __str__(self):
        return repr(self)

    def read(self):
        """
        Read the content
        """
        return self.__path.read_text()
