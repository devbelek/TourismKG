from django.contrib.auth.models import User
from django.db import models


class ProfileUser(models.Model):
    bio = models.TextField(blank=True)