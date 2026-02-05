from keras.models import Sequential
from keras.layers import Dense

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.utils import to_categorical
import numpy as np

config = [
    ([(8, 'relu'),  (8, 'relu'), (3, 'softmax')], 'Shallow-8'),
    ([(16, 'relu'), (16, 'relu'), (3, 'softmax')], 'Shallow-16'),
    ([(32, 'relu'), (32, 'relu'), (3, 'softmax')], 'Shallow-32'),

    ([(16, 'relu'), (16, 'relu'), (8, 'relu'), (3, 'softmax')], 'Deep-16-8'),
    ([(32, 'relu'), (32, 'relu'), (16, 'relu'), (3, 'softmax')], 'Deep-32-16'),
    ([(64, 'relu'), (64, 'relu'), (32, 'relu'), (3, 'softmax')], 'Deep-64-32'),

    ([(64, 'relu'), (32, 'relu'), (16, 'relu'), (8, 'relu'), (3, 'softmax')], 'Very_Deep-64-32-16-8'),
    ([(128, 'relu'), (64, 'relu'), (32, 'relu'), (16, 'relu'), (8, 'relu'), (3, 'softmax')], 'Very_Deep-128-64-32-16-8'),
]

def create_and_train_model(layer_config, name, data_test, data_train, target_test_cat, target_train_cat):
    model = Sequential()

    # Первый слой
    neurons, activation = layer_config[0]
    model.add(Dense(neurons, activation = activation, input_shape = (4,)))

    # Скрытые слои
    for neurons, activation in layer_config[1:-2]:
        model.add(Dense(neurons, activation = activation))

    # Выходной слой
    neurons, activation = layer_config[-1]
    model.add(Dense(neurons, activation = activation))

   # Компиляция
    model.compile(
        optimizer = 'adam',
        loss = 'categorical_crossentropy',
        metrics = ['accuracy']
    )

    # Обучение
    model_learn = model.fit(
        data_train, target_train_cat,
        epochs = 100,
        batch_size = 16,
        validation_split = 0.2,
        verbose = 1,
    )

    # Тесты
    test_loss, test_acc = model.evaluate(data_test, target_test_cat, verbose = 1)

    return {
        'name': name,
        'test_accuracy': test_acc,
        'test_loss': test_loss,
        'params': model.count_params(),
        'val_accuracy': model_learn.history['val_accuracy'][-1],
    }

# Тесты на данных
iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

y_train_cat = to_categorical(y_train, num_classes = 3)
y_test_cat = to_categorical(y_test, num_classes = 3)
