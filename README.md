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

>>> from pytconfig import PytConfigFile
>>> conf = "/path/to/the/file"
>>> # PytConfigFile(path (str), PytConfigFile.{isjson|isyaml})
>>> config = PytConfigFile(conf, PytConfigFile.isjson)
>>> print(config['mykey'])
>>> print(config.keys())
>>> print(len(config))

```

## Project Structure
```
.
├── last_check.log
├── LICENSE
├── Makefile
├── MANIFEST.in
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
    ├── test_pycodestyle.py
    └── use_it.py
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
- [X] Release : 0.1.4

## License

pytping is distributed under the [GPLv3 license](./LICENSE)
## Dev notes
### Runtime

```
python-3.6.x

```
### Requirements

```
setuptools>=36.2.7
pycodestyle>=2.3.1

```
### UML Diagram
![alt text](pictures/classes_pytconfig.png)

### Objects
[PytConfigFile()](#pytconfigfile)<br />
[PytConfigFile.__getitem__(self, key)](#pytconfigfilegetitemself-key)<br />
[PytConfigFile.__init__(self, filename, filetype)](#pytconfigfileinitself-filename-filetype)<br />
[PytConfigFile.__iter__(self)](#pytconfigfileiterself)<br />
[PytConfigFile.__len__(self)](#pytconfigfilelenself)<br />
[PytConfigFile.__load(self)](#pytconfigfile__loadself)<br />
[PytConfigFile.isjson(self)](#pytconfigfileisjsonself)<br />
[PytConfigFile.isyaml(self)](#pytconfigfileisyamlself)<br />
[PytConfigFile.items(self)](#pytconfigfileitemsself)<br />
[PytConfigFile.keys(self)](#pytconfigfilekeysself)<br />
[PytFile()](#pytfile)<br />
[@Property: PytFile.filename](#property-pytfilefilename)<br />
[PytFile.__init__(self, filename)](#pytfileinitself-filename)<br />
[PytFile.__repr__(self)](#pytfilereprself)<br />
[PytFile.__str__(self)](#pytfilestrself)<br />
[PytFile.read(self)](#pytfilereadself)<br />


#### PytConfigFile()
```python
class PytConfigFile(dict):
```

```
This Class provides a dict from a JSON File or YAML file.
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
```

##### PytConfigFile.__getitem__(self, key)
```python
def PytConfigFile.__getitem__(self, key):
```
> <br />
> x.__getitem__(y) <==> x[y]<br />
> <br />
##### PytConfigFile.__init__(self, filename, filetype)
```python
def PytConfigFile.__init__(self, filename, filetype):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### PytConfigFile.__iter__(self)
```python
def PytConfigFile.__iter__(self):
```
> <br />
> Implement iter(self).<br />
> <br />
##### PytConfigFile.__len__(self)
```python
def PytConfigFile.__len__(self):
```
> <br />
> Return len(self).<br />
> <br />
##### PytConfigFile.__load(self)
```python
def PytConfigFile.__load(self):
```
> <br />
> Docstring empty<br />
> <br />
##### PytConfigFile.isjson(self)
```python
def PytConfigFile.isjson(self):
```
> <br />
> Docstring empty<br />
> <br />
##### PytConfigFile.isyaml(self)
```python
def PytConfigFile.isyaml(self):
```
> <br />
> Docstring empty<br />
> <br />
##### PytConfigFile.items(self)
```python
def PytConfigFile.items(self):
```
> <br />
> D.items() -> a set-like object providing a view on D's items<br />
> <br />
##### PytConfigFile.keys(self)
```python
def PytConfigFile.keys(self):
```
> <br />
> D.keys() -> a set-like object providing a view on D's keys<br />
> <br />
#### PytFile()
```python
class PytFile(object):
```

```
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
```

##### @Property: PytFile.filename
```python
@property
def PytFile.filename(self):
@filename.setter
def PytFile.filename(self, value):

```
> <br />
> @Property<br />
> <br />
##### PytFile.__init__(self, filename)
```python
def PytFile.__init__(self, filename):
```
> <br />
> Initialize self.  See help(type(self)) for accurate signature.<br />
> <br />
##### PytFile.__repr__(self)
```python
def PytFile.__repr__(self):
```
> <br />
> Return repr(self).<br />
> <br />
##### PytFile.__str__(self)
```python
def PytFile.__str__(self):
```
> <br />
> Return str(self).<br />
> <br />
##### PytFile.read(self)
```python
def PytFile.read(self):
```
> <br />
> Docstring empty<br />
> <br />
