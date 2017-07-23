# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import ProniteSerializer, PronitesGenreSerializer,PronitesEventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PronitesGenre, Pronite, PronitesEvent

class Pronite1(APIView): #return description of entire ProniteS
    def get(self, request, format=None):
        serializer = ProniteSerializer(Pronite.objects.get(pk=1))
        #serializer += PronitesGenreSerializer(PronitesGenre.objects.all(), many = True)
        serializer.data["asdfg"] = "asdf"
        return Response(serializer.data)

class PronitesGenreList(APIView): #return all the genres under ProniteS and create a new genre
    def get(self, request, format=None):
        genres = PronitesGenre.objects.all()
        serializer = PronitesGenreSerializer(genres, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = PronitesGenreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class PronitesGenre1(APIView): #return info about a particular genre
    def get(self, request, genre_id, format=None):
        genre=PronitesGenre.objects.get(pk = genre_id)
        serializer = PronitesGenreSerializer(genre)
        return Response(serializer.data)

class PronitesEventList(APIView): #returns all events under a particular genre
    def get(self, request, genre_id, format=None):
        events = PronitesEvent.objects.all().filter(genre = genre_id)
        serializer = PronitesEventSerializer(events, many=True)
        return Response(serializer.data)

class PronitesEvent1(APIView): #return info about a particular event
    def get(self, request, event_id, format=None):
        event = PronitesEvent.objects.get(pk = event_id)
        serializer = PronitesEventSerializer(event)
        return Response(serializer.data)