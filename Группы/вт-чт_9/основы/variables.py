# Переменные
# имя = значение
num = 12 # number - числовой
message = 'Привет, бобер!' # string - строковый тип
isOpen = True # boolean - логический тип (True/False)

# Ввод/вывод данных
# print(значение/переменная)
print('как дела?')
print(num)

# Интерполяция - внедрение переменной в строку
# f'привет, {name}!'
name = 'Tom'
print(f'Привет, {name}!')

blabla = input('напиши что нибудь: ')
print(blabla)

# преобразование ввода в числовой тип
# number = int(input('Введите число: '))

# Арифметика
# + - * / % ** //

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

print(f'{num1} + {num2} = {num1 + num2}') # сложение
print(f'{num1} - {num2} = {num1 - num2}') # вычитание
print(f'{num1} * {num2} = {num1 * num2}') # умножение
print(f'{num1} / {num2} = {num1 / num2}') # деление
print(f'{num1} % {num2} = {num1 % num2}') # остаток от деления
print(f'{num1} ** {num2} = {num1 ** num2}') # степень числа
print(f'{num1} // {num2} = {num1 // num2}') # целочисленное деление

print('\n')
# Сравнения
# > < >= <= == !=
print(f'{num1} > {num2} = {num1 > num2}')
print(f'{num1} < {num2} = {num1 < num2}')
print(f'{num1} >= {num2} = {num1 >= num2}')
print(f'{num1} <= {num2} = {num1 <= num2}')
print(f'{num1} == {num2} = {num1 == num2}')
print(f'{num1} != {num2} = {num1 != num2}')


