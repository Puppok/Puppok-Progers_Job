from sklearn.datasets import load_iris # готовый датасет
from sklearn.model_selection import train_test_split # распределение данных на обучающие и тестовые
from sklearn.preprocessing import StandardScaler # нормализация данных
from keras.utils import to_categorical # преобразователь в one hot encoding
import numpy as np

from keras.models import Sequential
from keras.layers import Dense

import matplotlib.pyplot as plt

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
# .evaluate(test_data, test_output, progress_bar) - тестирует обученную модель на тестовых данных
test_loss, test_accuracy = model.evaluate(data_test, target_test_cat, verbose = 0)

print(f'\nLoss test result: {test_loss:.4f}\n'
      f'Accuracy test result: {test_accuracy:.3f} ({test_accuracy*100:.1f}%)\n')

# === 7. Предсказания ===
# .predict(new_data, progress_bar) - получить ответ по новым данным
predictions = model.predict(data_test[10:21], verbose = 0)

for i in range(10):
    pred_class = np.argmax(predictions[i])
    true_class = target_test[i]
    confidence = predictions[i][pred_class]

    status = 'Ok' if pred_class == true_class else 'Fail'

    print(f'Example {i + 1}: {status}\n'
          f'True class: {true_class}\n'
          f'Predicted class: {pred_class}\n'
          f'Confidence: {confidence*100:.1f}%\n'
          f'Model answer: {predictions[i]}\n')


# === Визуализация ===
train_acc = history.history['accuracy']
train_loss = history.history['loss']
val_acc = history.history['val_accuracy']
val_loss = history.history['val_loss']

epochs_range = range(1, len(train_acc) + 1)

# создание графика
# .subplots(rows, columns, figsize = (width, height))
# rows - строки
# columns - колонки графика
# figsize - размер изображения в дюймах
fig, (acc, loss) = plt.subplots(1, 2, figsize = (14, 5))

# рисуем графики
acc.plot(epochs_range, train_acc, 'b-', label = 'Train accuracy', linewidth = 2)
# epochs_range - кол-во эпох
# train_acc - данные для отрисовки
# b-/r- - синяя/красная линия
# label - название для легенды
# linewidth - толщина линии графика
acc.plot(epochs_range, val_acc, 'r-', label = 'Validation accuracy', linewidth = 2)
acc.set_title('Model Accuracy', fontsize = 14, fontweight = 'bold') # заголовок графика
acc.set_xlabel('Epoch') # подпись оси X
acc.set_ylabel('Accuracy') # подпись оси Y
acc.legend() # создание легенды из параметров label
acc.grid(True, alpha = 0.3) # отображение сетки с 30% прозрачности

loss.plot(epochs_range, train_loss, 'b-', label = 'Train loss', linewidth = 2)
loss.plot(epochs_range, val_loss, 'r-', label = 'Validation loss', linewidth = 2)
loss.set_title('Model Accuracy', fontsize = 14, fontweight = 'bold')
loss.set_xlabel('Epoch')
loss.set_ylabel('Accuracy')
loss.legend()
loss.grid(True, alpha = 0.3)

plt.tight_layout() # подготовка графика, подстраивание размеров
plt.show() # отрисовка графика

