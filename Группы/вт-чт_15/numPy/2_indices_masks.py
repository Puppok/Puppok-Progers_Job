import numpy as np

# Индексация и срезы массивов

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[4]) # 5
print(arr[-1]) # 9
print(arr[-6]) # 4

# [start:end:step]
print(arr[2:8])

# индексация по списку
indices = [2, 4, 5, 7] # список индексов
print(arr[indices])

# индексация многомерных массивов
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr_2d[1, 2]) # доступ к элементу [строка, столбец]
print(arr_2d[-1, -3]) # 7 [первая с конца, третий с конца]

print(arr_2d[1:]) # значение - строка среза (со средней строки до конца)
print(arr_2d[:1])
print(arr_2d[2:, 2]) # через запятую - индекс элементов по данному срезу

# Маски массивов (булевая индексация)
start_arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 100])
mask = start_arr > 30 # массив маска (условие выборки элементов)
print(f'arr mask: {mask}') # массив значений True/False
print(f'result: {start_arr[mask]}') # массив с учетом маски по значениям True
print(f'result: {start_arr[~mask]}') # массив с учетом маски по значениям False

print(f'result: {start_arr[start_arr > 50]}') # сокращенная запись для значений True
print(f'result: {start_arr[~(start_arr > 50)]}') # сокращенная запись для значений False

# применение логических операторов
# & - И (and)
# | - ИЛИ (or)
# ~ - НЕ (not)

# выборка элементов больше 50 и которые деляться на 3 нацело
print(f'Complex: {start_arr[(start_arr > 50) & (start_arr % 3 == 0)]}')

# изменение элементов по условию
change_arr = np.array([12, 56, 8, 1, 35, 9, 35, 91])
change_arr[change_arr < 10] = 100 # элементы меньше 10 станут равны 100
print(change_arr)

# поиск индексов np.where
find_indices = np.where(change_arr < 80) # выборка элементов, проходящих по условию
print(find_indices)
new_arr = change_arr[find_indices]
print(new_arr)
