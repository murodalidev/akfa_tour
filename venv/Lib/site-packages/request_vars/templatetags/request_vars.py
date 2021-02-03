from __future__ import absolute_import

from django import template

from request_vars.utils import get_variable


try:
    from django_jinja import library
except ImportError:  # pragma: no cover
    library = None


register = template.Library()

register.simple_tag(get_variable)

if library:
    library.global_function(get_variable)
