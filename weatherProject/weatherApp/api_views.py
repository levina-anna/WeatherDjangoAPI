from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import WeatherReportSerializer
from .models import WeatherReport
from .modules.weather_api.main import prepare_weather_data


class WeatherAPIView(generics.ListAPIView):
    """
    Представление API для обработки данных о погоде.
    Поддерживает методы GET и POST.
    """
    queryset = WeatherReport.objects.all()
    serializer_class = WeatherReportSerializer

    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запросы.

        Возвращает информационное сообщение о назначении API
        и пример формата JSON для отправки данных.
        """
        info_message = {
            "Информация": "Это API предназначено для отправки JSON файла c информацией о погоде"
                          " и сохранения ее в базу данных.",

            "Пример JSON файла":

                [
                    {
                        "city": "Москва",
                        "date_time": "2024-01-01",
                        "temperature": 3,
                        "humidity": 1,
                        "wind_speed": 1.0,
                        "description": ""
                    },
                    {
                        "city": "Москва",
                        "date_time": "2024-01-02",
                        "temperature": 4,
                        "humidity": 1,
                        "wind_speed": 1.0,
                        "description": ""
                    }
                ]
        }
        return Response(info_message, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запросы.

        Ожидает JSON с данными о погоде, обрабатывает их через
        функцию prepare_weather_data, валидирует через сериализатор
        и сохраняет в базу данных.

        Возвращает:
        - 201 Created: если данные успешно сохранены.
        - 400 Bad Request: если данные не прошли валидацию.
        - 500 Internal Server Error: если возникла серверная ошибка.
        """
        try:
            prepared_data = prepare_weather_data(request.data)

            serializer = WeatherReportSerializer(data=prepared_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Сообщение': 'Данные успешно сохранены в базу данных',
                    'Данные': serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'Сообщение': 'Ошибка валидации данных',
                    'Ошибки': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'Сообщение': 'Произошла ошибка на сервере',
                'Ошибка': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
