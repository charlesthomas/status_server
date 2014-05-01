#!/usr/bin/env python
from setuptools import setup

NAME = 'status_server'
DESCRIPTION = 'Serve HTTP statuses by URL'
AUTHOR = 'Charles Thomas'
EMAIL = 'ch@rlesthom.as'
URL = 'https://github.com/charlesthomas/%s' % NAME
VERSION = open('VERSION').read().strip()
LONG_DESC = open('README.rst').read()
LICENSE = open('LICENSE').read()
REQUIREMENTS = [open('requirements.txt').readlines()]
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing :: Traffic Generation',
]

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    packages=[NAME],
    url=URL,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESC,
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    entry_points='''
    [console_scripts]
    status_server = status_server.status_server:main
    '''
)
