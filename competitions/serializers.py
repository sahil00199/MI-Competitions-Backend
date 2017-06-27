from rest_framework import serializers
from .models import GroupEvent, IndividualEvent, Genre, Group, Competition

class IndividualEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEvent
        fields = ('name', 'genre', 'about', 'rules', 'prizes', 'multicity_details',)

class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class GroupEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupEvent
        fields = ('name', 'genre', 'about', 'rules', 'prizes', 'multicity_details',)
