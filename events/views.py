# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response

from competitions.serializers import CompetitionsGenreSerializer
from proshows.serializers import ProshowsGenreSerializer
from workshops.serializers import WorkshopsGenreSerializer
from pronites.serializers import PronitesGenreSerializer
from informals.serializers import InformalsGenreSerializer
from artsandideas.serializers import ArtsAndIdeasGenreSerializer

from competitions.models import CompetitionsGenre
from proshows.models import ProshowsGenre
from workshops.models import WorkshopsGenre
from pronites.models import PronitesGenre
from informals.models import InformalsGenre
from artsandideas.models import ArtsAndIdeasGenre


class Events(APIView):
    def get(self, request, format=None):
        competitionsgenres = CompetitionsGenre.objects.all()
        proshowsgenres = ProshowsGenre.objects.all()
        workshopsgenres = WorkshopsGenre.objects.all()
        pronitesgenres = PronitesGenre.objects.all()
        informalsgenres = InformalsGenre.objects.all()
        artsandideasgenres = ArtsAndIdeasGenre.objects.all()
        competitionserializer = CompetitionsGenreSerializer(competitionsgenres, many = True)
        proshowserializer = ProshowsGenreSerializer(proshowsgenres, many = True)
        workshopserializer = WorkshopsGenreSerializer(workshopsgenres, many = True)
        proniteserializer = PronitesGenreSerializer(pronitesgenres, many = True)
        informalserializer = InformalsGenreSerializer(informalsgenres, many = True)
        artsandideaserializer = ArtsAndIdeasGenreSerializer(artsandideasgenres, many = True)

        return Response({
            "competitions": competitionserializer.data,
            "proshows": proshowserializer.data,
            "workshops": workshopserializer.data,
            "pronites": proniteserializer.data,
            "informals": informalserializer.data,
            "artsandideas": artsandideaserializer.data
            })