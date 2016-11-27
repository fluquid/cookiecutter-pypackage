#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
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
    return [name for _, name, is_pkg in walk_packages([path]) if is_pkg]


def read_file(filename):
    with io.open(filename) as fp:
        return fp.read().strip()


def read_rst(filename):
    # Ignore unsupported directives by pypi.
    content = read_file(filename)
    return ''.join(line for line in io.StringIO(content)
                   if not line.startswith('.. comment::'))


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup_attrs = dict(
    name='{{ cookiecutter.project_slug }}',
    version=read_file('VERSION'),
    description="{{ cookiecutter.project_short_description }}",
    long_description=read_rst('README.rst') + '\n\n' + read_rst('HISTORY.rst'),
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=list(find_packages('src')),
    package_dir={'': 'src'},
    setup_requires=read_requirements('requirements-setup.txt'),
    install_requires=read_requirements('requirements-install.txt'),
    include_package_data=True,
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
)


if __name__ == "__main__":
    setup(setup_attrs)
