from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GymViewSet

router = DefaultRouter()
router.register(r'gyms', GymViewSet)

urlpatterns = [
    path('', include(router.urls)),
]