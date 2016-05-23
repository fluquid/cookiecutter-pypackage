#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_package }}
----------------------------------

Tests for `{{ cookiecutter.project_package }}` module.
"""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}

from {{ cookiecutter.project_package }} import {{ cookiecutter.project_package }}

{% if cookiecutter.use_pytest == 'y' -%}
class Test{{ cookiecutter.project_package|title }}(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass
{% else %}
class Test{{ cookiecutter.project_package|title }}(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
{%- endif %}
