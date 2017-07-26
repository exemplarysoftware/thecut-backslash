# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        super(ModelAdmin, self).__init__(*args, **kwargs)
        app_label = self.model._meta.app_label
        model_name = self.model._meta.object_name.lower()

        self.add_form_template = self.add_form_template or [
            'backslash/{app}/{model}/change_form.html'.format(
                app=app_label, model=model_name),
            'backslash/{app}/change_form.html'.format(app=app_label),
            'backslash/change_form.html']

        self.change_form_template = self.change_form_template or [
            'backslash/{app}/{model}/change_form.html'.format(
                app=app_label, model=model_name),
            'backslash/{app}/change_form.html'.format(app=app_label),
            'backslash/change_form.html']

        self.change_list_template = self.change_list_template or [
            'backslash/{app}/{model}/change_list.html'.format(
                app=app_label, model=model_name),
            'backslash/{app}/change_list.html'.format(app=app_label),
            'backslash/change_list.html']

        self.delete_confirmation_template = \
            self.delete_confirmation_template or [
            'backslash/{app}/{model}/delete_confirmation.html'.format(
                app=app_label, model=model_name),
            'backslash/{app}/delete_confirmation.html'.format(app=app_label),
            'backslash/delete_confirmation.html']  # NOQA

        self.delete_selected_confirmation_template = \
            self.delete_selected_confirmation_template or [
            'backslash/{app}/{model}/delete_selected_confirmation.html'.format(
                app=app_label, model=model_name),
            'backslash/{app}/delete_selected_confirmation.html'.format(
                app=app_label),
            'backslash/delete_selected_confirmation.html']  # NOQA

        self.object_history_template = self.object_history_template or [
            'backslash/{app}/{model}/object_history.html'.format(
                app=app_label, model=model_name),
            'backslash/{app}/object_history.html'.format(app=app_label),
            'backslash/object_history.html']
