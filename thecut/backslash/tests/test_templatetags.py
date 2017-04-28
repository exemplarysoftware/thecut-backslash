# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.backslash.templatetags.backslash_list import search_form
from django.contrib.admin.views.main import SEARCH_VAR

try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


class TestBackslashList(TestCase):
    def test_search_form_results_match(self):
        cl = mock.MagicMock()
        cl.result_count = 1
        cl.full_result_count = 1
        ret = search_form(cl)
        self.assertIs(ret['cl'], cl)
        self.assertFalse(ret['show_result_count'])
        self.assertIs(ret['search_var'], SEARCH_VAR)

    def test_search_form_results_dont_match(self):
        cl = mock.MagicMock()
        cl.result_count = 1
        cl.full_result_count = 2
        ret = search_form(cl)
        self.assertIs(ret['cl'], cl)
        self.assertTrue(ret['show_result_count'])
        self.assertIs(ret['search_var'], SEARCH_VAR)
