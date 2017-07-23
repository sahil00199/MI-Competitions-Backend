from django.db import models
from participant_api.models import UserProfile
#from __future__ import unicode_literals

class Competition(models.Model):
    description = models.TextField()

class Genre(models.Model):
    genre = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        return self.genre

class Group(models.Model):
    name= models.CharField(max_length = 100)
    team_id = models.IntegerField(default = 0)
    members = models.ManyToManyField(UserProfile)
    event = models.ForeignKey('IndividualEvent', on_delete=models.CASCADE, blank = True)
    
    def __str__(self):
        return self.name

class IndividualEvent(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.ForeignKey(Genre, on_delete= models.CASCADE)
    about = models.TextField()
    rules = models.TextField()
    prizes = models.TextField()
    multicity_details = models.TextField()
    participants = models.ManyToManyField(UserProfile, blank=True)
    groups_part = models.ManyToManyField(Group, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class GroupEvent(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    about = models.TextField()
    rules = models.TextField()
    prizes = models.TextField()
    multicity_details = models.TextField()
    participants = models.ManyToManyField(Group, blank = True)

    def __str__(self):
        return self.name

    def delete(self, using=None):
        if self.participants:
            self.participants.delete()
        super(GroupEvent, self).delete(using)