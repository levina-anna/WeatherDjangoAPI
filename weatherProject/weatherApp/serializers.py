from rest_framework import serializers
from .models import WeatherReport


class WeatherReportSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели WeatherReport.

    Используется для валидации и преобразования данных о погоде.
    Все поля модели включены в сериализацию.

    Валидация:
    - Поле 'city' обязательно и не может быть пустым.
    - Поле 'date_time' обязательно и не может быть null.
    - Поле 'temperature' обязательно и не может быть null.
    """
    class Meta:
        model = WeatherReport
        fields = '__all__'

        extra_kwargs = {
            'city': {'required': True, 'allow_blank': False},
            'date_time': {'required': True, 'allow_null': False},
            'temperature': {'required': True, 'allow_null': False},
        }
