from django.contrib.auth.models import User
from django.db import models


class ProfileUser(models.Model):
    bio = models.TextField(blank=True)

class Tour(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tours')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title