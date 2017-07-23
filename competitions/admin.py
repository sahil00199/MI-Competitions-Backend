from django.contrib import admin
from .models import GroupEvent, IndividualEvent, Genre, Competition, Group
from .forms import ImprovedModelForm



class GroupAdmin(ImprovedModelForm):
	raw_id_fields = ('event',"members",)

admin.site.register(GroupEvent)
admin.site.register(IndividualEvent)
admin.site.register(Genre)
admin.site.register(Competition)
admin.site.register(Group,GroupAdmin)

