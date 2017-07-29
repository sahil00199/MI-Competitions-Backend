from rest_framework import serializers
from .models import ProshowsGenre, ProshowsEvent

'''
class ProshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proshow
        fields = "__all__"
'''


class ProshowsEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProshowsEvent
        fields = ('name', 'description')


class ProshowsGenreSerializer(serializers.ModelSerializer):
    events = ProshowsEventSerializer(many=True, read_only=True)

    class Meta:
        model = ProshowsGenre
        fields = ('name', 'description', 'events')
