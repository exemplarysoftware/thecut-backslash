# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import warnings


def applist(*args, **kwargs):
    """Deprecated. Instead use custom ``backslash/_menu.html`` template."""
    warnings.warn('Backslash context_processors have been deprecated, please ' \
        'remove from your TEMPLATE_CONTEXT_PROCESSORS setting.',
        DeprecationWarning, stacklevel=2)
    return {}


def model_list(*args, **kwargs):
    """Deprecated. Instead use custom ``backslash/_menu.html`` template."""
    warnings.warn('Backslash context_processors have been deprecated, please ' \
        'remove from your TEMPLATE_CONTEXT_PROCESSORS setting.',
        DeprecationWarning, stacklevel=2)
    return {}

