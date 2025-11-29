# Массивы / Списки
# имя = [значение, значение, значение, ...]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Ivan', 'Petr', 'Vasya', 'Masha', 'Kolya']
logics = [True, False, True, False, True]
mixed = [1, 'Ivan', True, 2, 'Petr', False, 5, 'Kolya', True]

# Создание пустого массива
empty = []
emptyList = list()

# Получение элемента массива
# Индекс - порядковый номер элемента в массиве (начинается с 0)
# В порядке возрастания
# print(names[0]) # Ivan
# print(names[1]) # Petr
# print(names[2]) # Vasya
# print(names[3]) # Masha

# В порядке убывания
# print(names[-1]) # Kolya
# print(names[-2]) # Masha
# print(names[-3]) # Vasya
# print(names[-4]) # Petr

# Перебор массива
# Через цикл while
# i = 0
# while i < len(names):
#     print(f'Человек №{i + 1}: {names[i]}')
#     i += 1

# Через цикл for
# for name in names:
#     print(f'Ochko{name}')

# Разложение массива
weatherData = ['Шклгеыл', 5, 1]
city, temp, feelsLike = weatherData
# print(f'Город: {city}')
# print(f'Температура: {temp}')
# print(f'Ощущается как: {feelsLike}')

# Получение части массива
# array[start:] - от start до конца
# array[:end] - от начала до end-1
# array[start:end] - от start до end-1
# array[start:end:step] - от start до end-1 с шагом step

# print(names[3:]) # Masha, Kolya
# print(names[:3]) # Ivan, Petr, Vasya
# print(names[1:4]) # Petr, Vasya, Masha
# print(numbers[2:8:2]) # 3, 5, 7

# Методы массивов
# arr.append(item) - добавляет элемент в конец массива
# arr.insert(index, item) - добавляет item в массив по индексу index
# arr.extend(items) - добавить набор элементов в конец arr
# arr.remove(item) - удалить элемент item
# arr.clear() - удалить все элементы из arr
# arr.index(item) - возвращает индекс элемента item
# arr.pop(index) - удаляет и возвращает элемент под индексом index
# arr.count(item) - подсчитывает, сколько элементов item есть в массиве
# arr.sort([key]) - сортирует элементы по возрастанию
#                   в key можно записать ф-цию сортировки
# arr.reverse() - переворачивает массив в обратном порядке
# arr.copy() - копирует массив

# len(arr) - узнать длину массива
# sorted(list, [key]) - возвращает отсортированный список
# min(arr) - найти минимальный элемент в массиве
# max(arr) - найти максимальный элемент в массиве

import random
array = [random.randint(-10, -1) for i in range(10)]
print(array)

# Задачки епта
# Задача 1: Найти максимальное число в массиве
# Условие: Напишите программу, которая находит самое большое число в массиве
# (не используя встроенную функцию max())
max = array[0]

for i in array:
    if i > max:
        max = i

print('Наибольшее число:', max)

# Задача 2: Посчитать четные числа
# Условие: Дан массив чисел. Посчитайте, сколько в нем четных чисел
count = 0

for i in array:
    if i % 2 == 0:
        count += 1

print(f'кол-во четных: {count}')


# Задача 3: Найти пропущенное число
# Условие: Дан массив, содержащий числа от 1 до N, но одно число пропущено. 
# Найдите это число
# arr1 = [1, 3, 4, 5, 6, 7, 9, 10]

# Задача 4: Переместить нули в конец
# Условие: Дан массив с числами. Переместите все нули в конец массива, 
# сохранив порядок остальных элементов

# Задача 5: Удалить дубликаты
# Условие: Дан массив с числами. Удалите дубликаты

# 6. Поиск пары с заданной суммой
# Найти все уникальные пары элементов в массиве, 
# сумма которых равна заданному числу K. 
# Вывести пары без повторений. 
# Например: [1, 5, 3, 7, 2], K=8 → [(1,7), (3,5)]

