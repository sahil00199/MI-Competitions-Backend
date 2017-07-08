# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ProshowsGenre(models.Model):
	genre = models.CharField(max_length = 100)
	description = models.TextField()

	def __str__(self):
		return self.genre

class Proshow(models.Model):
	description = models.TextField()
	genres = ProshowsGenre.objects.all()

class ProshowsEvent(models.Model):
	name = models.CharField(max_length = 100)
	genre = models.ForeignKey(ProshowsGenre, on_delete = models.CASCADE)
	description = models.TextField()

	def __str__(self):
		return self.name