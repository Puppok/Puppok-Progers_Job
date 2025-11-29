# Рекурсия - функция, которая вызывается сама себя

# def func(x):
#     func(x)

def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

print(fac(3))

# 1. Написать ф-цию, 
#    которая принимает n и выводит в консоль все числа от n до 0
def countDown(n):
    if n == 0:
        print(0)
        return
    
    print(n)
    countDown(n - 1)

countDown(10)

# 2. Найдите сумму чисел от 1 до n
def recSum(n):
    if n == 1:
        return 1
    
    return n + recSum(n - 1)

print(recSum(10))
# 3. Напишите ф-цию для подсчета чисел в последовательности фибоначчи
#    - ввести n и показать в консоли число, находящее на позиции n
#    - ввести n и отобразить в консоли всю последовательность от 1 (0) до n
#    1 1 2 3 5 8 13 ...

def fib_1(n):
    if n == 0: 
        return  0
    if n == 1:
        return 1
    
    return fib_1(n - 1) + fib_1(n - 2)

print(fib_1(6))

def fib_2(n, a = 1, b = 1):
    if n == 0: 
        return
    
    print(a, end = ' ')
    fib_2(n - 1, b, a + b)

fib_2(10)