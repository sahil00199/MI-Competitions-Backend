from rest_framework import serializers
from .models import Workshop, WorkshopsGenre, WorkshopsEvent

class WorkshopSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workshop
		fields = "__all__"

class WorkshopsGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkshopsGenre
		fields = "__all__"

class WorkshopsEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkshopsEvent
		fields = "__all__"