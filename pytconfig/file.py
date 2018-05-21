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
    >>> data_file = PytFile("lorem")
    Traceback (most recent call last):
    ...
    OSError: File not found !
    >>> data_file = PytFile(None)
    Traceback (most recent call last):
    ...
    OSError: File not found !
    >>> fstab = PytFile("/etc/fstab")
    >>> fstab.filename.stem
    'fstab'
    >>> fstab
    /etc/fstab
    >>> # pathlib to run the test everywhere
    >>> import pathlib
    >>> path = str(pathlib.Path(__file__).resolve().parent) + "/"
    >>> license = PytFile(path + "../LICENSE")
    >>> license.filename.stem
    'LICENSE'
    >>> license.exists()
    True
    >>> result = license.read()
    >>> result = result.split("\\n")
    >>> result[0]
    '                    GNU GENERAL PUBLIC LICENSE'
    """

    def __init__(self, filename):
        self.__exists = False
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
        if pathlib.Path(str(value)).exists():
            self.__path = pathlib.Path(str(value)).resolve()
            self.__exists = True
        else:
            self.__exists = False
            raise IOError("File not found !")

    def exists(self):
        """
        file exists
        """
        return self.__exists

    def __repr__(self):
        return str(self.__path)

    def __str__(self):
        return repr(self)

    def read(self):
        """
        Read the content
        """
        return self.__path.read_text()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
