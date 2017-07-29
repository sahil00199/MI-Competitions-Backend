#password is mimi1234

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import InformalsGenre, InformalsEvent

admin.site.register(InformalsEvent)
admin.site.register(InformalsGenre)