# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.admin import sites
from thecut.backslash.options import ModelAdmin
from .decorators import reject_unsupported_browsers


class AdminSite(sites.AdminSite):

    actions = []

    browser_requirements = {
        'microsoft internet explorer': '10',
    }

    index_template = 'backslash/index.html'

    login_template = 'backslash/login.html'

    logout_template = 'backslash/logged_out.html'

    app_index_template = 'backslash/app_index.html'

    password_change_template = 'backslash/password_change_form.html'

    password_change_done_template = 'backslash/password_change_done.html'

    unsupported_browser_template = 'backslash/unsupported_browser.html'

    def admin_view(self, view, *args, **kwargs):
        view = reject_unsupported_browsers(
            browser_requirements=self.browser_requirements,
            template_name=self.unsupported_browser_template)(view)
        return super(AdminSite, self).admin_view(view, *args, **kwargs)

    def login(self, *args, **kwargs):
        wrapper = reject_unsupported_browsers(
            browser_requirements=self.browser_requirements,
            template_name=self.unsupported_browser_template)
        return wrapper(super(AdminSite, self).login)(*args, **kwargs)

    def register(self, model_or_iterable, admin_class=None, **kwargs):
        if admin_class is None:
            admin_class = ModelAdmin
        return super(AdminSite, self).register(
            model_or_iterable, admin_class=admin_class, **kwargs)

site = AdminSite(name='backslash')
