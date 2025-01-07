from django.db import models


class WeatherReport(models.Model):
    """
    Модель для хранения данных о погоде.
    """
    city = models.CharField(max_length=100, verbose_name="Город")
    date_time = models.DateTimeField(verbose_name="Дата и время наблюдения")
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Температура (°C)")
    humidity = models.IntegerField(verbose_name="Влажность (%)")
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Скорость ветра (км/ч)")
    description = models.CharField(max_length=255, verbose_name="Описание погоды")

    def __str__(self):
        return f"{self.city} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Отчет о погоде"
        verbose_name_plural = "Отчеты о погоде"
