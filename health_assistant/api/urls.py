# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthDataViewSet
from .services import get_health_recommendation

router = DefaultRouter()
router.register(r'healthdata', HealthDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recommendation/', health_recommendation),
]