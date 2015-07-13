#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='wmsproxy',
      version='0.1.1',
      description='Convert CartoDB projects on-the-fly to WMS services.',
      author='Omniscale GmbH & Co KG',
      author_email='support@omniscale.de',
      url='http://www.omniscale.de',
      packages=find_packages(),
      license='Apache 2',
      install_requires=[
        "PyYAML",
        "requests",
        "mapproxy>=1.7.1",
      ]
)
