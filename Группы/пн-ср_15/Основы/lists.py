# Массивы / Списки
# имя = [значение1, значение2, значение3...]

numbers = [1, 4, 6, 18, 14, 20, 1, 46, 1, 57, 1]
names = ['Tom', 'Stas', 'Chpok', 'Markdown']
logics = [True, True, False, True]
mixed = [12, 67, 'Dima', True, 45.6, 'Antoshka']

# Получение значений массива
# print(numbers) # вывод цельного массива

# получение элементов в порядке возрастания
# print(names[0]) 
# print(names[3])

# получение элементов в порядке убывания
# print(names[-1]) 
# print(names[-4])

# Разложение элементов массива
weatherData = ['city', -6, -35]
# print(weatherData)

city, temp, feelsLike = weatherData
# print(city, temp, feelsLike)

# Перебор массива
# С помощью цикла for
# for element in mixed:
#     print(f'Элемент массива: {element}')

# print()

# С помощью цикла while
# i = 0
# while i < len(mixed):
#     print(f'Элемент {i + 1}: {mixed[i]}')
#     i += 1

# Получение части массива
# array[:end] - получение элементов по индексам от 0 до end-1
# print(numbers[:3])

# array[start:] - полчение элементов по индексам от start до конца
# print(numbers[2:])

# array[start:end] - получение элементов по индексам от start до end-1
# print(numbers[2:4])

# array[start:end:step] - получение элементов по индексам от start до end-1 с шагом step
# print(numbers[1:5:2])

# bigArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# print(bigArray[10:30:3])

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
randomArray = [random.randint(0, 100) for i in range(30)]




# Задача 1: Найти максимальное число в массиве
# Условие: Напишите программу, которая находит самое 
# большое число в массиве
# (не используя встроенную функцию max())
def findMax(arr):
    max = arr[0]
    for element in arr:
        if element > max:
            max = element
    print(f'Максимальное число в массиве: {max}')
# findMax(randomArray)

# Задача 2: Посчитать четные числа
# Условие: Дан массив чисел. Посчитайте, сколько в нем четных чисел
def countEven(arr):
    count = 0
    for element in arr:
        if element % 2 == 0:
            count += 1
    print(f'Количество четных чисел в массиве: {count}')
# countEven(arr1)

# Задача 3: Найти пропущенное число
# Условие: Дан массив, содержащий числа от 1 до N, но одно число пропущено. 
# Найдите это число
def findLost(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 1:
            print(f'Пропущенное число: {arr[i] - 1}')

# arr1 = [1, 3, 4, 5, 6, 7, 9, 10]
# findLost(arr1)

# Задача 4: Переместить нули в конец
# Условие: Дан массив с числами. Переместите все нули в конец массива, 
# сохранив порядок остальных элементов
def moveZeros(arr):
    for i in arr:
        if i == 0:
            arr.append(0)
            arr.remove(i)
    print(arr)

zeroArr = [0, 12, 0, 4, 0, 7, 0, 15, 7]
moveZeros(zeroArr)

# Задача 5: Удалить дубликаты
# Условие: Дан массив с числами. Удалите дубликаты
def deleteDoubles(arr):
    for i in range(0, len(arr) - 1):
        print(arr[i])
        for j in range(i + 1, len(arr) - 1):
            if arr[i] == arr[j]:
                arr.remove(arr[j])
    print(arr)

deleteDoubles(zeroArr)
