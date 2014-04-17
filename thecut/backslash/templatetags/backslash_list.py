from __future__ import absolute_import, unicode_literals
from django.contrib.admin.templatetags.admin_list import search_form
from django.template import Library


register = Library()


search_form = register.include_tag(search_form, 'backslash/search_form.html')
