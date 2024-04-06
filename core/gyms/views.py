from rest_framework import viewsets
from .models import Gym
from .serializers import GymSerializer
from rest_framework.permissions import IsAuthenticated


class GymViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Gym.objects.all()
    serializer_class = GymSerializer