"""library for supporting the collection+json format in django-rest-framework
"""
import os
import sys
sys.path.append(os.path.dirname(__file__))
from drf_collection_json import version
from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    sys.exit(os.system('python setup.py sdist upload'))

requires = ['djangorestframework', 'collection_json']

setup(
    name='drf_collection_json',
    version=version,
    description='library for supporting the collection+json format in django-rest-framework',
    long_description=__doc__,
    author='Daniel DeSousa',
    author_email='dan+drfcollectionjson@desousa.cc',
    url='http://github.com/dandesousa/drf-collection-json',
    license='CC0 1.0 Universal',
    platforms='any',
    test_suite="tests.test_suite.test_all",
    packages=find_packages(exclude=["tests"]),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        # TODO: add additional classifiers
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
