from __future__ import absolute_import, unicode_literals
from django.contrib.admin.views.main import SEARCH_VAR
from django.template import Library


register = Library()


@register.inclusion_tag('backslash/search_form.html')
def search_form(cl):
    """Displays a search form for searching the list."""
    return {'cl': cl,
            'show_result_count': cl.result_count != cl.full_result_count,
            'search_var': SEARCH_VAR}
