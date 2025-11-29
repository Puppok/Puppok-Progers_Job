# # Словари / объекты
# # имя = {
# #     'ключ1': 'значение1',
# #     'ключ2': 'значение2',
# #     'ключ3': 'значение3'
# # }

# # пример словаря
# person = {
#     'name': 'Tom',
#     'age': 20,
#     'isProgrammer': True
# }

# shopList = {
#     'bread': 2,
#     'milk': 3,
#     'eggs': 4,
#     'cheese': 1,
#     'water': 5
# }

# # ввод значений в словарь
# age = int(input('Введите ваш возраст: '))

# person['age'] = age
# print('age:', person['age'])

# city = input('Введите город: ')
# person['city'] = city
# print(person)

# print('\n-------\nПолучение значений из словаря')
# # получение значений
#     # 1. по ключу
# print(person['name'])
# print(person['age'])
# # print(person['pep']) - ошибка, ключа не существует

#     # 2. с помощью get()
# print(person.get('name')) 
# print(person.get('pep', 'Такого ключа не существует'))


# print('\n-------\nУдаление значений из словаря')
# # удаление значений
#     # 1. напрямую (del)
# del person['name']
# # del person['koko'] - ошибка, ключа не существует
# print(person)

#     # 2. с помощью pop()
# person.pop('age')
# print(person.pop('koko', 'koko не существует'))
# print(person)


# print('\n-------\nПеребор значений в словаре')
# # перебор значений в словаре
#     # 1. Общий способ
# for key in shopList: 
#     print(key, shopList[key])

#     # 2. По ключам
# print('--- только ключи ---')
# for key in shopList.keys():
#     print(key)

#     # 3. По значениям
# print('--- только значения ---')
# for value in shopList.values():
#     print(value)

#     # 4. Комплексный способ
# print('--- Комплексный ---')
# for key, value in shopList.items():
#     print(f'ключ {key}, значение {value}')
    

# # Вложенные словари (словарь в словаре)
# person = {
#     'name': 'Tom',
#     'age': 20,
#     'isProgrammer': True,
#     'languages': {
#         'python': 'good',
#         'c++': 'bad',
#         'JavaScript': 'bad',
#         'PHP': 'bullshit'
#     },
#     'hobby': ['sport', 'music', 'books', 'coding', 'games']
# }

# print(person['name']) # обращение к значению по ключу
# print(person['languages']['python']) # обращение к словарю с языками и значению с ключом python
# print(person['hobby'][3]) # обращение к списку с хобби и значению с индексом 3 (coding)


# # Задачи
# # 1. Создайте функцию word_count, которая принимает строку и возвращает словарь,
# # где ключами являются уникальные слова из строки, 
# # а значениями - количество их повторений.
# # input
# def wordCount(text):
#     dict = {}

#     for word in text.split():
#         if word in dict:
#             dict[word] += 1
#         else:
#             dict[word] = 1
        
#     return dict

# text = "hello world hello python"
# print(wordCount(text))

# # output
# dict = {
#     'hello': 2,
#     'world': 1,
#     'python': 1
# }

# # .split() - поможет разделить строку на слова

# # 2. Напишите программу, которая принимает словарь и 
# # возвращает новый словарь,
# # где значения ключей заменены на их квадраты.

# def squareDict(dict):
#     newDict = {}

#     for key, value in dict.items():
#         newDict[key] = value ** 2

#     return newDict

# testDict = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4
# }

# print(testDict)
# print(squareDict(testDict))

# # 3. Телефонная книга
# # Создай программу-телефонную книгу. Программа должна:
# # - Хранить имена и номера телефонов в словаре
# # - Позволять пользователю добавлять новые контакты (имя и номер)
# # - Искать номер телефона по имени
# # - Выводить все контакты

# # 4. Оценки студентов
# # Создай словарь, где ключи — это имена студентов, 
# # а значения — списки их оценок. Напиши функции, которые:
# # -Добавляют новую оценку студенту
# # -Вычисляют средний балл для каждого студента
# # -Находят студента с самым высоким средним баллом

# # Пример словаря: {
# #   "Анна": [5, 4, 5], 
# #   "Иван": [3, 4, 4], 
# #   "Мария": [5, 5, 4]
# # }

dict = {
  "Анна": [5, 2, 5], 
  "Иван": [1, 1, 5], 
  "Мария": [3, 2, 2]
}

def find(dict):
    max = 0
    for student, marks in dict.items():
        average = sum(marks) / len(marks)
        if average > max:
            max = average
            name = student
    return f'{name}: {max}'

print(find(dict))