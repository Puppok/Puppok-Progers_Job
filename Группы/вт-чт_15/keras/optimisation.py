from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

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

# Тесты разных конфигураций
config_test_results = []
for layer_config, name in config:
    test_config = create_and_train_model(layer_config, name, x_test, x_train, y_test_cat, y_train_cat)
    config_test_results.append(test_config)

for result in config_test_results:
    print(f'Config name: {result["name"]}\n'
          f'Test accuracy: {result["test_accuracy"]:.4f}\n'
          f'Test loss: {result["test_loss"]:.4f}\n'
          f'Params: {result["params"]}\n'
          f'Val accuracy: {result["val_accuracy"]:.4f}\n')

# Определение лучшей модели
best_result = max(config_test_results, key = lambda config: config["test_accuracy"])
print(f'Best config name: {best_result["name"]}\n'
      f'Best test accuracy: {best_result["test_accuracy"]:.4f}\n'
      f'Best val accuracy: {best_result["val_accuracy"]:.4f}\n')

# Визуализация
fig, ax = plt.subplots(figsize = (12, 6))

names = [result['name'] for result in config_test_results]
test_acc = [result['test_accuracy'] for result in config_test_results]
params = [result['params'] for result in config_test_results]

columns = range(len(config_test_results))
bars = ax.bar(columns, test_acc, color = 'blue', edgecolor = 'navy', linewidth = 1.5)

best_id = names.index(best_result['name'])
bars[best_id].set_color('gold')
bars[best_id].set_edgecolor('orange')

ax.set_xlabel('Architecture', fontsize = 12)
ax.set_ylabel('Test Accuracy', fontsize = 12)
ax.set_title('Comparison', fontsize = 14, fontweight = 'bold')

ax.set_xticks(columns)
ax.set_xticklabels(names, rotation = 45, ha = 'right')
ax.set_ylim((0.9, 1.0))
ax.grid(axis = 'y', alpha = 0.3)