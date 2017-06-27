from rest_framework import serializers
from .models import Informal, InformalsEvent, InformalsGenre

class InformalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informal
        fields = "__all__"

class InformalsGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformalsGenre
        fields = "__all__"

class InformalsEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformalsEvent
        fields = "__all__"