from rest_framework import generics
from .serializers import WeatherReportSerializer
from .models import WeatherReport


class WeatherAPIView(generics.ListAPIView):
    queryset = WeatherReport.objects.all()
    serializer_class = WeatherReportSerializer
