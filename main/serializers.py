from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['owner', 'title', 'description', 'start_date', 'end_date', 'price', 'location', 'view_count']

class TourPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPhotos
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

