"""
    В этом модуле следует размещать дополнительные методы для работы с данными, например:
    математические функции, работу со строковыми данными, преобразование данных в различные форматы (zip, pdf и т.п.)
"""

# Метод для преобразования объекта строки БД в стандартный тип данных Python
# (в объект dict), который хранит пары { 'ключ': значение }
def row_to_dict(row):
    # Если полученная строка из БД является объектон типа tuple
    # (неизменяемая коллекция, может быть получена, если в запросе указываются конкретные колонки для выбора)
    if isinstance(row, tuple):
        # возвращаем dict с помощью маппинга значений tuple и соответствующих названиям колонок ключей
        return dict(zip(row.keys(), row))
    # Если строка не "пустая", т.е. запрос к БД был успешен
    if row != None:
        # преобразуем row-объект в dict
        result = dict(row.__dict__)
        # удаляем поле с лишней служебной информацией
        result.pop('_sa_instance_state', None)
        return result
    else:
        return None