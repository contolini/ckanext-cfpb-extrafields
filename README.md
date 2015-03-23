# CFPB CKAN Extra Fields

[![Build Status](https://travis-ci.org/marcesher/ckanext-cfpb-extrafields.png)](https://travis-ci.org/marcesher/ckanext-cfpb-extrafields)
[![Coverage Status](https://coveralls.io/repos/marcesher/ckanext-cfpb-extrafields/badge.svg)](https://coveralls.io/r/marcesher/ckanext-cfpb-extrafields)

**Description**: This is a [CKAN](http://docs.ckan.org) extension to add CFPB-specific extra metadata fields.
It is a sibling project to https://github.com/cfpb/ckan and expected to live along-side that project.


## Dependencies

## General

- Python 2.7
- virtualenv and virtualenvwrapper
- Vagrant for local testing

### Runtime

This is a CKAN extension designed to plug in to a running instance of CKAN.
For local testing, we use Vagrant. See https://github.com/cfpb/ckan for details.

### Testing

For running unit tests:

1. git clone this repository and cd into it
1. create a new virtualenv: `mkvirtualenv ckanext-cfpb-extrafields`
1. install requirements: `pip install requirements-test.txt`

## Installation

This software should live alongside a cloned copy of https://github.com/cfpb/ckan.
That project's provisioning will create a mapped directory in the Vagrant install.

For real servers, this software should be installed via `pip install`

## How to test the software

After following the testing installation instructions above, you can test with:

`nosetests -s --with-coverage --cover-package=ckanext.cfpb_extrafields.validators`

Currently the only software  under test are custom validators.


## Getting help

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

General instructions on _how_ to contribute should be stated with a link to [CONTRIBUTING](CONTRIBUTING.md).

----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)


----

## Credits and references

1. http://docs.ckan.org/en/latest/extensions/index.html
