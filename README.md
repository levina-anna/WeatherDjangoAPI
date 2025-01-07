# WeatherDjangoAPI

This application is designed to receive weather data, allowing submissions in JSON format or manually via a form, and store this data in a database.

![Screenshot](https://github.com/levina-anna/levina-anna.github.io/raw/main/images/WeatherDjangoAPI.png)

## Features

- Accepts weather data submissions in JSON format or via an HTML form.
- Stores submitted data in a database for future retrieval.

## API Usage

- GET /api/v1/weather
- POST /api/v1/weather

## Installation and Launch

1. Clone the repository:
```bash
git clone git@github.com:levina-anna/WeatherDjangoAPI.git
cd WeatherDjangoAPI
```
2. Launch the application using Docker:
```
docker-compose up --build
```
3. Open the application in your browser: http://localhost:8001/api/v1/weather

## Technologies Used

![Django](https://img.shields.io/badge/Django-5.0.3-092E20?logo=django&logoColor=white&style=flat-square)
![Django REST framework](https://img.shields.io/badge/Django%20REST%20framework-3.1.2-green)
![Python](https://img.shields.io/badge/Python-3.11.1-blue)
