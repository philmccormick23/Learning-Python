from __future__ import unicode_literals
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    tags = TaggableManager()

class Startups(models.Model):
    title = models.CharField(max_length=200)
    tags = TaggableManager()

class Score(models.Model):
    title = models.CharField(max_length=200)
    tags = TaggableManager()