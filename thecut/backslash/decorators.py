# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.http import HttpResponseForbidden
from django.template import loader
from pkg_resources import parse_version
import httpagentparser
import wrapt


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


def reject_unsupported_browsers(browser_requirements, template_name):

    @wrapt.decorator
    def _wrapper(view, instance, args, kwargs):
        if kwargs.get('request'):
            request = kwargs['request']
        else:
            request, args = args[0], args[1:]

        unsupported_browser = False
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        browser = httpagentparser.detect(user_agent).get('browser', {})
        browser_name = browser.get('name', '').lower()

        if browser_name in browser_requirements and browser.get('version'):
            required_version = parse_version(
                browser_requirements[browser_name])
            if required_version > parse_version(browser['version']):
                unsupported_browser = True

        if unsupported_browser:
            template = loader.get_template(template_name)
            return HttpResponseForbidden(template.render(request=request))

        return view(request, *args, **kwargs)

    return _wrapper
