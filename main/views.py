from rest_framework import viewsets
from .models import ProfileUser
from .serializers import ProfileSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = ProfileUser.objects.all()
    serializer_class = ProfileSerializer
