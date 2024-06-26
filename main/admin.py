from django.contrib import admin
from .models import *

admin.site.register(ProfileUser)
admin.site.register(Tour)
admin.site.register(TourPhotos)
admin.site.register(Reservation)

