===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
        :target: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

{%- if cookiecutter.use_codecov|lower == 'y' %}
.. image:: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
{%- endif %}

{%- if cookiecutter.use_landscape|lower == 'y' %}
.. image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/master/landscape.svg?style=flat
    :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/master
    :alt: Code Quality Status
{%- endif %}

{%- if cookiecutter.use_requiresio|lower == 'y' %}
.. image:: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/requirements/?branch=master
{%- endif %}

{{ cookiecutter.project_short_description}}

* Free software: MIT license
* Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.org.

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
