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