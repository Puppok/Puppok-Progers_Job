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
# reshape - преобразует линейный массив в матрицу (можно использовать с arange, linspace, logspace)
reshape_arr = np.linspace(10, 20, 30).reshape(5, 6)
print('reshape', reshape_arr)

    # • logspace - логарифмическая последовательность (как linspace, но через логарифмы)
log_arr = np.logspace(1, 5, 8)
print(log_arr)

# 5. Через случайную последовательность
    # • равномерное распределение
np.random.seed(15) # создания seed для одинаковых результатов при каждом запуске
random_arr = np.random.rand(5) # линейный массив на 5 элементов со случайными значениями от 0 до 1
print('random:', random_arr)

# rand() принимает размерность массива, можно создать любую величину
random_3d = np.random.rand(3, 3, 2)
print('random3d:', random_3d)

# заполнить случайными числами больше 0 и 1 (в примере от 5 до 10)
random_big = (5 + np.random.rand(2, 3) * 10)
print('randombig:', random_big)

# --- Типы данных ---
# Целые числа
int8 = np.array([1, 2, 3], dtype=np.int8)
int32 = np.array([1, 2, 3], dtype=np.int32)
int64 = np.array([1, 2, 3], dtype=np.int64)

print(f'int8: {int8.itemsize} байт, диапазон значений: -128 - 127')
print(f'int32: {int32.itemsize} байт, диапазон значений: -2^31 - 2^31-1')
print(f'int32: {int64.itemsize} байт, диапазон значений: -2^63 - 2^63-1')

# Дробные числа
float16 = np.array([1, 2, 3.746875978648764], dtype=np.float16) # 3 знака после запятой
float32 = np.array([1, 2, 3.746875978648764], dtype=np.float32) # 7 знаков
float64 = np.array([1, 2, 3.746875978648764], dtype=np.float64) # 8 знаков

print(f'float16: {float16.itemsize}, {float16}')
print(f'float32: {float32.itemsize}, {float32}')
print(f'float64: {float64.itemsize}, {float64}')

# Битовый тип
uint8 = np.array([1, 2, 3], dtype=np.uint8)
print(f'uint8: {uint8.itemsize} бит, диапазон значений: 0 - 255')

# astype(тип) - преобразует значения массива к указанному типу (если int - дробная часть обрезается)
test_type = (5 + np.random.rand(2, 3) * 10).astype(int)
print(test_type)

