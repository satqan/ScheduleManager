from rest_framework import serializers
from .models import Gym


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ('name', 'address', 'contact_number', 'email')