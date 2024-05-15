from django.shortcuts import render

from rest_framework import viewsets
from .models import HealthData
from .serializers import HealthDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import get_health_recommendation

class HealthDataViewSet(viewsets.ModelViewSet):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer

@api_view(['POST'])
def health_recommendation(request):
    user_data = request.data
    recommendation = get_health_recommendation(user_data)
    return Response({'recommendation': recommendation})
