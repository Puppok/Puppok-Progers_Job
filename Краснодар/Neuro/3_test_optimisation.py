from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.utils import to_categorical

configs = [
    ([(8, 'relu'), (8, 'relu'), (3, 'softmax')], 'Shallow-8'),
    ([(8, 'relu'), (16, 'relu'), (3, 'softmax')], 'Shallow-16'),
    ([(8, 'relu'), (32, 'relu'), (3, 'softmax')], 'Shallow-32'),

    ([(8, 'relu'), (16, 'relu'), (8, 'relu'), (3, 'softmax')], 'Deep-16-8'),
    ([(8, 'relu'), (32, 'relu'), (16, 'relu'), (3, 'softmax')], 'Deep-32-16'),
    ([(8, 'relu'), (64, 'relu'), (32, 'relu'), (3, 'softmax')], 'Deep-64-32'),

    ([(8, 'relu'), (32, 'relu'), (16, 'relu'), (8, 'relu'), (3, 'softmax')], 'VeryDeep-32-16-8'),
    ([(8, 'relu'), (64, 'relu'), (32, 'relu'), (16, 'relu'), (8, 'relu'), (3, 'softmax')], 'VeryDeep-64-32-16-8'),
    ([(8, 'relu'), (128, 'relu'),(64, 'relu'), (32, 'relu'), (16, 'relu'), (8, 'relu'), (3, 'softmax')], 'VeryDeep-128-64-32-16-8'),
]

def create_and_train_model(layer_config, name, data_train, target_train, data_test, target_test):
    model = Sequential()

    # Входной слой
    neurons, activation = layer_config[0]
    model.add(Dense(neurons, activation = activation, input_shape = (4,)))

    # Скрытые слои
    for neuron, activation in layer_config[1:-2]:
        model.add(Dense(neuron, activation = activation))

    # Выходной слой
    neurons, activation = layer_config[-1]
    model.add(Dense(neurons, activation = activation))

    # Компиляция
    model.compile(
        optimizer = 'adam',
        loss = 'binary_crossentropy',
        metrics = ['accuracy']
    )

    # Обучение
    model_learn = model.fit(
        data_train, target_train,
        epochs = 100,
        batch_size = 16,
        validation_split = 0.2,
        verbose = 0
    )

    # Тесты
    test_loss, test_acc = model.evaluate(data_test, target_test, verbose = 0)

    return {
        'name': name,
        'test_loss': test_loss,
        'test_acc': test_acc,
        'params': model.count_params(),
        'val_acc': model_learn.history['val_accuracy'][-1]
    }


# Подгрузка данных
iris = load_iris()
iris_data = iris.data
iris_target = iris.target

data_test, data_train, target_test, target_train = train_test_split(iris_data, iris_target, test_size = 0.2, random_state = 42)

scaler = StandardScaler()
data_train = scaler.fit_transform(data_train)
data_test = scaler.transform(data_test)

target_train_cat = to_categorical(target_train, num_classes = 3)
target_test_cat = to_categorical(target_test, num_classes = 3)

# Тесты конфигов
test_results = []
for config, name in configs:
    config_test = create_and_train_model(config, name, data_train, target_train_cat, data_test, target_test_cat)
    test_results.append(config_test)

    print(f'Config name: {config_test['name']}\n'
          f'Test loss: {config_test["test_loss"]}\n'
          f'Test accuracy: {config_test["test_acc"]}\n'
          f'Params: {config_test["params"]}\n'
          f'Val accuracy: {config_test["val_acc"]}\n')

# Находим наилучший результат
best_result = max(test_results, key = lambda x: x['test_acc'])
print(f'Best config: {best_result["name"]}\n'
      f'Test acc: {best_result["test_acc"]}\n')

# Визуализация сравнения
fig, ax = plt.subplots(figsize = (12, 6)) # создание холста и графика

# получение данных для графика (названия, результаты тестов, кол-во параметров обучения)
names = [result['name'] for result in test_results]
test_acc = [result['test_acc'] for result in test_results]
params = [result['params'] for result in test_results]

column_position = range(len(test_results)) # позиции столбцов графика
bars = ax.bar(column_position, test_acc, color = 'blue', edgecolor = 'navy', linewidth = 1.5) # создание столбца графика

# Подсветка лучшего результата
best_index = names.index(best_result['name'])
bars[best_index].set_color('gold')
bars[best_index].set_edgecolor('orange')

# Заголовки
ax.set_xlabel('Config', fontsize = 12)
ax.set_ylabel('Test accuracy', fontsize = 12)
ax.set_title('Config comparison', fontsize = 14, fontweight = 'bold')

# Позиции делений столбцов
ax.set_xticks(column_position)
ax.set_xticklabels(names, rotation = 45, ha = 'right')
ax.set_ylim((0.2, 1))

ax.grid(axis = 'y', alpha = 0.3)

# Добавление значений
for i, (acc, params) in enumerate(zip(test_acc, params)):
    ax.text(i, acc + 0.005, f'{acc:.3f}\n{params}p', ha = 'center', va = 'bottom', fontsize = 9)

# Отрисовка графика
plt.tight_layout()
plt.savefig('plot.png', dpi=150, bbox_inches='tight')
# plt.show()


