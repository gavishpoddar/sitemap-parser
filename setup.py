#!/usr/bin/env python

from setuptools import setup, find_packages
from usp.__about__ import __version__


setup(
    name='sitemap-parser',
    version=__version__,
    description='Sitemap Parser',
    packages=find_packages(exclude=['tests']),
    zip_safe=True,
    python_requires='>=3.6',
    install_requires=[
        # Parsing arbitrary dates (sitemap date format is standardized but some implementations take liberties)
        'python-dateutil>=2.1,<3.0.0',
        # Making HTTP requests
        'requests>=2.2.1',
        'Faker',
        'cloudscraper',
    ],
)
