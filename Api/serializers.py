from rest_framework import serializers
from . import models


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'email']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = '__all__'


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Queue
        fields = '__all__'