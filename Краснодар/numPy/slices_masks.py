import numpy as np

# === Индексация линейных массивов ===
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# индексация линейных массивов
print(arr[3]) # слева направо
print(arr[-1]) # в обратную сторону

# fancy indexing - индексация по списку индексов
indices = [0, 4, 6, 8]
print('fancy: ', arr[indices])

# изменение значений разными способами
arr[0] = 100 # через индекс
arr[1:4] = [200, 300, 400] # через срез
arr[[4, 5, 6]] = [500, 600, 700] # через fancy
arr[[7, 8, 9]] = 5 # фиксированное число через fancy
print('Refactor: ', arr)

# Срезы
# [start:end-1:step]
print(arr[2:]) # от 2 индекса до конца
print(arr[2:7]) # от 2 до 6 индекса
print(arr[::2]) # каждый 2ой элемент, начиная с первого


# === Индексация матриц ===
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix[0][1]) # через списки python
print(matrix[0, 1]) # через numpy [строка, столбец]

# срезы матриц
print('срезы матриц:')
print(matrix[0]) # первая строка
print(matrix[1, :2]) # вторая строка, все значения кроме последнего
print(matrix[:2, 0]) # 1, 2 строки, все значения под индексом 0

np.random.seed(1)
randint_arr = np.random.randint(1, 100, (10, 10))
print('Тест срезов:\n', randint_arr)
print('\nПосле среза:\n', randint_arr[2:8, 4:6]) # c 3 до 8 строки, с 5 до 6 столбика

# === Маски ===
np.random.seed(None)
mask_indexing = np.random.randint(1, 100, 10) # исходный массив
print(f'Arr: {mask_indexing}')

mask = mask_indexing > 30 # массив маска (фильтрация массива, проходят значения, которые > 30)
print(f'Mask arr: {mask}')

result = mask_indexing[mask] # новый массив, с учетом фильтрации
print(f'Result: {result}')

# без промежуточной переменной
print(f'Без переменной маски: {mask_indexing[mask_indexing < 60]}')

# === Комбинирование условий ===
# И (and) - &
# ИЛИ (or) - |
# НЕ (not) - ~

combine = mask_indexing[(mask_indexing < 60) & (mask_indexing > 30)]
print(f'Combine arr: {combine}')

# Пример: статистика массива
count = (mask_indexing > 30).sum()
print(f'Элементов > 20: {count}')

percent = (mask_indexing > 30).mean() * 100
print(f'Процент от всех элементов: {percent:.1f}%')

# === Поиск индексов ===
# np.where(условие, если True, если False)

# 1. взять только индексы массива
indices = np.where(mask_indexing > 50)
print(f'Индексы по условию: {indices}')
print(mask_indexing[indices])

# 2. форматирование массива
indices_result = np.where(mask_indexing > 50, mask_indexing, 100)
print(f'Форматированный массив: {indices_result}')


# Задача:
# У вас есть данные о 1000 сотрудников компании. Нужно провести анализ
# используя булевы маски для фильтрации и выборки данных.
np.random.seed(100)
amount = 1000

# ЗАДАНИЕ:
# 1. Создайте массивы данных:
#    - Возраст: случайные числа 22-65
#    - Зарплата: случайные числа 40,000-200,000
#    - Отдел: случайный выбор из [0=IT, 1=Sales, 2=HR, 3=Finance]
#    - Опыт: случайные числа 0-40 лет
ages = np.random.randint(22, 66, amount)
salaries = np.random.randint(40_000, 200_000, amount)
office = np.random.choice([0, 1, 2, 3], amount)
exp = np.random.randint(0, 41, amount)

# 2. Используя ТОЛЬКО булевы маски, найдите:
#    - Сотрудников старше 50 лет
#    - Сотрудников с зарплатой > 100,000
#    - IT сотрудников (отдел=0) с зарплатой > 80,000
#    - Сотрудников 30-40 лет с опытом > 10 лет
#    - Топ-10% по зарплате (зарплата выше 90-го перцентиля)
count_old = ages[ages > 50]
print(f'Older than 50:\n {count_old}')

high_salary = salaries[salaries > 100_000]
print(f'High salary:\n {high_salary}')

it_high_salary = np.array([(office == 0) & (salaries > 80_000)]).sum()
print(f'IT & high salary: {it_high_salary}')

dinosaur = np.array([((ages > 29) & (ages < 41)) & (exp > 10)]).sum()
print(f'Dinosaur: {dinosaur}')

# по умному
percent_90 = np.percentile(salaries, 90)
percent_mask = np.array([salaries > percent_90]).sum()
print(f'Percent mask: {percent_mask}')

# по простому
salaries_sort = np.sort(salaries)
print(f'Top 10% salaries:\n {salaries_sort[-100:]}')

# 3. Операции с масками:
#    - Повысить зарплату на 10% сотрудникам с опытом > 15 лет
#    - Установить максимальную зарплату 180,000 (клиппинг сверху)
#    - Найти "недооценённых" (зарплата < медианной, но опыт > медианного)
salary_mod = salaries.copy().astype(np.float64)

exp_mask = exp > 15
count_exp_15 = exp_mask.sum() # кол-во сотрудников с опытом > 15 лет
avg_exp_15 = salary_mod[exp_mask].mean() # текущая средняя зп
salary_mod[exp_mask] *= 1.1 # повышение зп на 10%
avg_new = salary_mod[exp_mask].mean() # новая средняя зп

print(f'Employees: {count_exp_15}\n' 
      f'Old average: {avg_exp_15:.0f}\n'
      f'New average: {avg_new:.0f}\n'
      f'Income: +{(avg_new / avg_exp_15 - 1) * 100:.1f}%')

max_salary = 180_000
mask_above = salary_mod > max_salary
count_clipped = mask_above.sum()
salary_mod[mask_above] = max_salary

print(f'Max salary: {max_salary:.0f}\n'
      f'Employees clipped: {count_clipped:.0f}\n')

median_salary = np.median(salaries)
median_exp = np.median(exp)
mask_dodiki = (salaries < median_salary) & (exp > median_exp)
print(f'Dodiki: {mask_dodiki.sum()}')

rates= np.array([
    [85, 90, 78],
    [92, 88, 95],
    [78, 85, 82],
    [95, 92, 90],
    [70, 75, 80]
])

for i, subject in enumerate(rates):
    print(f'{i + 1}. {subject.mean():.1f}')