# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserProfile
from django.shortcuts import render
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ParticipantDetail(APIView):
    def get_object(self, mi_number):
        try:
            return UserProfile.objects.get(mi_number=mi_number)
        except UserProfile.DoesNotExist:
            raise Http404


    def get(self, request, mi_number, format=None):
        participant = self.get_object(mi_number)
        serializer = UserSerializer(participant)
        return Response(serializer.data)


    def put(self, request, mi_number, format=None):
        participant = self.get_object(mi_number)
        serializer = UserSerializer(participant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, mi_number, format=None):
        snippet = self.get_object(mi_number)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def giveFirstThree(word):
	word = word[:3]
	ans = ""
	for letter in word:
		temp = ord(letter)
		if temp<=ord('z') and temp>=ord('a'):
			ans+=chr(temp+ord('A')-ord('a'))
		else:
			ans+=letter
	return ans

class CreateParticipant(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            datum = serializer.validated_data
            name = datum['name']
            beg = giveFirstThree(name)
            beg = "MI-"+beg
            already_there = len(UserProfile.objects.filter(mi_number__startswith = beg))
            if already_there == 0:
                end = "101"
            else:
                end = str(101+already_there)
            datum["mi_number"] = beg+"-"+end
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)