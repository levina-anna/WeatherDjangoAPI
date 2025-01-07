from rest_framework import serializers
from .models import WeatherReport


class WeatherReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the WeatherReport model.
    Used for validation, transformation, and default values in forms.
    """
    class Meta:
        model = WeatherReport
        fields = '__all__'

        extra_kwargs = {
            'city': {'required': True, 'allow_blank': False},
            'date_time': {'required': True, 'allow_null': False},
            'temperature': {'required': True, 'allow_null': False},
        }

    def get_initial(self):
        """
        Sets default values for form rendering in DRF browsable API.
        """
        return {
            'city': "Moscow",
            'date_time': "2024-01-01T00:00:00",
            'temperature': 0,
            'humidity': 0,
            'wind_speed': 0.0,
            'description': "Clear",
        }
