from rest_framework import serializers
from .models import InformalsEvent, InformalsGenre
from pronites.models import PronitesGenre
from pronites.serializers import PronitesGenreSerializer

class InformalsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformalsEvent
        fields = ('name','description')

class InformalsGenreSerializer(serializers.ModelSerializer):
    events = InformalsEventSerializer(many=True, read_only=True)
    class Meta:
        model = InformalsGenre
        fields = ('name','description','events')
