from rest_framework import viewsets, generics, permissions
from .models import *
from .serializers import *


class UserRegistrationViews(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializers


class GuideRegistrationViews(viewsets.ModelViewSet):
    queryset = GuideRegistration.objects.all()
    serializer_class = GuideRegistrationSerializers


class ProfileView(viewsets.ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileSerializers


class TourCreateView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TourDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [permissions.IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)


class TourhotosView(viewsets.ModelViewSet):
    queryset = TourPhotos.objects.all()
    serializer_class = TourPhotosSerializer
    permission_classes = [permissions.IsAdminUser]


class ReservationCreateAPIView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
