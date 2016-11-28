#!/usr/bin/env python

#try:
#    from setuptools import setup
#except ImportError:
#    from easy_install import setup

from distutils.core import setup

setup(name= 'CLSR',
      description= 'Following the textbook "Introduction to Algorithms"',
      author= 'Artem Vovk',
      url= 'https://github.com/kierachell',
      download_url= 'https://github.com/kierachell',
      author_email= 'artemavovk@gmail.com',
      version= '0.1a',
      requires= ['pytest'],
      packages= ['CLSR'],
      scripts= [],
)
