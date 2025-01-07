from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import WeatherReportSerializer
from .models import WeatherReport
from .modules.weather_api.main import prepare_weather_data


class WeatherAPIView(generics.ListAPIView):
    """
    API view for processing weather data.
    Supports GET and POST methods.
    """
    queryset = WeatherReport.objects.all()
    serializer_class = WeatherReportSerializer

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests.

        Returns an informational message about the purpose of the API
        and an example JSON format for submitting data.
        """
        info_message = {
            "Information": "This API is designed to send a JSON file with weather information"
                           " and save it to the database.",

            "Example JSON file":

                [
                    {
                        "city": "Moscow",
                        "date_time": "2024-01-01T12:00:00",
                        "temperature": 3,
                        "humidity": 1,
                        "wind_speed": 1.0,
                        "description": "Cloudy"
                    },
                    {
                        "city": "Moscow",
                        "date_time": "2024-01-02T14:30:00",
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
        Handles POST requests.

        Expects a JSON file with weather data, processes it using the
        `prepare_weather_data` function, validates it through the serializer,
        and saves it to the database.

        Returns:
        - 201 Created: if the data is successfully saved.
        - 400 Bad Request: if the data validation fails.
        - 500 Internal Server Error: if a server error occurs.
        """
        try:
            prepared_data = prepare_weather_data(request.data)

            serializer = WeatherReportSerializer(data=prepared_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Message': 'Data has been successfully saved to the database',
                    'Data': serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'Message': 'Data validation error',
                    'Errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'Message': 'A server error occurred',
                'Errors': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
