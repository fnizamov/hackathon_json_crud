import json
from json.decoder import JSONDecodeError
from settings import DataBase
from datetime import datetime

"""
list_ = [
    {
        'id': 1,
        'title': 'IPhone 13 Pro Max',
        'price': '152000'
        'description': '512 GB / Gold',
        'date_created': '26.08.2022 18:45'
        'date_updated': '26.08.2022 20:15'
    },
    {
        'id': 2,
        'title': 'Samsung Galaxy S22 Ultra',
        'price': '150000'
        'description': '512 GB / Black',
        'date_created': '26.08.2022 18:20'
        'date_updated': '26.08.2022 20:15'
    }
"""

def get_all_data():
    with open(DataBase) as file:
        try:
            return json.load(file)
        except JSONDecodeError:
            return []

def create():
    id_ = datetime.now().strftime('%H%M%S')
    data = {
        'id': id_,
        'title': input('Введите наименование товара: '),
        'price': int(input('Укажите стоимость товара: ')),
        'description': input('Введите описание товара: '),
        'data_created': datetime.now().strftime('%d.%m.%Y %H:%M')
    }
    json_data: list = get_all_data()
    json_data.append(data)
    with open(DataBase, 'w') as file:
        json.dump(json_data, file, indent=4)
    print(f'  --->  Товар ({id_}) успешно добавлен!')

def get_data_by_id():
    id_ = input('Введите ID товара: ')
    for obj in get_all_data():
        if obj['id'] == id_:
            return obj
    return 'Неверно указан ID товара.'


def delete():
    id_ = input('Введите ID для удаления товара: ')
    data = get_all_data()
    for obj in get_all_data():
        if obj['id'] == id_:
            data.remove(obj)
            break
    with open(DataBase, 'w') as file:
        json.dump(data, file, indent=4)
    print('-------------------------------------------------------------------------------')
    print(f'  --->  Товар ({id_}) успешно удален!')
    print('-------------------------------------------------------------------------------')

def clear():
    confirm = input('Подтвердите очищение всей базы (Y/N): ')
    if confirm == 'y':
        with open(DataBase, 'w') as file:
            json.dump([], file, indent=4)
        print('-------------------------------------------------------------------------------')
        print(f'  --->  База данных успешно очищена!')
        print('-------------------------------------------------------------------------------')
    elif confirm == 'n':
        return []
            

def update():
    id_ = input('Введите ID товара, который хотите изменить')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            obj['title'] = input('Введите наименование товара: ') or obj['title']
            obj['price'] = input('Укажите стоимость товара: ') or obj['price']
            obj['description'] = input('Введите описание товара: ') or obj['description']
            obj['date_updated'] = datetime.now().strftime('%d.%m.%Y %H:%M')
            break
    with open(DataBase, 'w') as file:
        json.dump(data, file, indent=4)