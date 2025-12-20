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

# Создание массивов
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