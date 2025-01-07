def prepare_weather_data(data):
    """
    Prepares weather data for saving to the database.

    This function accepts data in the form of a dictionary (a single object)
    or a list of dictionaries and transforms it into a format suitable for the serializer.

    Parameters:
        data (dict | list): Input data. Can be a single object (dict)
        or a list of objects (list). Example input:
        [
            {
                "city": "Moscow",
                "date_time": "2024-01-01",
                "temperature": 3,
                "humidity": 80,
                "wind_speed": 1.5,
                "description": "Cloudy"
            }
        ]

    Returns:
        list: Prepared data as a list of dictionaries with mandatory
        and optional fields.

    Mandatory fields:
        - city
        - date_time
        - temperature

    Optional fields (if present):
        - humidity
        - wind_speed
        - description
    """
    all_possible_fields = [
        'city', 'date_time', 'temperature', 'humidity',
        'wind_speed', 'description'
    ]

    mandatory_fields = ['city', 'date_time', 'temperature']

    if isinstance(data, dict):
        data = [data]

    prepared_data = []

    for item in data:
        weather_data = {field: item.get(field) for field in mandatory_fields}

        for field in all_possible_fields:
            if field not in mandatory_fields and field in item:
                weather_data[field] = item[field]

        prepared_data.append(weather_data)

    return prepared_data
