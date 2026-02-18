import matplotlib.pyplot as plt # для графиков

from keras.models import Sequential
from keras.layers import Dense

# преобразователь меток в one-hot encoding (представление данных в виде чисел)
from keras.utils import to_categorical

from sklearn.datasets import load_iris # пример датасета
from sklearn.model_selection import train_test_split # разделитель данных на тестовые и обучающие
from sklearn.preprocessing import StandardScaler # нормализатор (что то на математическом)
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

print(f'Data: {x}')
print(f'Target: {y}')

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
      epochs = 1, # кол-во эпох обучения (повторений цикла)
      batch_size = 100, # спустя сколько примеров произойдет обновление данных
      validation_split = 0.2, # 20% данных для определения степени переобучения
      verbose = 1 # 0 - не показывать progress bar
            # 1 - progress bar для каждой эпохи
            # 2 - время выполнения каждой эпохи
)

# === 6. Тестирование ===
test_loss, test_accuracy = model.evaluate(x_test, y_test_cat, verbose = 1)
print(f'Test loss: {test_loss:.4f}\n'
      f'Test accuracy: {test_accuracy:.4f} ({test_accuracy * 100:.1f}%)')

# # === 7. Предсказания ===
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

# === Визуализация ===
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
train_loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(1, len(train_loss) + 1)

# создание графика: 1 строка, 2 колонки, размеры 14x5" (дюймов)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (14, 5))

# отрисовка графика 1
ax1.plot(epochs_range, train_acc, 'b-', label = 'Train accuracy', linewidth = 2)
# epochs_range - кол-во эпох обучения
# train_acc/val_acc - данные для отрисовки
# 'b-'/'r-' - синяя/красная линия
# label - подпись для легенды
# linewidth - толщина линии
ax1.plot(epochs_range, val_acc, 'r-', label = 'Validation accuracy', linewidth = 2)
ax1.set_title('Model accuracy', fontsize = 14, fontweight = 'bold') # заголовок графика
ax1.set_xlabel('Epoch') # подпись оси X
ax1.set_ylabel('Accuracy') # подпись оси Y
ax1.legend() # показать легенду
ax1.grid(True, alpha = 0.3) # отрисовка сетки с 30% прозрачности

# отрисовка графика 2
ax2.plot(epochs_range, train_loss, 'b-', label = 'Train loss', linewidth = 2)
ax2.plot(epochs_range, val_loss, 'r-', label = 'Validation loss', linewidth = 2)
ax2.set_title('Model accuracy', fontsize = 14, fontweight = 'bold')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')
ax2.legend()
ax2.grid(True, alpha = 0.3)

plt.tight_layout()
plt.show()
#
# # анализ обучения
# print(f'Top val_accuracy: {max(val_acc):.4f} (Epoch: {np.argmax(val_acc)+1})\n'
#       f'Final accuracy: {val_acc[-1]:.4f}')
#
# # проверка на переобучение
# diff = train_acc[-1] - val_acc[-1]
# if diff > 0.1:
#       print(f'Есть переобучение:\n'
#             f'Train accuracy: {train_acc[-1]:.4f}\n'
#             f'Val accuracy: {val_acc[-1]:.4f}\n'
#             f'Difference: {diff:.4f}')
# else:
#       print('Good')