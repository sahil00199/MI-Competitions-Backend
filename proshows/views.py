# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import ProshowsGenreSerializer,ProshowsEventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProshowsGenre, ProshowsEvent

class Proshows(APIView): #return all the genres under ProshowS and create a new genre
    def get(self, request, format=None):
        genres = ProshowsGenre.objects.all()
        serializer = ProshowsGenreSerializer(genres, many = True)
        return Response(serializer.data)

'''
class Proshow1(APIView): #return description of entire ProshowS
    def get(self, request, format=None):
        serializer = ProshowSerializer(Proshow.objects.get(pk=1))
        #serializer += ProshowsGenreSerializer(ProshowsGenre.objects.all(), many = True)
        serializer.data["asdfg"] = "asdf"
        return Response(serializer.data)

class ProshowsGenreList(APIView): #return all the genres under ProshowS and create a new genre
    def get(self, request, format=None):
        genres = ProshowsGenre.objects.all()
        serializer = ProshowsGenreSerializer(genres, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ProshowsGenreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class ProshowsGenre1(APIView): #return info about a particular genre
    def get(self, request, genre_id, format=None):
        genre=ProshowsGenre.objects.get(pk = genre_id)
        serializer = ProshowsGenreSerializer(genre)
        return Response(serializer.data)

class ProshowsEventList(APIView): #returns all events under a particular genre
    def get(self, request, genre_id, format=None):
        events = ProshowsEvent.objects.all().filter(genre = genre_id)
        serializer = ProshowsEventSerializer(events, many=True)
        return Response(serializer.data)

class ProshowsEvent1(APIView): #return info about a particular event
    def get(self, request, event_id, format=None):
        event = ProshowsEvent.objects.get(pk = event_id)
        serializer = ProshowsEventSerializer(event)
        return Response(serializer.data)

class ProshowsEventAll(APIView):
    def get(self, request, format=None):
        serializer = ProshowsEventSerializer(ProshowsEvent.objects.all(), many=True)
        return Response(serializer.data)
'''
