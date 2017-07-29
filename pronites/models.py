# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PronitesGenre(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()

	def __str__(self):
		return self.name

'''
class Pronite(models.Model):
	description = models.TextField()
	genres = PronitesGenre.objects.all()
'''

class PronitesEvent(models.Model):
	name = models.CharField(max_length = 100)
	genre = models.ForeignKey(PronitesGenre, related_name='events', on_delete = models.CASCADE)
	description = models.TextField()

	def __str__(self):
		return self.name