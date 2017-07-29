from rest_framework import serializers
from .models import PronitesGenre, PronitesEvent

'''
class ProniteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pronite
		fields = "__all__"
'''

class PronitesEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PronitesEvent
        fields = ('name','description')

class PronitesGenreSerializer(serializers.ModelSerializer):
    events = PronitesEventSerializer(many=True, read_only=True)
    class Meta:
		model = PronitesGenre
		fields = ('name','description','events')
