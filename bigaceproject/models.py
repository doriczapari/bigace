from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Technology(models.Model):
    name = models.CharField(max_length=264)


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    skills = models.ManyToManyField(Technology, blank=True)
    github = models.URLField(null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)


class Project(models.Model):
    name = models.CharField(max_length=264)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='owner')
    participants = models.ManyToManyField(User, blank=True)
    deadline = models.DateField(null=True, blank=True)
    time = models.PositiveSmallIntegerField(null=True, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    max_people = models.PositiveSmallIntegerField(null=True, blank=True)


class Task(models.Model):
    name = models.CharField(max_length=264)
    project = models.ForeignKey(Project, related_name='tasks')
    completed = models.BooleanField(default=False)
