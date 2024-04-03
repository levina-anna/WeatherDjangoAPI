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

```bash
git clone <repository-url>
cd <project-directory-name>
# Install dependencies
pip install -r requirements.txt
# Apply database migrations
python manage.py migrate
# Run the application
python manage.py runserver
```

## Technologies Used

- Django 5.0.3
- djangorestframework 3.1.2
- Python 3.11.1
