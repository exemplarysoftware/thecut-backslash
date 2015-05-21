# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.admin.apps import AdminConfig


class AppConfig(AdminConfig):

    label = 'backslash'

    name = 'thecut.backslash'
