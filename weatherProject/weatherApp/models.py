from django.db import models


class WeatherReport(models.Model):
    """
    Model for storing weather data.
    """
    city = models.CharField(max_length=100, verbose_name="City")
    date_time = models.DateTimeField(verbose_name="Date and time of observation")
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperature (°C)")
    humidity = models.IntegerField(verbose_name="Humidity (%)")
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Wind speed (km/h)")
    description = models.CharField(max_length=255, verbose_name="Weather description")

    def __str__(self):
        return f"{self.city} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"
