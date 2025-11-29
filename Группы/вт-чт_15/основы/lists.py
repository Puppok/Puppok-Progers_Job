# Массив (список)
# a = list() - создание массива командой list
# b = [] - создание пустого массива
# a = [1, 2, 3]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # массив чисел
names = ['Ivan', 'Petr', 'Vasya'] # массив строк
logic = [True, False, True] # массив логических значений
mixed = [1, 'Petr', True] # массив с разными типами данных

# Вывод элемента массива
print(names[0]) # Ivan
print(names[1]) # Petr
print(names[2]) # Vasya

# Вывод последнего элемента массива
print(names[-1]) # Vasya
print(names[-2]) # Petr
print(names[-3]) # Ivan

# Разложение массива
name1, name2, name3 = names

# Перебор элементов массива
for name in names:
    print(name)

# i = 1
# while i < len(names):
#     print(names[i])
#     i += 1

# Получение части массива
# array[:end]
print(numbers[:3]) # [1, 2, 3]
print(numbers[3:]) # [4, 5, 6, 7, 8, 9, 10]

# array[start:end]
print(numbers[1:4]) # [2, 3, 4]

# array[start:end:step]
print(numbers[0:9:2]) # [1, 3, 5, 7, 9]

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