FROM python:3.11.5

RUN pip install --upgrade pip
RUN apt update && apt install -y nano

ENV DJANGO_SETTINGS_MODULE=weatherProject.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /WeatherDjangoAPI

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /WeatherDjangoAPI

WORKDIR /WeatherDjangoAPI/weatherProject

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD python3 manage.py migrate && gunicorn weatherProject.wsgi:application --bind 0.0.0.0:8000
