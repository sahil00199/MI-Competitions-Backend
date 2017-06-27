# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class City(models.Model):
	city_name=models.CharField(max_length=20)

	def __str__(self):
		return self.city_name


class College(models.Model):
	college_name=models.CharField(max_length=50)
	located_city=models.ForeignKey(City,on_delete=models.CASCADE)

	def __str__(self):
		return self.college_name


class UserProfile(models.Model):
    YEAR = ['First',
            'Second',
            'Third',
            'Fourth',
            'Fifth', ]

    YEAR_CHOICES = [(c, c) for c in YEAR]

    name = models.CharField(max_length=50)
    mi_number = models.CharField(max_length=10, unique=True, default='default')
    email = models.EmailField(max_length=70, unique=True, blank=False)
    present_city = models.ForeignKey(City, on_delete=models.CASCADE)
    present_college = models.ForeignKey(College, on_delete=models.CASCADE)
    mobile_number = models.IntegerField(unique=True, default=None)
    whatsapp_number = models.IntegerField(unique=True, default=None)
    postal_address = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    year_of_study = models.CharField(max_length=7, choices=YEAR_CHOICES)

    def __str__(self):
        return self.name

    def set_mi_number(self, no):
        self.mi_number=no

    class Meta:
        ordering = ('name',)