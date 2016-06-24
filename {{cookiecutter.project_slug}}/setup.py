#!/usr/bin/env python
# -*- coding: utf-8 -*-
{% if cookiecutter.use_cython == 'y' -%}
import glob
import os

{% endif -%}
from pkgutil import walk_packages
from setuptools import setup
{%- if cookiecutter.use_cython == 'y' %}
from setuptools.extension import Extension
from setuptools.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):

    def finalize_options(self):
        from Cython.Build import cythonize
        self.distribution.ext_modules[:] = cythonize(
            self.distribution.ext_modules,
            compiler_directives={'embedsignature': True},
        )
        _build_ext.finalize_options(self)


def find_extensions(dir, pattern, **kwargs):
    for pkgname in find_packages(dir):
        pkgdir = os.path.join(dir, pkgname.replace('.', '/'))
        for path in glob.glob(os.path.join(pkgdir, pattern)):
            modname, _ = os.path.splitext(os.path.basename(path))
            extname = '%s.%s' % (pkgname, modname)
            yield Extension(extname, [path], **kwargs)
{%- endif %}


def find_packages(path):
    # This method returns packages and subpackages as well.
    for _, name, is_pkg in walk_packages([path]):
        if is_pkg:
            yield name


def read_file(filename):
    with open(filename) as fp:
        return fp.read()


requirements = [
    # TODO: put package requirements here
]

requirements_setup = [
{%- if cookiecutter.use_cython == 'y' %}
        'cython>=0.24',
{%- endif %}
]

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=read_file('README.rst') + '\n\n' + read_file('HISTORY.rst'),
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=list(find_packages('src')),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
{%- if cookiecutter.use_cython == 'y' %}
    zip_safe=False,
{%- endif %}
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
{%- if cookiecutter.use_cython == 'y' %}
    ext_modules=list(find_extensions('src', '*.pyx')),
    cmdclass={'build_ext': build_ext},
{%- endif %}
    setup_requires=requirements_setup,
)
