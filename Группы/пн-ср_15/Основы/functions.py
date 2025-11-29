# Функции
# def имя_ф-ции(аргументы):
#   набор действий, которые выполняет ф-ция
#   print() / return 

# 1. Простая ф-ция, отдает результат в консоль
def sayHello():
    print('Привет, чебурек!')

sayHello()

# 2. Ф-ция, принимающая аргументы
def sum(num1, num2):
    print(f'Сумма {num1} + {num2} = {num1 + num2}')

sum(45, 28)

x = 122
y = 68
sum(x, y)

# 3. Функция, которая возвращает значение
def compare(a, b):
    if a > b:
        return f'{a} больше'
    elif a < b:
        return f'{b} больше'
    else:
        return 'числа равны'

print(compare(12, 56))
result = compare(12, 7)
print(result)

result = result + ', ваще круто'
print(result)

sum(result, ', чпок')


# 1. Создайте функцию countLetters, 
#    которая принимает строку и выдает в консоль количество букв в ней 

# 2. Напишите функцию fibonacci, 
#    которая принимает число n и выдает в консоль первые n чисел Фибоначчи 

# 3. Создайте функцию is_prime, 
#    которая принимает число и проверяет, является ли оно простым. 
#    Функция должна показать в консоль True, если число простое, 
#    и False в противном случае.

# 1. Создайте функцию countLetters, 
#    которая принимает строку и выдает в консоль 
#    количество букв в ней 

# 2. Напиши функцию stats(a, b, c), которая принимает три числа 
#    и возвращает сумму и среднее значение этих чисел

# 3. Напиши функцию minutes_to_hours(minutes), 
#    которая переводит количество минут в часы и минуты.
#    Функция должна возвращать строку в формате "X ч Y мин"






def fib(n):
    first = 1
    second = 1

    for i in range(1, n + 1):
        print(first, end = ' ')
        buffer = first + second
        first = second
        second = buffer
        
fib(10)


# def countLetters(string):
#     print(f'Длина "{string}" = {len(string)} символов')

# str = input('введите строку: ')
# countLetters(str)

# def fibonacci(n):
#     first = 1
#     second = 1
#     buffer = 0
#     for i in range(1, n + 1):
#         print(first, end = ' ')
#         buffer = first + second
#         first = second
#         second = buffer

# len = int(input('Введите кол-во чисел последовательности: '))
# fibonacci(len)
# print()

# def simpleNumber(n):
#     if n <= 1:
#         return 'Bad'

#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return 'Bad'
    
#     return 'Good'

# n = int(input('Enter num: '))
# print(simpleNumber(n))


# Задача 1
# Напишите функцию power(base, exponent), которая принимает два числа:
# основание и показатель степени. Функция должна вернуть результат
# возведения числа base в степень exponent.
# Пример: power(2, 3) должна вернуть 8

# Задача 2
# Создайте функцию reverse_number(num), которая принимает целое число
# и возвращает это число в обратном порядке.
# Пример: reverse_number(12345) должна вернуть 54321

# Задача 3
# Напишите функцию is_palindrome(text), которая проверяет, является ли
# переданная строка палиндромом (читается одинаково слева направо и справа налево).
# Функция должна вернуть True, если строка является палиндромом, и False в противном случае.
# Пример: is_palindrome("radar") должна вернуть True, 
# is_palindrome("hello") должна вернуть False


