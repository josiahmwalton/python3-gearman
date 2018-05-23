#!/usr/bin/env python

from setuptools import setup

from python3_gearman import __version__ as version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python3_gearman',
    version=version,
    description=(
        'Python 3 Gearman API - Client, worker, and admin client interfaces'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/josiahmwalton/python3-gearman',
    packages=['python3_gearman'],
    python_requires='>=3',
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
