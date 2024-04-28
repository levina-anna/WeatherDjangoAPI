def prepare_weather_data(data):
    # Определение списка всех возможных полей, которые могут быть в модели
    all_possible_fields = [
        'city', 'date_time', 'temperature', 'humidity',
        'wind_speed', 'description'
    ]

    # Определение списка обязательных полей
    mandatory_fields = ['city', 'date_time', 'temperature']

    # Преобразование QueryDict в словарь
    data_dict = {key: value[0] for key, value in data.lists() if key in all_possible_fields}

    # Подготовка списка словарей с нужными полями
    prepared_data = []

    # Поскольку функция ожидает список словарей, обернем словарь в список
    for item in [data_dict]:  # Теперь item гарантированно будет словарем
        # Начинаем с обязательных полей
        weather_data = {field: item.get(field) for field in mandatory_fields}

        # Добавляем необязательные поля, если они присутствуют и соответствуют списку возможных
        for field in all_possible_fields:
            if field not in mandatory_fields and field in item:
                weather_data[field] = item[field]

        # Если поля корректны, добавляем словарь в подготовленный список
        prepared_data.append(weather_data)

    return prepared_data
