from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, renderers, permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
