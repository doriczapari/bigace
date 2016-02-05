from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator


class Technology(models.Model):
    LEVEL_CHOICES = (
        (0, 'Novice'),
        (1, 'Intermediate'),
        (2, 'Expert'),
    )
    name = models.CharField(max_length=264)
    level = models.SmallIntegerField(null=True, blank=True, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Technologies'


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    skills = models.ManyToManyField(Technology, blank=True)
    github = models.URLField(null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    # ratings = ArrayField(models.SmallIntegerField(null=False, blank=False,), null=True, blank=True)

    def __str__(self):
        return self.user


class Project(models.Model):
    name = models.CharField(max_length=264)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='owner')
    participants = models.ManyToManyField(User, blank=True)
    deadline = models.DateField(null=True, blank=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    max_people = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    @property
    def total_points(self):
        total = 0
        for task in self.tasks:
            total += task.points
        return total

        # sum(task.points for task in self.tasks)

    @property
    def reviews(self):
        return sum(self.rating_to) / len(self.rating_to)


class Rating(models.Model):
    rating_to = models.ForeignKey(User, related_name='rating_to')
    rating_from = models.ForeignKey(User, related_name='rating_from')
    point = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])


class Task(models.Model):
    name = models.CharField(max_length=264)
    project = models.ForeignKey(Project, related_name='tasks')
    completed = models.BooleanField(default=False)
    points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
