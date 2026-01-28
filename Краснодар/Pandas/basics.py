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
# 3. Имя (name) - наименования данных (необязательно)

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
np_arr = np.random.rand(5)
random_serires = pd.Series(np_arr, index=list('ABCDE'))
print(f'\nFrom NumPy: \n{random_serires}')

# 4. Константное значение
const_series = pd.Series(500, index=range(1, 6))
print(f'\nConstant: \n{const_series}')

# Атрибуты типа Series
attr_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print('\nSeries attributes:')
print(f'1. Values: {attr_series.values}')
print(f'2. Index: {attr_series.index}')
print(f'3. Datatypes: {attr_series.dtypes}')
print(f'4. Shape: {attr_series.shape}')
print(f'4. Size: {attr_series.size}')

# Установка имени
attr_series.name = 'Index' # наименование таблицы
attr_series.index.name = 'Table attribute' # заголовок таблицы (над таблицей)
print(f'With names: \n{attr_series}')

# === DataFrame ===
# 1. Из словаря
dict_df = pd.DataFrame({
    'Name': ['Sam', 'Tom', 'Bob'],
    'Age': [25, 35, 45],
    'Salary': [40_000, 80_000, 140_000]
})
print(f'\nDF from dict: \n{dict_df}')

# 2. Из списка словарей
list_df = pd.DataFrame([
    {'A': 1, 'B': 2, 'C': 3}, # ключ - название столбца, значение - данные таблицы
    {'A': 4, 'B': 5, 'C': 6},
    {'A': 7, 'B': 8, 'C': 9}
])
print(f'\nDF from dict list: \n{list_df}')

# 3. Из NumPy массива
np_array = np.random.rand(5, 3)
np_df = pd.DataFrame(np_array, columns = list('ABC'))
print(f'\nDF from numpy array: \n{np_df}')

# 4. Из набора Series
df_series_1 = pd.Series([1, 2, 3], name = 'Column 1') # создаем набор Series (минимум 2)
df_series_2 = pd.Series([4, 5, 6], name = 'Column 2')

# .concat для объединения массивов (axis = 0 - по вертикали, axis = 1 - по горизонтали)
df_series = pd.concat([df_series_1, df_series_2], axis = 1)
print(f'\nDF from pandas Series: \n{df_series}')

# DataFrame attributes
print(f'\nDataFrame attributes:')
print(f'Shape: {np_df.shape}')
print(f'Columns: {np_df.columns}')
print(f'Index: {np_df.index}')
print(f'Datatypes: {np_df.dtypes}')
print(f'Size: {np_df.size}')
print(f'Dimensions: {np_df.ndim}')

# DataFrame data view
data_view_df = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.randint(0, 100, 100),
    'C': np.random.choice(['x', 'y', 'z'], 100)
})
print(f'\nData view DataFrame: \n{data_view_df}')

# 1. Выборка первых строк
print(f'\nDF head:\n {data_view_df.head()}') # .head(amount) - без указания количества, выдаст 5 первых строк

# 2. Выборка последних строк
print(f'\nDF tail:\n {data_view_df.tail(1)}')  # .tail(amount) - без указания количества, выдаст 5 последних строк

# 3. Случайная выборка
print(f'\nDF sample:\n {data_view_df.sample(10)}') # .sample(amount) - случайное кол-во строк (по умолчанию 1)

# 4. Информация о таблице
print(f'\nDF info:\n {data_view_df.info()}')

# 5. Статистика
print(f'\nDF describe:\n {data_view_df.describe()}')