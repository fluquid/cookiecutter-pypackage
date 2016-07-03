{% set title_line = "=" * cookiecutter.project_name|length -%}
{{ title_line }}
{{ cookiecutter.project_name }}
{{ title_line }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
        :target: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

{% if cookiecutter.use_codecov|lower == 'y' -%}
.. image:: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

{% endif -%}

{% if cookiecutter.use_landscape|lower == 'y' -%}
.. image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/master
    :alt: Code Quality Status

{% endif -%}

{% if cookiecutter.use_requiresio|lower == 'y' -%}
.. image:: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/requirements/?branch=master

{% endif -%}

{{ cookiecutter.project_short_description}}

* Free software: MIT license
* Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.org.
* Python versions: 2.7, 3.4+

Features
--------

FIXME

Quickstart
----------

FIXME

Credits
-------

This package was created with Cookiecutter_ and the `rolando/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`rolando/cookiecutter-pypackage`: https://github.com/rolando/cookiecutter-pypackage
