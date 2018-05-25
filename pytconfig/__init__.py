#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# python-config-file
## Description:

This package loads the configuration values defined in external JSON or
YAML file, not the built-in data structures.

## Setup:

```shell
$ git clone https://github.com/francois-le-ko4la/python-config-file.git
$ cd python-config-file
$ make install
```

## Test:

This module has been tested and validated on Ubuntu.
```shell
$ make test
```

## Use:

```python
from pytconfig import PytConfigFile
conf = "/path/to/the/file"
# PytConfigFile(path (str), PytConfigFile.{isjson|isyaml})
config = PytConfigFile(conf, PytConfigFile.isjson)
print(config['mykey'])
print(config.keys())
print(len(config))
```

## Project Structure
```
.
├── last_check.log
├── LICENSE
├── Makefile
├── pictures
│   ├── classes_pytconfig.png
│   └── packages_pytconfig.png
├── pytconfig
│   ├── __about__.py
│   ├── config.py
│   ├── file.py
│   └── __init__.py
├── README.md
├── requirements.txt
├── runtime.txt
├── setup.cfg
├── setup.py
└── tests
    ├── facebook.json
    ├── facebook.yaml
    ├── test_doctest.py
    └── test_pycodestyle.py
```

## Todo:

- [X] Create the project
- [X] Write code and tests
- [X] Test installation and requirements (setup.py and/or Makefile)
- [X] Test code
- [X] Validate features
- [X] Write Doc/stringdoc
- [X] Run PEP8 validation
- [X] Clean & last check
- [X] Fix global header
- [X] Fix tests
- [X] Fix doc
- [X] Release : 0.1.7
- [X] change (un)install process
- [X] remove MANIFEST.in
- [X] manage global var: __version__....
- [X] improve the doc
- [X] remove old tests
- [X] Release : 0.1.9
- [X] improve Makefile
- [X] Release : 0.1.10


## License

This package is distributed under the [GPLv3 license](./LICENSE)

"""

from pytconfig.__about__ import __version__, __author__, __license__, __url__
from pytconfig.file import PytFile
from pytconfig.config import PytConfigFile
