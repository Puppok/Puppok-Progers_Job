# 1. Модель - контейнер, содержащий все компоненты нейронки
# 2. Слои - строительные блоки нейронки
# 3. Компиляция - процесс настройки обучения нейронки
# 4. Обучение
# 5. Предсказания - запрос с новыми данными

import numpy as np
import sklearn
from keras.models import Sequential # класс для создания последовательных моделей
from keras.layers import Dense # создание полносвязных слоев

# Создание модели
# model = Sequential([
#     Dense(10, activation='relu', input_shape=(5,)),
#     Dense(1, activation='sigmoid')
# ])
#
# model.summary()

# Dense слой - полносвязный слой, где каждый нейрон связан со всеми нейронами предыдущего слоя
# units - кол-во нейронов в слое
# activation - функция активации (relu, sigmoid, tanh, softmax)
    # процесс преобразования суммы входных данных
    # relu (Rectified Linear Unit) - если x>0 -> x, если x<0 -> 0
    # sigmoid - всегда от 0 до 1, используется для определения вероятностей
    # tanh - всегда от -1 до 1, используется как альтернатива relu
    # softmax - для многоклассовой классификации (преобразует числа в вероятности, сумма которых = 1)
# input_shape - размер входных данных (только для первого слоя)

# Dropout
# отключение части нейронов во время обучения, защита от переобучения

# Создание модели
model = Sequential([
    Dense(10, activation='relu', input_shape=(4,)),
    Dense(3, activation='softmax')
])

print(f'Структура модели: \n{model.summary()}')

print(f'Анализ модели:')
print(f'Кол-во слоев: {len(model.layers)}')
for i, layer in enumerate(model.layers):
    print(f'Слой {i + 1}.: {layer.name}\n'
          f'Тип слоя: {type(layer).__name__}\n'
          # f'Выходные данные: {layer.output_shape}\n'
          f'Кол-во параметров: {layer.count_params()}\n')

print(f'Всего параметров: {model.count_params()}')

# Слой 1 - (4 входа * 10 нейронов) + 10 bias = 50
# Слой 2 - (10 входов * 3 нейрона) + 3 bias = 33
print(f'Ожидаем: {4 * 10 + 10} + {10 * 3 + 3}')

# Компиляция модели
model.compile(
    optimizer = 'adam', # как обучаем модель
    loss = 'categorical_crossentropy', # что минимизируем
    metrics = ['accuracy'] # что отслеживаем
)

# Виды optimizer (процесс изменения весов ради уменьшения ошибки)
# adam
# SGD
# RMSprop

