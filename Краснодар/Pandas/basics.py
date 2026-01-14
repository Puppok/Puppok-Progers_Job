import pandas as pd
import numpy as np

# Pandas - Python Data Analysis Library

# NumPy
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(arr) # табличное представление данных

# Pandas
pd_data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
})
print(pd_data) # полноценная таблица, с данными, названиями столбцов и нумерацией строк

# Виды данных в pandas
# 1. Series - линейные данные (одномерные массивы)
# 2. DataFrame - табличные данные

# === Series ===
# Структура
# 1. Данные (values) - NumPy массив
# 2. Индексы (index) - метки для каждого элемента
# 3. Имя (name) - наименования индексов (данных) (необязательно)

series = pd.Series([1, 2, 3, 4, 5])
print(series)

# Вариации создания линейных данных
# 1. Из списка с именованными индексами
temps = pd.Series(
    [22, 30, 18, 6, 12],
    index = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт']
)
print(f'\nDaily temps: \n{temps}')

# 2. Из словаря (ключ = индексы)
grades = pd.Series({
    'Русский': 85,
    'Математика': 60,
    'Физика': 70,
    'Информатика': 95
})
print(f'\nGrades: \n{grades}')

# 3. Из NumPy массива


# 4. Константное значение