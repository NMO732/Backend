from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets,generics
from projectApp.serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

class UserListApiView(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        qs = User.objects.filter(is_active=True)
        return qs