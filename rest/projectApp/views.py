from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from projectApp.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer