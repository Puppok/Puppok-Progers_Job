from sklearn.datasets import load_iris # готовый датасет
from sklearn.model_selection import train_test_split # распределение данных на обучающие и тестовые
from sklearn.preprocessing import StandardScaler # нормализация данных
from keras.utils import to_categorical # преобразователь в one hot encoding
import numpy as np

# === 1. Загрузка данных ===

