from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet, RecordViewSet

router = DefaultRouter()
router.register(r'schedules', ScheduleViewSet)
router.register(r'records', RecordViewSet)


urlpatterns = [
    path('', include(router.urls)),
]