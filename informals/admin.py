#password is mimi1234

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import InformalsGenre, Informal, InformalsEvent

# Register your models here.
admin.site.register(Informal)
admin.site.register(InformalsEvent)
admin.site.register(InformalsGenre)