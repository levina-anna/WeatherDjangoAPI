def prepare_weather_data(data):
    """
    Подготавливает данные о погоде для сохранения в базе данных.

    Функция принимает данные в виде словаря (один объект) или списка словарей
    и преобразует их в формат, подходящий для сериализатора.

    Параметры:
        data (dict | list): Входные данные. Может быть одним объектом (dict)
        или списком объектов (list). Пример входных данных:
        [
            {
                "city": "Москва",
                "date_time": "2024-01-01",
                "temperature": 3,
                "humidity": 80,
                "wind_speed": 1.5,
                "description": "Облачно"
            }
        ]

    Возвращает:
        list: Подготовленные данные в виде списка словарей с обязательными
        и дополнительными полями.

    Обязательные поля:
        - city
        - date_time
        - temperature

    Дополнительные поля (если присутствуют):
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
