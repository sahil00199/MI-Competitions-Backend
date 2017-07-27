from django.contrib import admin
from .models import GroupEvent, IndividualEvent, Genre, Competition, Group
from participant_api.models import UserProfile
from .forms import ImprovedModelForm
from django.contrib.admin.widgets import ManyToManyRawIdWidget

class MembersInline(admin.TabularInline):
    model = Group.members.through
    verbose_name = u"Member"
    verbose_name_plural = u"Members"
    extra = 0
        

class GroupAdmin(admin.ModelAdmin):
    inlines = (
       MembersInline,
    )
    exclude = ("members",)

class GroupsInline(admin.TabularInline):
    model = IndividualEvent.groups_part.through
    verbose_name = u"Group"
    verbose_name_plural = u"Groups"
    extra = 0 
        

class IndividualEventAdmin(admin.ModelAdmin):
    #filter_horizontal = ('groups_part',)
    exclude = ("groups_part","participants")
    inlines = (
       GroupsInline,
    )  

admin.site.register(GroupEvent)
admin.site.register(IndividualEvent,IndividualEventAdmin)
admin.site.register(Genre)
admin.site.register(Competition)
admin.site.register(Group,GroupAdmin)

