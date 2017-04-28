# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.backslash.options import ModelAdmin

try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


class TestModelAdmin(TestCase):
    def test_model_initialisation(self):
        model = mock.MagicMock()
        meta = mock.MagicMock()
        model._meta = meta
        meta.app_label = 'app'
        meta.object_name = 'model'
        admin_site = mock.MagicMock()

        m = ModelAdmin(model, admin_site)
        self.assertEqual(m.add_form_template,  [
            'backslash/app/model/change_form.html',
            'backslash/app/change_form.html',
            'backslash/change_form.html'])
        self.assertEqual(m.change_form_template, [
            'backslash/app/model/change_form.html',
            'backslash/app/change_form.html',
            'backslash/change_form.html'])
        self.assertEqual(m.change_list_template, [
            'backslash/app/model/change_list.html',
            'backslash/app/change_list.html',
            'backslash/change_list.html'])
        self.assertEqual(m.delete_confirmation_template, [
            'backslash/app/model/delete_confirmation.html',
            'backslash/app/delete_confirmation.html',
            'backslash/delete_confirmation.html'])
        self.assertEqual(m.delete_selected_confirmation_template, [
            'backslash/app/model/delete_selected_confirmation.html',
            'backslash/app/delete_selected_confirmation.html',
            'backslash/delete_selected_confirmation.html'])
        self.assertEqual(m.object_history_template, [
            'backslash/app/model/object_history.html',
            'backslash/app/object_history.html',
            'backslash/object_history.html'])
