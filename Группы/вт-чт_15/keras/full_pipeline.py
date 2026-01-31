from keras.models import Sequential
from keras.layers import Dense

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

# нормализация данных (числовой формат)
scaler = StandardScaler()

# вычисляет среднее и стандартное отклонение и затем нормализует (приводит к общему числовому диапазону)
x_train = scaler.fit_transform(x_train)

# использует те же параметры, что были получены на x_train
x_test = scaler.transform(x_test)

# one hot encoding - процесс преобразования нечисловых данных в числовые
# [красный] -> [1, 0, 0]
# [желтый] -> [0, 1, 0]
# [зеленый] -> [0, 0, 1]
y_train_cat = to_categorical(y_train, num_classes = 3)
y_test_cat = to_categorical(y_test, num_classes = 3)

print(f'Train: {x_train.shape}, {y_train_cat.shape}')
print(f'Test: {x_test.shape}, {y_test_cat.shape}')

print(f'Before one hot: {y_train[0]}')
print(f'After one hot: {y_train_cat[0]}')

# === 3. Создание модели ===
model = Sequential([
      Dense(16, activation = 'relu', input_shape=(4,)),
      Dense(8, activation = 'relu'),
      Dense(3, activation = 'softmax')
])

model.summary()

# === 4. Компиляция ===
model.compile(
      optimizer = 'adam',
      loss = 'categorical_crossentropy',
      metrics = ['accuracy']
)

# === 5. Обучение ===
history = model.fit(
      x_train, y_train_cat, # данные для обучения
      epochs = 100, # кол-во эпох обучения (повторений цикла)
      batch_size = 16, # спустя сколько примеров произойдет обновление данных
      validation_split = 0.2, # 20% данных для определения степени переобучения
      verbose = 1 # не показывать progress bar
            # 1 - один progress bar на все обучения
            # 2 - progress bar для каждой эпохи
)

# === 6. Тестирование ===
test_loss, test_accuracy = model.evaluate(x_test, y_test_cat, verbose = 1)
print(f'Test loss: {test_loss:.4f}\n'
      f'Test accuracy: {test_accuracy:.4f} ({test_accuracy * 100:.1f}%)')

# === 7. Предсказания ===
predictions = model.predict(x_test[:5], verbose = 1)

for i in range(5):
      pred_class = np.argmax(predictions[i])
      true_class = y_test[i]
      confidence = predictions[i][pred_class]

      status = 'Ok' if pred_class == true_class else 'Wrong'

      print(f'Example: {i + 1}, {status}\n'
            f'True class: {true_class}\n'
            f'Predicted class: {pred_class}\n'
            f'Confidence: {confidence:.2f}%\n'
            f'Chance: {predictions[i]}\n')
