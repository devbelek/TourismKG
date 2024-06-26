from rest_framework import viewsets, generics, permissions
from .models import *
from .serializers import *


from django.urls import reverse_lazy
<<<<<<< HEAD

from django.contrib.auth.mixins import LoginRequiredMixin
=======
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tour
from .forms import TourForm
>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3


class ProfileView(viewsets.ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileSerializer


class TourCreateView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
<<<<<<< HEAD
    permission_classes = [permissions.IsAdminUser]
=======
    permission_classes = [permissions.IsAuthenticated]
>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TourDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
<<<<<<< HEAD
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

=======
    permission_classes = [permissions.IsAuthenticated]
>>>>>>> 4ff5cd637c84a2065e10f50dc2943038fa7369e3
