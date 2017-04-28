# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.backslash.decorators import register, reject_unsupported_browsers
from thecut.backslash.options import ModelAdmin
from test_app.models import BackslashTestModel
from django.test.client import RequestFactory
from django.http import HttpResponse

try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


class TestRegister(TestCase):
    def test_not_modeladmin_subclass(self):
        class Useless2(object):
            pass

        with self.assertRaises(ValueError):
            @register(Useless2)
            class Useless(object):
                pass

    def test_is_modeladmin_subclass(self):
        @register(BackslashTestModel)
        class Useless(ModelAdmin):
            pass

    def test_invalid_site(self):
        class Useless2(object):
            pass

        with self.assertRaises(ValueError):
            @register(BackslashTestModel, site=Useless2)
            class Useless(ModelAdmin):
                pass


class TestRejectUnsupportedBrowsers(TestCase):
    def setUp(self):
        self.wrapper = reject_unsupported_browsers({
            'microsoft internet explorer': '10'},
            'backslash/unsupported_browser.html')

    def test_browser_is_not_supported(self):
        def always_fails_view(request):
            assert False

        view = reject_unsupported_browsers(
            browser_requirements={'microsoft internet explorer': '10'},
            template_name='backslash/unsupported_browser.html')(
            always_fails_view)

        request_factory = RequestFactory()
        request = request_factory.get('/', HTTP_USER_AGENT='Mozilla/4.0 '
            '(compatible; MSIE 6.0; Windows NT 5.1) ')  # NOQA

        response = view(request)

        self.assertEqual(response.status_code, 406)

    def test_browser_is_supported(self):

        def always_succeeds_view(request):
            html = '<html><body>Hello</body></html>'
            return HttpResponse(html)
        view = reject_unsupported_browsers(
            browser_requirements={'microsoft internet explorer': '10'},
            template_name='backslash/unsupported_browser.html')(
            always_succeeds_view)

        request_factory = RequestFactory()
        request = request_factory.get('/', HTTP_USER_AGENT='Mozilla/5.0 '
            '(compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)')  # NOQA

        response = view(request)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.content, b'<html><body>Hello</body></html>')
