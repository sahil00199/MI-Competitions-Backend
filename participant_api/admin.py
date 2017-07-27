# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserProfile, City, College
from django.contrib import admin

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    exclude = ("mi_number","fb_id")
    list_display = ('name', 'mobile_number','present_college','present_city')


admin.site.register(City)
admin.site.register(College)
admin.site.register(UserProfile,UserProfileAdmin)