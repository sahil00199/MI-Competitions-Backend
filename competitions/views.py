from django.shortcuts import render
from .models import Group, Genre, GroupEvent, IndividualEvent, Competition
from participant_api.models import UserProfile
from .serializers import IndividualEventSerializer, GroupSerializer, GroupEventSerializer, GenreSerializer
from .serializers import GeneralInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class IndividualCompetition(APIView): #add participant to an individual competition and return info on individual competition
    def post(self, request, event_id, format = None):
        participant = request.data['participant']
        event = IndividualEvent.objects.get(pk=event_id)
        obj= Group.objects.latest('id')
        try:
            group_leader = UserProfile.objects.get(mi_number=participant[0])
            group = Group.objects.create(event=event, team_id=obj.team_id+1, name=group_leader.mi_number)
        except:
            return Response({"details":"MI Number invalid"}, status = status.HTTP_400_BAD_REQUEST)
        
        for user in participant:
            try:
                event.participants.add(UserProfile.objects.get(mi_number=user))
                group.members.add(UserProfile.objects.get(mi_number=user))
            except:
                return Response({"details":"MI Number invalid"}, status = status.HTTP_400_BAD_REQUEST)
            event.groups_part.add(group)
        serializer = IndividualEventSerializer(event)
        group_serializer = GroupSerializer(group)
        return Response({"details":"success", "default":group_serializer.data}, status=status.HTTP_201_CREATED)
    
    def get(self, request, event_id, format = None):
        serializer = IndividualEventSerializer(IndividualEvent.objects.get(pk = event_id))
        return Response(serializer.data)

class IndividualEventsForUser(APIView): #given fb_id, find all individual competitions registered for
    def get(self, request, fb_id, format = None):
        try:
            user = UserProfile.objects.get(fb_id = fb_id)
            events = user.individualevent_set.all()
            serializer = IndividualEventSerializer(events, many = True)
            return Response(serializer.data)
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)

class GroupCompetition(APIView): #add a group of participants to a group competition and return info on grp competition
    def post(self, request, event_id, format = None):
        participant_list = request.data['participants']
        name = request.data['name']
        grp = Group()
        grp.name = name
        grp.save()
        prev = participant_list.find("MI-")
        mi_number = participant_list[prev:max(-1, participant_list.find("MI-", prev+1)-1)]
        while participant_list.find("MI-", prev) != -1:
            user = UserProfile.objects.get(mi_number = mi_number)
            grp.members.add(user)
            prev = participant_list.find("MI-", prev+1)
            mi_number = participant_list[prev:max(-1, participant_list.find("MI-", prev+1)-1)]
        event = GroupEvent.objects.get(pk = event_id)
        event.participants.add(grp)
        serializer = GroupEventSerializer(event)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    def get(self, request, event_id, format = None):
        serializer = GroupEventSerializer(GroupEvent.objects.get(pk = event_id))
        return Response(serializer.data )

class GroupEventsForUser(APIView):
    def get(self, request, fb_id, format = None):
        try:
            user = UserProfile.objects.get(fb_id = fb_id)
            groups = user.group_set.all()
            events = GroupEvent.objects.filter(participants__in = groups)
            serializer = GroupEventSerializer(events, many = True)
            return Response(serializer.data)
        except:
            return Response({}, status = status.HTTP_400_BAD_REQUEST)

class GeneralInfo(APIView): #return general info about competitions
    def get(self, request, format = None):
        return Response(GeneralInfoSerializer(Competition.objects.get(pk=1)).data)

class AllGenres(APIView): #return list of genres
    def get(self, request, format=None):
        serializer = GenreSerializer(Genre.objects.all(), many = True)
        return Response(serializer.data)

class IndividualEventsUnderGenre(APIView): #return all individual events under a genre
    def get(self, request, genre_id, format = None):
        events = IndividualEvent.objects.all().filter(genre = genre_id)
        serializer = IndividualEventSerializer(events, many = True)
        return Response(serializer.data)

class GroupEventsUnderGenre(APIView): #return all group events under a genre
    def get(self, request, genre_id, format=None):
        events = GroupEvent.objects.all().filter(genre=genre_id)
        serializer = GroupEventSerializer(events, many=True)
        return Response(serializer.data)

class GenreInfo(APIView): #return info about a particular genre
    def get(self, request, genre_id, format = None):
        serializer = GenreSerializer(Genre.objects.get(pk = genre_id))
        return Response(serializer.data)

class AllEvents(APIView):
    def get(self, request, format=None):
        serializer = IndividualEventSerializer(IndividualEvent.objects.all(), many = True)
        return Response(serializer.data)