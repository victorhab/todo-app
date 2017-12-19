from django.db import models
from django.utils import timezone

# Create your models here.
class Activity(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title