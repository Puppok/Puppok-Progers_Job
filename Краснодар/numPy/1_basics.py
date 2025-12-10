import numpy as np
import time

# Сравнение скорости работы списков python и массивов numpy

n = 100_000_000

# Python списки
# py_list = list(range(n)) # список на 10млн элементов
# py_start = time.time() # начало отсчета времени
# py_result = [el * 2 for el in py_list] # умножение каждого элемента списка на 2
# py_end = time.time() - py_start # просчет времени выполнения прошлого действия
# print(f'Python: {py_end:.8f} сек') # вывод времени работы (2 знака после запятой)

# numPy массивы
# np_arr = np.array(n)
# np_start = time.time() # 1765358762
# np_result = np_arr * 2
# np_end = time.time() - np_start # 1765358765 - 1765358762 = 3
# print(f'NumPy: {np_end:.8f} сек')
#
# print(f'Разница в {py_end / np_end:.1f} раз')

# === NumPy ===
# ndarray (N dimensional array) - массив N размерности
x = [1, 2, 3, 4, 5] # стандартный python список
n_arr = np.array([1, 2, 3, 4, 5]) # numpy массив
# базовые значения массива
print(f'Массив: {n_arr}')
print(f'Форма: {n_arr.shape}')
print(f'Размерность: {n_arr.ndim}')
print(f'Размер: {n_arr.size}')
print(f'Тип сжатия: {n_arr.dtype}')

# пример с 2d массивом
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f'\n2d форма: {arr_2d.shape}')
print(f'2d Размерность: {arr_2d.ndim}')


# --- Способы создания массивов ---
# 1. Из python списков ([] / list() / ()), используя np.array(список)
# Важно! при создании 2d и более массива, строки массива должны быть одинаковой длины

# 2. Заполнение значениями
    # • заполнение нулями (инициализация массива, создание маски)
zero_arr = np.zeros((4, 6))
print(zero_arr)

    # • заполнение единицами (веса нейросети, нормализация)
ones_arr = np.ones((4, 6))
print(ones_arr)

    # • заполнение конкретным значением (для тестирований, доп. просчетов)
twelve_arr = np.full((3, 3), 12)
print(twelve_arr)

    # • создание пустого массива (только если сразу перезаписать или заполнить значениями)
empty_arr = np.empty((3, 3))
print(empty_arr)

# 3. Специальные конструкторы матриц
    # • диагональ единиц
ones_diag = np.eye(4)
print(ones_diag)

    # • диагональная матрица значений
diag = np.diag([1, 23, 67, 9])
print(diag)

# 4. Через последовательность чисел
    # • arange() - аналог range()
arange_arr = np.arange(10, 20, 2) # от 10 до 20 с шагом 2
print(arange_arr)

    # • linspace(start, finish, N) - последовательность N чисел от start до finish равномерно
lin_arr = np.linspace(0, 1, 5)
print(lin_arr)

    # • logspace - логарифмическая последовательность (как linspace, но через логарифмы)
log_arr = np.logspace(1, 5, 8)
print(log_arr)

# 5. Через случайную последовательность
    # • равномерное распределение
np.random.seed(15) # создания seed для одинаковых результатов при каждом запуске
random_arr = np.random.rand(5) # линейный массив на 5 элементов со случайными значениями от 0 до 1
print('random:', random_arr)

# TODO: случайные целые + случайный выбор из списка + reshape для linspace