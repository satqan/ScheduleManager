from rest_framework import viewsets
from .models import Coach
from .serializers import CoachSerializer
from rest_framework.permissions import IsAuthenticated


class CoachViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer