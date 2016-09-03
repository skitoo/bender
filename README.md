# Bender

Ansible playbook to manage my Debian server.

[![Build Status](https://travis-ci.org/skitoo/bender.svg?branch=master)](https://travis-ci.org/skitoo/bender)
[![Licence GPL](http://img.shields.io/badge/license-GPL-yellow.svg)](http://www.gnu.org/licenses/quick-guide-gplv3.fr.html)

## Dependencies

Bender relies on several outside packages and programs to function.

* [Docker](https://docker.com)
* [Python 2.7](https://python.org)
* [Ansible](https://ansible.com)
* [Molecule](http://molecule.readthedocs.org)

## Quick Start

Clone the project:

```
$ git clone git@github.com:skitoo/bender.git
$ cd bender
```

Install ansible and molecule:

```
$ pip install ansible
$ pip install molecule
```

Run molecule

```
$ molecule test
```

## LICENSE

[GNU GENERAL PUBLIC LICENSE Version 3](http://www.gnu.org/licenses/gpl-3.0.txt)
