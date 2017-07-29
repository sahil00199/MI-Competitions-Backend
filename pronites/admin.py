#password is mimi1234

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PronitesGenre, PronitesEvent

# Register your models here.
#admin.site.register(Pronite)
admin.site.register(PronitesEvent)
admin.site.register(PronitesGenre)