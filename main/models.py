from django.contrib.auth.models import User
from django.db import models
<<<<<<< HEAD
from django.db.models import UniqueConstraint
=======
>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3


class ProfileUser(models.Model):
    bio = models.TextField(blank=True)

<<<<<<< HEAD

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

=======
>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3
class Tour(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tours')
    title = models.CharField(max_length=200)
    description = models.TextField()
<<<<<<< HEAD
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

    # class Meta:
    #     constraints = [
    #         UniqueConstraint(fields=['user', 'tour'], name='unique_reservation')
    #     ]

    def __str__(self):
        return f'Бронироание от  {self.user}'





=======
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3
