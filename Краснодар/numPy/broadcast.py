import numpy as np

# 1. Скаляр + массив
arr = np.array([1, 2, 3, 4, 5])
result_arr = arr + 10 # 10 - скаляр, растягивается на массив по кол-ву элементов arr
print(result_arr) # [11 12 13 14 15]

# 2. Матрица + вектор
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
vector = np.array([10, 20, 30])
print(matrix + vector)
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]

# Столбец + строка
col = np.array([
    [1],
    [2],
    [3],
    [4]
])
row = np.array([[10, 20, 30]])
print(col + row)
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]
#  [14 24 34]]

# Пример: добавить шум разной интенсивности набору изображений
np.random.seed(1)

images = np.random.rand(10, 64, 64) # 10 картинок 64х64
# print(f'Images: \n{images}')

noise = np.random.rand(10, 1, 1)
# print(f'Noise: \n{noise}')

# сложение массивов через broadcast
noisy_images = images + noise
print(f'Noisy images: \n{noisy_images}')

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
weights = np.array([0.1, 0.5, 1.0])

# перемножение массивов через broadcast
result = matrix * weights
print(result)