#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from linguist import VERSION


setup(name='linguist',
      version=VERSION,
      keywords=('linguist', 'detect', 'programming', 'language'),
      description='Language Savant',
      long_description='Language Savant',
      license='New BSD',

      url='https://github.com/douban/linguist',
      author='liluo',
      author_email='i@liluo.org',

      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      install_requires=['PyYAML',
                        'six',
                        'pygments>=2.5.2',
                        'pygments-github-lexers>=0.0.3',
                        'charlockholmes',
                        'mime>=0.1.0',
                        'scanner>=0.0.4'],
      classifiers=[],
      scripts=['bin/pylinguist'])
