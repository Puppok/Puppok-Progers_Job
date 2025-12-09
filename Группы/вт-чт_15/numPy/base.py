import numpy as np
import time

amount = 100_000_000

# Просчет времени работы через python
# py_list = list(range(amount))
# py_start = time.time()
# py_result = [x * 2 for x in py_list]
# py_time = time.time() - py_start
# print(f'Time python: {py_time:.4f} сек')

# Просчет времени работы через numPy
# np_list = np.arange(amount)
# np_start = time.time()
# np_result = np_list * 2
# np_time = time.time() - np_start
# print(f'Time numPy: {np_time:.4f} сек')
#
# print(f'Dif in {py_time / np_time:.1f} times')

# NumPy
# ndarray - N dimensional array
narray = np.array([1 ,2, 3, 4]) # базовое создание массива
# print(narray)
# print(f'Shape: {narray.shape}') # форма массива (строки, столбцы, слои)
# print(f'Dims: {narray.ndim}') # кол-во измерений
# print(f'Size: {narray.size}') # размер массива (кол-во элементов)
# print(f'Types: {narray.dtype}') # тип данных массива

n2array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# print(f'Shape: {n2array.shape}')
# print(f'Dims: {n2array.ndim}')

# Способы создания массивов
# 1. Из python списков ( [] / list() / () ), c помощью np.array(список)
# 2. Заполнение
    # • заполнение нулями
zeros = np.zeros((5, 8))
print(zeros)

    # • заполнение единицами
ones = np.ones((3, 6))
print(ones)

    # • заполнение конкретным числом
full = np.full((2, 4), 5)
print(full)

    # • пустой массив
empty = np.empty((3, 3))
print(empty)

# 3. Конструктор матрицы
    # • Единичная диагональ
indent = np.eye(5)
print('Единичная диагональ\n', indent)

    # • Диагональная матрица
diagonal = np.diag([1, 2, 3])
print('Диагональ\n', diagonal)

# 4. Последовательности чисел
    # • дипазон
# arr = np.arange(0, 20, 3) # (start, finish, step)
# print(arr)
pep = np.arange(0, 10).reshape(2, 5) # сформировать таблицу из линейного массива
print(pep)

    # • равномерные N чисел
# arr = np.linspace(0, 10, 5) # формирует равный диапазон от 0 до 10 из 5 чисел
# print(arr)

    # • логарифмическая шкала
# arr = np.logspace(1, 5, 5)
# print(arr)

# 5. Случайные числа
    # • случайность через seed
np.random.seed(20) # создания seed для генерации
print(np.random.rand(5))

    # • пседвослучайная последовательность
np.random.seed(None)
print(np.random.randn(5))


# Типы данных
int8 = np.arange(5, dtype=np.int8) # хранение в системе 8 байт (-128 до 127)
print(int8.itemsize) # вывод размера массива в памяти

int32 = np.arange(5, dtype=np.int32) # хранение в системе 32 байт (-2^31 до 2^31-1)
print(int32.itemsize)

int64 = np.arange(5, dtype=np.int64) # хранение в системе 64 байт (диапазон очень большой)
print(int64.itemsize)

unit8 = np.arange(5, dtype=np.uint8) # хранение в системе 8 бит (0 до 255)
print(unit8.itemsize)

float16 = np.array([1.5, 2.7, 23.5], dtype=np.float16) # ~3 знака точности
print(float16.itemsize)

float32 = np.array([1.5, 2.7, 23.5], dtype=np.float32) # ~7 знаков точности
print(float32.itemsize)

float64 = np.array([1.5, 2.7, 23.5], dtype=np.float64) # ~15 знаков точности
print(float64.itemsize)

# .astype(int) - обрезает дробную часть (4.7 -> 4)
test = np.array([2.5, 6.8, 23.5])
print(test.astype(int))

# Задачи
# 1. Создайте 1D массив из списка [10, 20, 30, 40, 50]
# 2. Создайте 2D массив 4×3 (4 строки, 3 столбца) из последовательных чисел от 1 до 12
# 3. Создайте 3D массив размером (2, 3, 4) заполненный случайными числами от 0 до 1
# 4. Для каждого массива выведите:
#    - shape (форму)
#    - ndim (количество измерений)
#    - size (общее количество элементов)
#    - dtype (тип данных)
#    - Размер в памяти (в байтах)

# Вы работаете с датасетом изображений: 1000 RGB изображений размером 256×256.
# 1. Создайте массив с типом float64 (по умолчанию)
# 2. Создайте такой же массив с типом float32
# 3. Создайте такой же массив с типом uint8 (целые 0-255 для изображений)
# 4. Сравните использование памяти всех трёх вариантов
# 5. Вычислите процент экономии при использовании uint8 вместо float64