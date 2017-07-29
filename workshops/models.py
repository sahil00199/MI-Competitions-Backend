# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class WorkshopsGenre(models.Model):
	name = models.CharField(max_length = 100)
	description = models.TextField()

	def __str__(self):
		return self.name
'''
class Workshop(models.Model):
	description = models.TextField()
	genres = WorkshopsGenre.objects.all()
'''

class WorkshopsEvent(models.Model):
	name = models.CharField(max_length = 100)
	genre = models.ForeignKey(WorkshopsGenre,related_name='genres', on_delete = models.CASCADE)
	description = models.TextField()

	def __str__(self):
		return self.name