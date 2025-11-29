# Словари
# имя = {
#   'ключ': значение,
#   'ключ': значение,
#   'ключ': значение,
#   ...
# }

person = {
    'name': 'Шклгеыл',
    'age': 'скуф',
    'gender': 'непонятно',
    'height': 15,
    'weight': 111,
    'is_alive': True,
}

# Добавление значения в словарь
person['is_bald'] = 'of course nigga bitch, mega ultra duper bombastic'
print(person)

# Получение значений из словаря
    # 1. по ключу
print(person['name'])   # Шклгеыл
print(person['age'])    # скуф
print(person['gender']) # непонятно

    # 2. с помощью get()
print(person.get('name'))   # Шклгеыл
print(person.get('age'))    # скуф
print(person.get('gender')) # непонятно
print(person.get('chpok')) # None

print(person.get('pepuchki', 'хз чо надо'))


# Удаление значений из словаря
    # 1. с помощью del
del person['name']
print(person)

    # 2. с помощью pop()
person.pop('age')
print(person)

print(person.pop('chpok', 'нет такого, иди в очко'))
    

# Перебор словаря
for key in person:
    print(f'Ключ: {key}, значение: {person[key]}')

# По ключу 
for key in person.keys():
    print(f'Ключ: {key}, значение: {person[key]}') 

# По значениям
for value in person.values():
    print(f'Значение: {value}')

# Комплексный способ
for key, value in person.items():
    print(f'Ключ: {key}, значение: {value}')


# Комплексные словари
gameChar = {
    'name': 'Chpukek',
    'health': 100,
    'level': 1,
    'titul': 'Dodik',
    'armor': {
        'head': 20,
        'chest': 60,
        'legs': 40,
        'hands': 3
    },
    'skills': ['fart', 'punch', 'kick'],
    'ultimate': ['mega poop', 'show fuck'],
    'money': 48,
    'stamina': 2,
    'id': 'dlb'
}

print('броня в груди:', gameChar['armor']['chest'])
print('второй скил Чпукека:', gameChar['skills'][1])

for key, value in gameChar['armor'].items():
    print(f'Ключ: {key}, значение: {value}')

# Напишите программу, которая принимает словарь и возвращает новый словарь,
# где значения ключей заменены на их квадраты.

# Телефонная книга
# Создай программу-телефонную книгу. Программа должна:
# - Хранить имена и номера телефонов в словаре
# - Позволять пользователю добавлять новые контакты (имя и номер)
# - Искать номер телефона по имени
# - Выводить все контакты

# Оценки студентов
# Создай словарь, где ключи — это имена студентов, 
# а значения — списки их оценок. Напиши функции, которые:
# -Добавляют новую оценку студенту
# -Вычисляют средний балл для каждого студента
# -Находят студента с самым высоким средним баллом
# Пример словаря: {
#   "Анна": [5, 4, 5], 
#   "Иван": [3, 4, 4], 
#   "Мария": [5, 5, 4]
# }