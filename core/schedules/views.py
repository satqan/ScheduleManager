from datetime import datetime
from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response

from coaches.models import Coach
from users.models import User
from gyms.models import Gym
from .models import Schedule, Record
from .serializers import ScheduleSerializer, RecordSerializer
from rest_framework.permissions import IsAuthenticated


class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class RecordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def create(self, request, *args, **kwargs):
        client_id = request.data.get('client')
        coach_id = request.data.get('coach')
        gym_id = request.data.get('gym')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')

        start_time = timezone.make_aware(datetime.fromisoformat(start_time))
        end_time = timezone.make_aware(datetime.fromisoformat(end_time))

        if start_time >= end_time:
            return Response({"error": "End time must be after start time."}, status=status.HTTP_400_BAD_REQUEST)

        coach = Coach.objects.get(id=coach_id)
        client = User.objects.get(id=client_id)
        gym = Gym.objects.get(id=gym_id)

        weekday = start_time.strftime("%A").lower()
        schedules = coach.schedules.filter(weekday=weekday, gym=gym_id)
        if not schedules:
            return Response({"error": "The coach does not have schedule for given weekday"}, status=status.HTTP_400_BAD_REQUEST)

        for schedule in schedules:
            schedule_start_datetime = timezone.make_aware(datetime.combine(start_time.date(), schedule.start_time))
            schedule_end_datetime = timezone.make_aware(datetime.combine(end_time.date(), schedule.end_time))

            if schedule_start_datetime > start_time or schedule_end_datetime < end_time:
                return Response({"error": "The coach is not available during the requested time."}, status=status.HTTP_400_BAD_REQUEST)

        records = Record.objects.filter(gym=gym_id, coach=coach_id)
        for record in records:
            if max(start_time, record.start_time) < min(end_time, record.end_time):
                return Response({"error": "The period of the following record clashes with another record"},
                                status=status.HTTP_400_BAD_REQUEST)

        record = Record.objects.create(client=client, coach=coach, gym=gym, start_time=start_time, end_time=end_time)
        serializer = self.get_serializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
