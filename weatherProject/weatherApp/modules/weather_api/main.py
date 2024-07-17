def prepare_weather_data(data):

    all_possible_fields = [
        'city', 'date_time', 'temperature', 'humidity',
        'wind_speed', 'description'
    ]

    mandatory_fields = ['city', 'date_time', 'temperature']
    data_dict = {key: value[0] for key, value in data.lists() if key in all_possible_fields}
    prepared_data = []

    for item in [data_dict]:
        weather_data = {field: item.get(field) for field in mandatory_fields}

        for field in all_possible_fields:
            if field not in mandatory_fields and field in item:
                weather_data[field] = item[field]

        prepared_data.append(weather_data)

    return prepared_data
