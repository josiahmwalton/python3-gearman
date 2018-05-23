==============
python3_gearman
==============

Description
===========
Python 3 Gearman API - Client, worker, and admin client interfaces

For information on Gearman and a C-based Gearman server, see http://www.gearman.org/

Since the current `gearman` module is only compatible with Python versions <=
2.7, and no longer in active development, this package was created. 
The majority of the work here was from folks at Yelp and other 
contributors (see Authors.txt). This package was created from the `gearman` package,
version v2.0.2, with python3-compatible fixes brought in from 
https://github.com/msjaiswal/python3-gearman. 

Additional TravisCI build functionality was brought in as well to automate
building and testing. 

Installation
============
* easy_install python3_gearman
* pip install python3_gearman

Links
=====
* 3.x source <http://github.com/josiahmwalton/python3-gearman>
* 3.x documentation <http://packages.python.org/python3-gearman/>

* 2.x source <http://github.com/Yelp/python-gearman/>
* 2.x documentation <http://packages.python.org/gearman/>

* 1.x source <http://github.com/samuel/python-gearman/>
* 1.x documentation <http://github.com/samuel/python-gearman/tree/master/docs/>

Contributing
===========

Contributions are welcome. In order for your changes to be incorporated, they
need to follow the general process:
* Your build must past all PEP8 code style checks and unit tests
* As new functionality is added, please write the corresponding unit tests
* For passing builds, please submit a pull request (PR) to submit your
  changes for inclusion