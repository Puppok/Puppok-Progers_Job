from sklearn.datasets import load_iris # пример датасета
from sklearn.model_selection import train_test_split # разделитель данных на тестовые и обучающие
from sklearn.preprocessing import StandardScaler # нормализатор (что то на математическом)
from keras.utils import to_categorical # преобразователь меток в one-hot encoding (представление данных в виде чисел)
import numpy as np

# Полный pipeline создания нейронки
# 1. === Загрузка данных ===
iris = load_iris()
x = iris.data
y = iris.target

# Iris датасет содержит:
# 150 примеров цветов
# 4 признака:
    # длина чашелистика, ширина чашелистика, длина лепестка, ширина лепестка
# 3 класса:
    # Setosa, Vertisicolor, Virginica

print(f'Примеров: {len(x)}\n'
      f'Признаки: {x.shape[1]}\n'
      f'Классы: {len(np.unique(y))}')

print(f'Примеры данных:\n'
      f'x[0]: {x[0]}\n'
      f'y[0]: {y[0]} (класс)\n')

# === 2. Подготовка данных ===
# train_test_split(массивы данных, процент данных для теста, random_seed)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
