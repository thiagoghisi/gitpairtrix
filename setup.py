# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gitpairtrix',
    version='0.0.1',
    description='Command line tool to generate pair programming matrix from a git repo',
    long_description=readme,
    author='Thiago Ghisi',
    author_email='thiago.ghisi@gmail.com',
    url='https://github.com/thiagoghisi/gitpairtrix',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

