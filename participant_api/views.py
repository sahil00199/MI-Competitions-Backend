# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserProfile, City, College
from django.shortcuts import render
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ParticipantDetail(APIView):
    def get_object(self, fb_id):
        try:
            return UserProfile.objects.get(fb_id=fb_id)
        except UserProfile.DoesNotExist:
            raise Http404


    def get(self, request, fb_id, format=None):
        participant = self.get_object(fb_id)
        serializer = UserSerializer(participant)
        return Response(serializer.data)


    def put(self, request, fb_id, format=None):
        participant = self.get_object(fb_id)
        serializer = UserSerializer(participant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, fb_id, format=None):
        snippet = self.get_object(fb_id)
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
        info = request.data
        try:
            city = City.objects.get(city_name=request.data['present_city'])
            #new_user.present_city=(city)
        except:
            city = City.objects.create(city_name=request.data['present_city'])
            #new_user.present_city=(new_city)
        try:
            college = College.objects.get(college_name=request.data['present_college'])
            #new_user.present_college=(college)
        except:
            college = College.objects.create(college_name=request.data['present_college'], located_city=city)
            #new_user.present_college=(new_college)
        print city.city_name
        name = request.data['name']
        beg = giveFirstThree(name)
        beg = "MI-"+beg
        already_there = len(UserProfile.objects.filter(mi_number__startswith=beg))
        if already_there == 0:
            end = "101"
        else:
            end = str(101+already_there)
        #try:
        new_user = UserProfile.objects.create(name=request.data['name'], postal_address=request.data['postal_address'], mobile_number=request.data['mobile_number'], whatsapp_number=request.data['whatsapp_number'], zip_code=request.data['zip_code'], year_of_study=request.data['year_of_study'], fb_id=request.data['fb_id'], email=request.data['email'], present_city=city, present_college=college, mi_number=(beg+"-"+end))
        #except:
        '''    #return Response({"details":"Invalid"}, status = status.HTTP_400_BAD_REQUEST)
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

        '''
