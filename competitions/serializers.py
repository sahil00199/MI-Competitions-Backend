from rest_framework import serializers
from .models import GroupEvent, IndividualEvent, CompetitionsGenre, Group

class IndividualEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEvent
        fields = ('name', 'genre', 'about', 'rules', 'prizes', 'multicity_details',)

'''
class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"
'''

class CompetitionsGenreSerializer(serializers.ModelSerializer):
    events = IndividualEventSerializer(many=True, read_only=True)
    class Meta:
        model = CompetitionsGenre
        fields = ('name','description','events')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class GroupEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupEvent
        fields = ('name', 'genre', 'about', 'rules', 'prizes', 'multicity_details',)

