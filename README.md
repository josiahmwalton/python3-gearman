<table>
<tr>
  <td>License</td>
  <td>
    <a href="https://github.com/josiahmwalton/python3-gearman/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="license" />
    </a>
</td>
</tr>
<tr>
  <td>Build Status</td>
  <td>
    <a href="https://travis-ci.org/josiahmwalton/python3-gearman">
    <img src="https://travis-ci.org/josiahmwalton/python3-gearman.svg?branch=master" alt="travis build status" />
    </a>
  </td>
</tr>
</table>

Description
===========
Python 3 Gearman API - Client, worker, and admin client interfaces

For information on Gearman and a C-based Gearman server, see http://www.gearman.org/

Since the current `gearman` module is with Python versions <=
2.7 and no longer in active development, this package was created. 
The vast majority of the work here was from folks at Yelp and other 
contributors (see Authors.txt). This package was based off an initial clone of 
the `gearman` package, tag `v2.0.2`. Python3-compatible fixes to core classes 
and functions were brought in from https://github.com/msjaiswal/python3-gearman. 
In addition, python3 updates to the unit tests were also included. Moreover, 
TravisCI functionality was brought in to automate
building and testing. 

Installation
============
* easy_install python3_gearman
* pip install python3_gearman

Links
=====

Python 3
* source <http://github.com/josiahmwalton/python3-gearman>
* documentation <http://packages.python.org/python3-gearman/>

Python 2 and earlier
* 2.x source <http://github.com/Yelp/python-gearman/>
* 2.x documentation <http://packages.python.org/gearman/>
* 1.x source <http://github.com/samuel/python-gearman/>
* 1.x documentation <http://github.com/samuel/python-gearman/tree/master/docs/>

Contributing
===========

Contributions are encouraged and welcome. In order for your changes to be incorporated, they
need to follow the general guidelines:
* Please do your work on a branch created from the `develop` branch (see the GitFlow approach to development)
* Your build must past all PEP8 code style checks and unit tests
* As new functionality is added, please write the corresponding unit tests
* For passing builds, please submit a pull request (PR) to submit your
  changes for inclusion into the `develop` branch