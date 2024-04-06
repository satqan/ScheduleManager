from rest_framework import serializers
from .models import Coach


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('user', 'date_of_birth', 'gender', 'gyms')