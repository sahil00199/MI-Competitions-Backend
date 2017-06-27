from django.contrib import admin
from .models import GroupEvent, IndividualEvent, Genre, Competition, Group

admin.site.register(GroupEvent)
admin.site.register(IndividualEvent)
admin.site.register(Genre)
admin.site.register(Competition)
admin.site.register(Group)