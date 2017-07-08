from rest_framework import serializers
from .models import Pronite, PronitesGenre, PronitesEvent

class ProniteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pronite
		fields = "__all__"

class PronitesGenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = PronitesGenre
		fields = "__all__"

class PronitesEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = PronitesEvent
		fields = "__all__"