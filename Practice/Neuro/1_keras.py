from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("="*60)
print("ШАГ 1: ЗАГРУЗКА ДАННЫХ")
print("="*60)

iris = load_iris()
X = iris.data      # 4 признака
y = iris.target    # 3 класса (0, 1, 2)

print(f"Примеров: {len(X)}")
print(f"Признаков: {X.shape[1]}")
print(f"Классов: {len(np.unique(y))}")

print(f"\nПример данных:")
print(f"X[0]: {X[0]}")
print(f"y[0]: {y[0]} (класс)")

print("\n" + "="*60)
print("ШАГ 2: ПОДГОТОВКА ДАННЫХ")
print("="*60)

# Разделить на train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Нормализация (важно для нейросетей!)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# One-hot encoding меток
# [0] → [1, 0, 0]
# [1] → [0, 1, 0]
# [2] → [0, 0, 1]
y_train_cat = to_categorical(y_train, num_classes=3)
y_test_cat = to_categorical(y_test, num_classes=3)

print(f"Train: {X_train.shape}, {y_train_cat.shape}")
print(f"Test: {X_test.shape}, {y_test_cat.shape}")

print(f"\nДо one-hot: {y_train[0]}")
print(f"После one-hot: {y_train_cat[0]}")

print("\n" + "="*60)
print("ШАГ 3: СОЗДАНИЕ МОДЕЛИ")
print("="*60)

model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')
])

model.summary()

print("\n" + "="*60)
print("ШАГ 4: КОМПИЛЯЦИЯ")
print("="*60)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("✅ Модель скомпилирована")
print("  Optimizer: adam")
print("  Loss: categorical_crossentropy")
print("  Metrics: accuracy")

print("\n" + "="*60)
print("ШАГ 5: ОБУЧЕНИЕ")
print("="*60)

history = model.fit(
    X_train, y_train_cat,
    epochs=100,
    batch_size=16,
    validation_split=0.2,
    verbose=0
)

print(f"✅ Обучение завершено!")
print(f"  Эпох: 100")
print(f"  Финальная точность на train: {history.history['accuracy'][-1]:.4f}")
print(f"  Финальная точность на val: {history.history['val_accuracy'][-1]:.4f}")

print("\n" + "="*60)
print("ШАГ 6: ОЦЕНКА НА ТЕСТЕ")
print("="*60)

test_loss, test_accuracy = model.evaluate(X_test, y_test_cat, verbose=0)

print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.1f}%)")

print("\n" + "="*60)
print("ШАГ 7: ПРИМЕРЫ ПРЕДСКАЗАНИЙ")
print("="*60)

# Предсказать для первых 5 примеров
predictions = model.predict(X_test[:5], verbose=0)

for i in range(5):
    pred_class = np.argmax(predictions[i])
    true_class = y_test[i]
    confidence = predictions[i][pred_class]

    status = "✅" if pred_class == true_class else "❌"

    print(f"\nПример {i + 1} {status}")
    print(f"  Истинный класс: {true_class}")
    print(f"  Предсказанный: {pred_class}")
    print(f"  Уверенность: {confidence:.2%}")
    print(f"  Вероятности: {predictions[i]}")

import matplotlib.pyplot as plt

# Извлечь историю
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
train_loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(1, len(train_acc) + 1)

# Создать графики
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# График 1: Accuracy
ax1.plot(epochs_range, train_acc, 'b-', label='Train Accuracy', linewidth=2)
ax1.plot(epochs_range, val_acc, 'r-', label='Validation Accuracy', linewidth=2)
ax1.set_title('Model Accuracy', fontsize=14, fontweight='bold')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Accuracy')
ax1.legend()
ax1.grid(True, alpha=0.3)

# График 2: Loss
ax2.plot(epochs_range, train_loss, 'b-', label='Train Loss', linewidth=2)
ax2.plot(epochs_range, val_loss, 'r-', label='Validation Loss', linewidth=2)
ax2.set_title('Model Loss', fontsize=14, fontweight='bold')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("АНАЛИЗ ОБУЧЕНИЯ")
print("="*60)

print(f"\nЛучшая val_accuracy: {max(val_acc):.4f} (эпоха {np.argmax(val_acc)+1})")
print(f"Финальная val_accuracy: {val_acc[-1]:.4f}")

# Проверка на переобучение
diff = train_acc[-1] - val_acc[-1]
if diff > 0.1:
    print(f"\n⚠️ ПЕРЕОБУЧЕНИЕ!")
    print(f"  Train accuracy: {train_acc[-1]:.4f}")
    print(f"  Val accuracy: {val_acc[-1]:.4f}")
    print(f"  Разница: {diff:.4f}")
else:
    print(f"\n✅ Модель обобщается хорошо")

