from rest_framework import serializers
from .models import Schedule, Record


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('coach', 'gym', 'weekday', 'start_time', 'end_time')


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('coach', 'client', 'gym', 'start_time', 'end_time')