#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup

standalone_packages = ['liblarch', 'liblarch_gtk']

for package in standalone_packages:
    setup(
      version = '0.1',
      url = 'https://live.gnome.org/liblarch',
      author = 'Liblarch team',
      author_email = 'gtg-contributors@lists.launchpad.net',
      maintainer = 'Izidor Matušov',
      maintainer_email = 'izidor.matusov@gmail.com',
      description = 'Liblarch is a python library built to easily handle data structure such are lists, trees and acyclic graphs (tree where nodes can have multiple parents)',
      license = 'LGPLv3',

      name = package,
      packages = [package],
    )
