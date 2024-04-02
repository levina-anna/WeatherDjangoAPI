from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import WeatherReportSerializer
from .models import WeatherReport
from .modules.weather_api.main import prepare_weather_data


class WeatherAPIView(generics.ListAPIView):
    queryset = WeatherReport.objects.all()
    serializer_class = WeatherReportSerializer

    # Метод GET для отображения информационного сообщения и примера JSON
    def get(self, request, *args, **kwargs):
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

    # Метод POST для отправки JSON
    def post(self, request, *args, **kwargs):
        prepared_data = prepare_weather_data(request.data)

        serializer = WeatherReportSerializer(data=prepared_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'Сообщение': 'Данные успешно сохранены в базу данных',
                'Данные': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            print("Произошла ошибка")
