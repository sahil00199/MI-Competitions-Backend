from rest_framework import serializers
from .models import Proshow, ProshowsGenre, ProshowsEvent

class ProshowSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proshow
		fields = "__all__"

class ProshowsGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProshowsGenre
		fields = "__all__"

class ProshowsEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProshowsEvent
		fields = "__all__"