import numpy as np
import time

# amount = 500_000_000

# py_list = list(range(amount))
# py_time_start = time.time()
# py_result = [num * 2 for num in py_list]
# py_result_time = time.time() - py_time_start
# print(f'Python: {py_result_time:.5f} sec')
#
# np_arr = np.arange(amount)
# np_time_start = time.time()
# np_result = np_arr * 2
# np_result_time = time.time() - np_time_start
# print(f'Numpy: {np_result_time:.5f} sec')
#
# print(f'{py_result_time / np_result_time:.1f} times faster')


# === numPy ===
# comp_list = [1, 2, 3, 4] #
# arr_1d = np.array([1, 2, 3, 4, 5])
# print(f'Array: {arr_1d}')
# print(f'Shape: {arr_1d.shape}')
# print(f'Dims: {arr_1d.ndim}')
# print(f'Size: {arr_1d.size}')
# print(f'Dtype: {arr_1d.dtype}')
# print(f'Itemsize: {arr_1d.itemsize} byte')
# print(f'Nbytes: {arr_1d.nbytes / 1024:.3f} KB\n')
#
# arr_2d = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(f'Array: \n{arr_2d}')
# print(f'Shape: {arr_2d.shape}')
# print(f'Dims: {arr_2d.ndim}')
# print(f'Itemsize: {arr_2d.itemsize} byte')
# print(f'Nbytes: {arr_2d.nbytes / 1024:.3f} KB\n')
#
# arr_3d = np.random.randint(0, 10, (3, 5, 5))
# print(f'Array: \n{arr_3d}')
# print(f'Shape: {arr_3d.shape}')
# print(f'Dims: {arr_3d.ndim}')
# print(f'Itemsize: {arr_3d.itemsize} byte')
# print(f'Nbytes: {arr_3d.nbytes / 1024:.3f} KB\n')
#
# arr_4d = np.random.rand(1000, 256, 256, 3).astype(np.uint8)
# print(f'Array: \n{arr_4d}')
# print(f'Shape: {arr_4d.shape}')
# print(f'Dims: {arr_4d.ndim}')
# print(f'Itemsize: {arr_4d.itemsize} byte')
# print(f'Nbytes: {arr_4d.nbytes / 1024:.3f} KB\n')

# === Создание массивов ===
# 1. Из python списков (list() / [] / tuple() / ())
# np.array(list)
array = np.array(tuple(range(100)))
print(f'Array: \n{array}')

# 2. Заполнение
    # 2.1 заполнить нулями
zeros = np.zeros((5, 5))
print(f'Zeros:\n{zeros}\n')

    # 2.2 заполнить единичками
ones = np.ones((5, 5))
print(f'Ones:\n{ones}\n')

    # 2.3 заполнить конкретным числом
full = np.full((5, 5), 50)
print(f'Full:\n{full}\n')

    # 2.4 заполнить пустотой
empty_arr = np.empty((5, 5))
print(f'Empty:\n{empty_arr}\n')

# 3. Конструкторы матриц
    # 3.1 единичная диагональ
eye = np.eye(5)
print(f'Eye:\n{eye}\n')

    # 3.2 диалогальная матрица
diag = np.diag([5, 4, 3, 2, 1])
print(f'Diag:\n{diag}\n')

# 4. Последовательности
    # 4.1 аналог range()
range_arr = np.arange(10, 100, 5)
print(f'Range:\n{range_arr}\n')

    # 4.2 равномерная последовательность от start до end
lin_arr = np.linspace(0, 10, 5)
print(f'Lin:\n{lin_arr}\n')

# 5. Случайная последовательность
random_arr = np.random.rand(4, 4)
print(random_arr)

np.random.seed(8) # seed для одинаковой генерации
random_int = np.random.randint(10, 100, (5, 10))
print(random_int)
np.random.seed(None) # отключить seed

# === Типы данных ===
# Целые числа
int8 = np.array([1, 2, 3, 4, 5], dtype=np.int8)
int32 = np.arange(1_000_000, dtype=np.int32)
int64 = np.array([1, 2, 3, 4, 5], dtype=np.int64)

print(f'int8: значение: {int8.itemsize} байт, массив: {int8.nbytes} байт') # содержит значения от -128 до 127
print(f'int32: значение: {int32.itemsize} байт, массив: {int32.nbytes / 1024**2:.2f} М/байт') # содержит значения от -2^31 до 2^31-1
print(f'int64: значение: {int64.itemsize} байт, массив: {int64.nbytes} байт') # содержит значения от -2^63 до 2^63-1

# Дробные чисел
float16 = np.array([1, 2, 3, 4, 5], dtype=np.float16) # ~3 знака после запятой
float32 = np.array([1, 2, 3, 4, 5], dtype=np.float32) # ~7 знаков
float64 = np.array([1, 2, 3, 4, 5], dtype=np.float64) # ~13-15 знаков

print(f'float16: значение: {float16.itemsize} байт, массив: {float16.nbytes} байт')
print(f'float32: значение: {float32.itemsize} байт, массив: {float32.nbytes} байт')
print(f'float64: значение: {float64.itemsize} байт, массив: {float64.nbytes} байт')

# битовые значения
uint8 = np.array([1, 2, 3, 4, 5], dtype=np.uint8) # значения от 0 до 255
print(f'uint8: значение: {uint8.itemsize} бит, массив: {uint8.nbytes} бит')

# конвертация типов
# .astype(тип)
float_16to64 = float16.astype(np.float64)
print(float_16to64.dtype)


# Задание:
# 1. Создайте 1D массив из списка [10, 20, 30, 40, 50]
# 2. Создайте 2D массив 4×3 (4 строки, 3 столбца) из последовательных чисел от 1 до 12
# 3. Создайте 3D массив размером (2, 3, 4) заполненный случайными числами от 0 до 1
# 4. Для каждого массива выведите:
#    - shape (форму)
#    - ndim (количество измерений)
#    - size (общее количество элементов)
#    - dtype (тип данных)
#    - Размер в памяти (в байтах)

# Задание:
# Вы работаете с датасетом изображений: 1000 RGB изображений размером 256×256.
# 1. Создайте массив с типом float64 (по умолчанию)
# 2. Создайте такой же массив с типом float32
# 3. Создайте такой же массив с типом uint8 (целые 0-255 для изображений)
# 4. Сравните использование памяти всех трёх вариантов
# 5. Вычислите процент экономии при использовании uint8 вместо float64