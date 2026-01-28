# Keras
# 1. Модель - контейнер, содержащий все данные нейронки
# 2. Слои - этапы мыслительного процесса
# 3. Компиляция - процесс настройки нейросети
# 4. Обучение
# 5. Предсказания - запрос нейросети с новыми данными

# Создание модели
from keras.models import Sequential
from keras.layers import Dense

model = Sequential([
    Dense(10, activation='relu', input_shape=(5,)),
    Dense(1, activation='sigmoid'),
])

model.summary()

# Типы активации
# 1. ReLU (Rectified Linear Unit) - если x > 0 = x, если x < 0 = 0
# 2. Sigmoid - всегда от 0 до 1
# 3. Softmax - преобразует все входные данные в вероятность, которая в сумме дает 1
# 4. Tanh - гиперболический тангенс, работает как relu, но ответ как sigmoid с разницей (от -1 до 1)

# Данные модели
print(f'Кол-во слоев: {len(model.layers)}')
for i, layer in enumerate(model.layers):
    print(f'Слой {i + 1}. {layer.name}\n'
          f'Тип слоя: {type(layer).__name__}\n'
          f'Кол-во параметров: {layer.count_params()}\n')

print(f'Всего параметров: {model.count_params()}')

# Компиляция
model.compile(
    optimizer='adam', # функция изменения весов, для избежания ошибки
        # adam - быстрый и стабильный
        # SGD - медленный, но с лучшими результатами
        # RMSprop - альтернатива adam, хорош для рекуррентных сетей
    loss='categorial_crossentropy', # что минимизировать при обучении
        # binary_crossentropy - бинарная классификация (одно из двух)
        # categorial_crossentropy - если используется больше трех классов
        # sparse_categorial_crossentropy - множество классов
    # Для регрессии
        # mse - для непрерывно обновляемых данных
        # mae - средняя абсолютная ошибка
    metrics=['accuracy'] # отслеживание качества работы
        # accuracy - точность
        # precision - точность положительных ответов
        # recall - полнота нахождения верных ответов


)