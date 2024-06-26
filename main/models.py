from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('regular', 'Regular'),
        ('guide', 'Guide'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class GuideRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=False)
    experience = models.CharField(max_length=300, blank=False)
    phone_number = models.PositiveIntegerField(blank=False)
    image = models.ImageField(upload_to='guide_images/', blank=False)


class ProfileUser(models.Model):
    pass


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Tour(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tours')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class TourPhotos(models.Model):
    tour_photos = models.ForeignKey(Tour, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.tour_photos.title


class Reservation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    description = models.TextField(default="empty")
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    time_now = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Бронирование от {self.user}'
