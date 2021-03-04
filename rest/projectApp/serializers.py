#from projectApp.models import User
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        #fields = '__all__'
        fields = ['username', 'first_name','email', 'is_active','is_staff']