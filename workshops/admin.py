#password is mimi1234

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import WorkshopsGenre, WorkshopsEvent

# Register your models here.
#admin.site.register(Workshop)
admin.site.register(WorkshopsEvent)
admin.site.register(WorkshopsGenre)