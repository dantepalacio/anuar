from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    pass

class Token(models.Model):
    objects = models.Manager()


class Publisher(models.Model):
    question = models.TextField()
