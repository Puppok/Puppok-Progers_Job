import tensorflow as tf
from tensorflow import keras
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense

print(f"TensorFlow версия: {tf.__version__}")
print(f"Keras версия: {keras.__version__}")
print(f"scikit-learn версия: {sklearn.__version__}")
print(f"NumPy версия: {np.__version__}")
print(f"Pandas версия: {pd.__version__}")
print(f"Matplotlib версия: {plt.matplotlib.__version__}")

test = Sequential([
    Dense(10, input_shape=(10,), activation='relu'),
])

test.summary()