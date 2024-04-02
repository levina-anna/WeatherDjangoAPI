def prepare_weather_data(data):
    # Определение списка всех возможных полей, которые могут быть в модели
    all_possible_fields = [
        'city', 'date_time', 'temperature', 'humidity',
        'wind_speed', 'description'
    ]

    # Определение списка обязательных полей
    mandatory_fields = ['city', 'date_time', 'temperature']

    # Подготовка списка словарей с нужными полями
    prepared_data = []

    for item in data:
        # Начинаем с обязательных полей
        weather_data = {field: item[field] for field in mandatory_fields}
        # Добавляем необязательные поля, если они присутствуют и соответствуют списку возможных
        unknown_fields = []
        for field in item:
            if field in all_possible_fields:
                if field not in mandatory_fields:
                    weather_data[field] = item[field]
            else:
                unknown_fields.append(field)

        if unknown_fields:
            # Прервать обработку и вернуть ошибку:
            raise ValueError(f"Введенные поля {unknown_fields} не соответствуют ни одному из возможных.")

        # Если поля корректны, добавляем словарь в подготовленный список
        prepared_data.append(weather_data)

    return prepared_data
