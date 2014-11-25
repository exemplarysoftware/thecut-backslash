# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.admin.filters import (
    AllValuesFieldListFilter, BooleanFieldListFilter, ChoicesFieldListFilter,
    DateFieldListFilter, FieldListFilter, ListFilter, RelatedFieldListFilter,
    SimpleListFilter)
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.contrib.admin.options import (HORIZONTAL, VERTICAL, StackedInline,
                                          TabularInline)
from thecut.backslash.decorators import register
from thecut.backslash.options import ModelAdmin
from thecut.backslash.sites import AdminSite, site


try:
    from django.utils.module_loading import autodiscover_modules
except ImportError:  # Pre Django 1.7 compatibility
    from .backports.module_loading import autodiscover_modules


__all__ = ['ACTION_CHECKBOX_NAME', 'AdminSite', 'AllValuesFieldListFilter',
           'autodiscover', 'BooleanFieldListFilter', 'ChoicesFieldListFilter',
           'DateFieldListFilter', 'FieldListFilter', 'HORIZONTAL',
           'ListFilter', 'ModelAdmin', 'register', 'RelatedFieldListFilter',
           'SimpleListFilter', 'site', 'StackedInline', 'TabularInline',
           'VERTICAL']


def autodiscover():
    autodiscover_modules('backslash', register_to=site)


default_app_config = 'thecut.backslash.apps.AppConfig'
