from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
<<<<<<< HEAD
        fields = ['owner', 'title', 'description', 'start_date', 'end_date', 'price', 'location', 'view_count']

class TourPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPhotos
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
=======
        fields = ['owner', 'title', 'description', 'start_date', 'end_date', 'price', 'location']
>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3

