# Функции
# def название(аргументы):
#   набор действий 
#   print() / return
# 
# название() - вызов функции

# 1. функция, которая выдает что то в консоль
def sayHello():
    print('Привет, чуваки!')

sayHello()

# 2. функция, которая принимает аргументы
def sum(a, b):
    print(f'Сумма {a} + {b} = {a + b}')

sum(12, 7)

x = 154
y = 3245

sum(x, y)
sum('привет, ', 'Захар!')

# 3. функция, которая возвращает значение
def multi(a, b):
    return a * b

print(multi(2, 5))
newNumber = multi(10, 6)
print(newNumber)

sum(multi(7, 6), multi(9, 4))

for i in range(1, newNumber):
    print(i, end = ' ')

print()

# 1. Создайте функцию countLetters, 
#    которая принимает строку и выдает в консоль количество символов в ней 
def countLetters(string):
    print(f'Длина {string} = {len(string)} символов')

str = input('введите строку: ')
countLetters(str)

# 2. Напишите функцию fibonacci, 
#    которая принимает число n и выдает в консоль первые n чисел Фибоначчи 
#    1 1 2 3 5 8 13 21 34 55 89 
def fibonacci(n):
    first = 1
    second = 1
    for i in range(1, n + 1):
        print(first, end = ' ')
        buffer = first + second
        first = second
        second = buffer

len = int(input('Введите кол-во чисел последовательности: '))
fibonacci(len)

# 3. Создайте функцию simpleNumber, 
#    которая принимает число и проверяет, является ли оно простым. 
#    Функция должна показать в консоль True, если число простое, 
#    и False в противном случае.

