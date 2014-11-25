# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule
import copy


def autodiscover_modules(*args, **kwargs):
    # Heavily modified from Django 1.7's ``autodiscover_modules`` function,
    # which uses the new app config registry.
    from django.conf import settings

    register_to = kwargs.get('register_to')

    for app in settings.INSTALLED_APPS:
        app_module = import_module(app)

        # Attempt to import the app's module.
        try:
            if register_to:
                before_import_registry = copy.copy(register_to._registry)

            for module_to_search in args:
                import_module('{app}.{module}'.format(app=app,
                                                      module=module_to_search))
        except:
            # Reset the model registry to the state before the last import as
            # this import will have to reoccur on the next request and this
            # could raise NotRegistered and AlreadyRegistered exceptions
            # (see #8245).
            if register_to:
                register_to._registry = before_import_registry

            # Decide whether to bubble up this error. If the app just
            # doesn't have an admin module, we can ignore the error
            # attempting to import it, otherwise we want it to bubble up.
            if module_has_submodule(app_module, module_to_search):
                raise
