from django.db import transaction
from rest_framework import viewsets, status
from .models import User
from .serializers import UserSerializer
from coaches.serializers import CoachSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            user_data = {key: value for key, value in request.data.items() if key in UserSerializer.Meta.fields}
            user_serializer = UserSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)

            user = user_serializer.save()

            if request.data.get("role", None) and request.data["role"] == 'coach':
                coach_data = {key: value for key, value in request.data.items() if key in CoachSerializer.Meta.fields}

                coach_data['user'] = user.id
                coach_serializer = CoachSerializer(data=coach_data)

                coach_serializer.is_valid(raise_exception=True)
                coach_serializer.save()

                response_data = {**user_serializer.data, **coach_serializer.data}
                return Response(response_data, status=status.HTTP_201_CREATED)
            
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
