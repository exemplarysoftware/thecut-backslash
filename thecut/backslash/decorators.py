# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def register(*models, **kwargs):

    from thecut.backslash import ModelAdmin
    from thecut.backslash.sites import site, AdminSite

    def _model_admin_wrapper(admin_class):
        admin_site = kwargs.pop('site', site)

        if not isinstance(admin_site, AdminSite):
            raise ValueError('site must subclass AdminSite')

        if not issubclass(admin_class, ModelAdmin):
            raise ValueError('Wrapped class must subclass ModelAdmin.')

        admin_site.register(models, admin_class=admin_class)

        return admin_class

    return _model_admin_wrapper
