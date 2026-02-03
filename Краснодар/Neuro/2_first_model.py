from sklearn.datasets import load_iris # готовый датасет
from sklearn.model_selection import train_test_split # распределение данных на обучающие и тестовые
from sklearn.preprocessing import StandardScaler # нормализация данных
from keras.utils import to_categorical # преобразователь в one hot encoding
import numpy as np

from keras.models import Sequential
from keras.layers import Dense

# === 1. Загрузка данных ===
# Iris датасет
# 150 примеров
# 4 признака: длина/ширина чашелистика, длина/ширина лепестка
# 3 класса: Setosa (0), Versicolor (1), Virginica (2)

iris = load_iris()
iris_data = iris.data # примеры с признаками
iris_target = iris.target # искомые классы

print(f'Total: {len(iris_data)}\n'
      f'Atrr: {iris_data.shape[1]}\n'
      f'Classes: {len(np.unique(iris_target))}\n')

print(f'Data example:\n'
      f'data: {iris_data[0]}\n'
      f'target: {iris_target[0]}\n')

# === 2. Подготовка данных ===

# train_test_split(*arrays, test_size, random_state)
# *arrays - набор массивов с данными
# test_size - процент данных, отведенных на тесты
# random_state - seed для избежания рандомизации данных на каждой итерации обучения
data_test, data_train, target_test, target_train = train_test_split(iris_data, iris_target, test_size = 0.2, random_state = 42)

# Нормализация - приведение всех входных значений в числовую вилку от -1 до 1
scaler = StandardScaler()
data_train = scaler.fit_transform(data_train) # нормализация данных (вычисление отклонений, средних значений и тд)
data_test = scaler.transform(data_test) # использование параметров из fit_transform для создания такой же нормализации для data_test

# One hot encoding - приведение целевых данных в числовой формат
# Вход: [0, 1, 2]
# Setosa (0) -> [1, 0, 0]
# Versicolor (1) -> [0, 1, 0]
# Virginica (2) -> [0, 0, 1]
target_train_cat = to_categorical(target_train, num_classes = 3)
target_test_cat = to_categorical(target_test, num_classes = 3)

print(f'Before One-hot: {target_train[0]}\n'
      f'After One-hot: {target_test_cat[0]}\n')

# === 3. Создание модели ===
model = Sequential([
    Dense(16, activation = 'relu', input_shape = (4,)),
    Dense(8, activation = 'relu'),
    Dense(3, activation = 'softmax'),
])

# model.summary() # - для просмотра статистики модели

# === 4. Компиляция ===
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)

# === 5. Обучение ===
history = model.fit(
    data_train, target_train_cat, # данные для обучения
    epochs = 100, # кол-во итераций обучения
    batch_size = 16, # вол-во данных, после который модель регулирует веса
    validation_split = 0.2, # процент данных для отслеживания переобучения
    verbose = 1 # progress bar (0 - не показывать, 1 - показывать каждую эпоху, 2 - показать время на эпоху)
)

print(f'Train complete\n'
      f'Accuracy: {history.history["accuracy"][-1]:.3f}')

# === 6. Тесты ===


