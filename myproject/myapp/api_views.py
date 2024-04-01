from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import WeatherReportSerializer
from .models import WeatherReport


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
