# Register your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ArtsAndIdeasGenre, ArtsAndIdeasEvent

# Register your models here.
#admin.site.register(Workshop)
admin.site.register(ArtsAndIdeasEvent)
admin.site.register(ArtsAndIdeasGenre)