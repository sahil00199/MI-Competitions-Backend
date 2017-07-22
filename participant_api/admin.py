# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserProfile, City, College
from django.contrib import admin

# Register your models here.ser
class UserProfileAdmin(admin.ModelAdmin):
    list_filter=('present_city','present_college')
    list_display=('name','present_city','present_college')

admin.site.register(City)
admin.site.register(College)
admin.site.register(UserProfile,UserProfileAdmin)
      