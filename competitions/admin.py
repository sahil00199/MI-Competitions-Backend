from django.contrib import admin
from .models import GroupEvent, IndividualEvent, Genre, Competition, Group
from django import forms

admin.site.register(GroupEvent)
#admin.site.register(IndividualEvent)
admin.site.register(Genre)
admin.site.register(Competition)
admin.site.register(Group)

class IndividualEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IndividualEventForm, self).__init__(*args, **kwargs)
        wtf = self.instance.participants.all()
        w = self.fields['participants'].widget
        choices = []
        for choice in wtf:
            choices.append((choice.id, choice.name))
        w.choices = choices

class IndividualEventAdmin(admin.ModelAdmin):
    form = IndividualEventForm

admin.site.register(IndividualEvent, IndividualEventAdmin)