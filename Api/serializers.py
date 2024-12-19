from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields = '__all__'


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Queue
        fields = '__all__'