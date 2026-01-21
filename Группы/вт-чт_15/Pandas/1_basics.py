import numpy as np
import pandas as pd

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr)

table = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})
print(table)

# Типы данных Pandas
# 1. Series - линейные данные
# 2. DataFrame - таблица

# === Series ===
# 1. Данные (values) - NumPy массив
# 2. Индексы (index) - метка для каждого элемента
# 3. Имена (name) - опциональные имена столбцов таблицы

# Простой пример
series = pd.Series([1, 2, 3, 4, 5])
print(series)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Способы создания Series
# 1. Из массива (списка)
temp = pd.Series(
    [12, 30, 27, 8, 16],
    index = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт']
)
print(f'\nДанные температур: \n{temp}')

# 2. Из словаря
dict_data = {
    'Макарашкесы': 5,
    'Картофачкен': 56,
    'Огуречики': 7,
    'Сасосики': 84
}
shop_list = pd.Series(dict_data)
print(f'\nСписок покупок: \n{shop_list}')

# 3. Из NumPy массива
np_arr = np.random.rand(5)
np_series = pd.Series(np_arr, index = list('ABCDE'))
print(np_series)

# 4. Константное значение
const_series = pd.Series(250, index = list('ABCDE'))
print(const_series)

# Атрибуты series
print(f'Values: {temp.values}') # значения таблицы
print(f'Index: {temp.index}') # индексы таблицы
print(f'Data Type: {temp.dtypes}') # тип данных кодировки значений
print(f'Shape: {temp.shape}') # форма
print(f'Size: {temp.size}') # размер

# === DataFrame ===
# Способы создания
# 1. Из словаря
dict_pd = pd.DataFrame({
    'Names': ['Tom', 'Bob', 'July'],
    'Age': [12, 59, 26],
    'Lunch': ['Chips', 'Potato', 'Tomato']
})
print(f'\nFrom dict:\n {dict_pd}')

# 2. Из списка словарей
list_dict_pd = pd.DataFrame([
    {'A': 1, 'B': 2, 'C': 3},
    {'A': 4, 'B': 5, 'C': 6},
    {'A': 7, 'B': 8, 'C': 9}
])
print(f'\nFrom dict list:\n {list_dict_pd}')

# 3. Из NumPy массива
np_array = np.random.rand(5, 3)
np_pd = pd.DataFrame(np_array, columns = list('ABC'))
print(f'\nFrom np array:\n {np_pd}')

# 4. Из Pandas series
# минимум 2 series
series_df_1 = pd.Series([1, 2, 3], name = 'A')
series_df_2 = pd.Series([4, 5, 6], name = 'B')

# .concat объединяет массивы, axis - способ объединения (0 - построчно, 1 - по столбцам)
series_df = pd.concat([series_df_1, series_df_2], axis = 1)
print(f'\nSeries DataFrame: \n{series_df}')

# Атрибуты DataFrame
print(f'Shape: {np_pd.shape}') # форма
print(f'Size: {np_pd.size}') # размер
print(f'Data Type: {dict_pd.dtypes}') # тип кодирования данных таблицы
print(f'Columns: {np_pd.columns}') # наименования столбцов
print(f'Index: {np_pd.index}') # индексация таблицы
print(f'Ndim: {np_pd.ndim}') # кол-во измерений

# Просмотр данных таблицы
dataview_df = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.randint(1, 50, 100),
    'C': np.random.choice(['Tom', 'Bred', 'Dick'], 100)
})
print(f'Dataview DataFrame:\n {dataview_df}')

# Выборка от начала
print(dataview_df.head(10)) # выборка первых строк таблицы (по умолчанию 5)

# Выборка от конца
print(dataview_df.tail(10)) # выборка конечных строк таблицы (по умолчанию 5)

# Случайная выборка
print(dataview_df.sample(5)) # выборка случайных строк таблицы (по умолчанию 1)

# Просмотр статистики таблицы
print(dataview_df.describe())

# Информация о таблице
dataview_df.info()