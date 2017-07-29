#password is mimi1234

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ProshowsGenre, ProshowsEvent

# Register your models here.
#admin.site.register(Proshow)
admin.site.register(ProshowsEvent)
admin.site.register(ProshowsGenre)