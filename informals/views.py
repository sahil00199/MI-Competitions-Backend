# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import InformalSerializer, InformalsGenreSerializer,InformalsEventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InformalsGenre, Informal, InformalsEvent

class Informal1(APIView): #return description of entire INFORMALS
    def get(self, request, format=None):
        serializer = InformalSerializer(Informal.objects.get(pk=1))
        #serializer += InformalsGenreSerializer(InformalsGenre.objects.all(), many = True)
        #serializer.data["asdfg"] = "asdf"
        return Response(serializer.data)

class InformalsGenreList(APIView): #return all the genres under INFORMALS and create a new genre
    def get(self, request, format=None):
        genres = InformalsGenre.objects.all()
        serializer = InformalsGenreSerializer(genres, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = InformalsGenreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class InformalsGenre1(APIView): #return info about a particular genre
    def get(self, request, genre_id, format=None):
        genre=InformalsGenre.objects.get(pk = genre_id)
        serializer = InformalsGenreSerializer(genre)
        return Response(serializer.data)

class InformalsEventList(APIView): #returns all events under a particular genre
    def get(selfs, request, genre_id, format=None):
        events = InformalsEvent.objects.all().filter(genre = genre_id)
        serializer = InformalsEventSerializer(events, many=True)
        return Response(serializer.data)

class InformalsEvent1(APIView): #return info about a particular event
    def get(self, request, event_id, format=None):
        event = InformalsEvent.objects.get(pk = event_id)
        serializer = InformalsEventSerializer(event)
        return Response(serializer.data)