from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(
    name='ckanext-example',
    version=version,
    description="Just a test of fields",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Daniel Davis',
    author_email='daniel.davis@cfpb.gov',
    url='github.com/cfpb',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.example'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        example_ckanext=ckanext.example.plugin:ExampleIDatasetFormPlugin
    ''',
)
