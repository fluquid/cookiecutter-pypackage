#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from pkgutil import walk_packages


def find_packages(path):
    return [
        name for _, name, is_pkg in walk_packages([path]) if is_pkg
    ]


def read_file(filename):
    with open(filename) as fp:
        return fp.read()


requirements = [
    # TODO: put package requirements here
]

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=read_file('README.rst') + '\n\n' + read_file('HISTORY.rst'),
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
