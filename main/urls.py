from django.urls import path
from .views import *


profile_list = ProfileView.as_view({
    'get': 'list',
    'post': 'create'
})

profile_detail = ProfileView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', profile_list, name='profile-list'),
    path('profiles/<int:pk>/', profile_detail, name='profile-detail'),

    path('tours/', TourCreateView.as_view(), name='tour-list-create'),
    path('tours/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
]
