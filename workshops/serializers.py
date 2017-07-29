from rest_framework import serializers
from .models import WorkshopsGenre, WorkshopsEvent

'''
class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = "__all__"
'''


class WorkshopsEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkshopsEvent
        fields = ('name', 'description')


class WorkshopsGenreSerializer(serializers.ModelSerializer):
    events = WorkshopsEventSerializer(many=True, read_only=True)

    class Meta:
        model = WorkshopsGenre
        fields = ('name', 'description', 'events')
