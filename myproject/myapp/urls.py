from django.urls import path
from .api_views import WeatherAPIView


urlpatterns = [
    path('api/v1/weather', WeatherAPIView.as_view())
]
