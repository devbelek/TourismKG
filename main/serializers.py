from rest_framework import serializers
from .models import *


class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = '__all__'


class GuideRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = GuideRegistration
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
