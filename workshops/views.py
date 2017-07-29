# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import WorkshopsGenreSerializer,WorkshopsEventSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WorkshopsGenre, WorkshopsEvent

class Workshops(APIView): #return all the genres under WorkshopS and create a new genre
    def get(self, request, format=None):
        genres = WorkshopsGenre.objects.all()
        serializer = WorkshopsGenreSerializer(genres, many = True)
        return Response(serializer.data)
'''
class Workshop1(APIView): #return description of entire WorkshopS
    def get(self, request, format=None):
        serializer = WorkshopSerializer(Workshop.objects.get(pk=1))
        #serializer += WorkshopsGenreSerializer(WorkshopsGenre.objects.all(), many = True)
        serializer.data["asdfg"] = "asdf"
        return Response(serializer.data)

class WorkshopsGenreList(APIView): #return all the genres under WorkshopS and create a new genre
    def get(self, request, format=None):
        genres = WorkshopsGenre.objects.all()
        serializer = WorkshopsGenreSerializer(genres, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = WorkshopsGenreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class WorkshopsGenre1(APIView): #return info about a particular genre
    def get(self, request, genre_id, format=None):
        genre=WorkshopsGenre.objects.get(pk = genre_id)
        serializer = WorkshopsGenreSerializer(genre)
        return Response(serializer.data)

class WorkshopsEventList(APIView): #returns all events under a particular genre
    def get(self, request, genre_id, format=None):
        events = WorkshopsEvent.objects.all().filter(genre = genre_id)
        serializer = WorkshopsEventSerializer(events, many=True)
        return Response(serializer.data)

class WorkshopsEvent1(APIView): #return info about a particular event
    def get(self, request, event_id, format=None):
        event = WorkshopsEvent.objects.get(pk = event_id)
        serializer = WorkshopsEventSerializer(event)
        return Response(serializer.data)
'''