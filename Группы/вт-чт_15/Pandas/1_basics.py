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

# 4. Константное значение