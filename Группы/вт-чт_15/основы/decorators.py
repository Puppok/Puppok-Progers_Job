# Декораторы
# @decorator
# def func():
#     действия ф-ции

# def decorator(func):
#     def wrapper():
#         действия декоратора
#         func()
#         действия декоратора
#     return wrapper

def decor(func):
    def wrapper():
        print('Ф-ция вызвалась')
        func()
        print('Ф-ция завершилась')
    return wrapper

@decor
def sayHello():
    print('Hello')

# sayHello()

# ------------------------------------

# Передача функции как аргумента
def func(func):
    func()

def hello():
    print('Hello')

x = hello

# func(x)

# Создание функции внутри функции
def outerFunc():
    print('это внешняя ф-ция')

    def innerFunc():
        print('это внутренняя ф-ция')

    innerFunc()

# outerFunc()

# Возврат функции, как результата другой ф-ции
def createMulti(x):

    def multi(y):
        return x * y
    
    return multi

# multiplier = createMulti(5)
# print(multiplier(10))
# print(multiplier(20))
# print(multiplier(100))

# Декоратор
def makeBold(func):
    def wrapped():
        return '<b>' + func() + '</b>'
    return wrapped

# def pep():
#     return 'дратути'

# decor = makeBold(pep)
# print(decor())

@makeBold
def pep():
    return 'дратути'

# print(pep())

# Пример: счетчик вызовов
def countCalls(func):
    count = 0 

    def wrapper():
        nonlocal count
        count += 1
        print(f'Сделано вызовов №{count}: ')
        return func()

    return wrapper

@countCalls
def calls():
    print('Hello')

# calls()
# calls()
# calls()
# calls()
# calls()
# calls()

# Декоратор с циклом
def repeat(func):
    def wrapper():
        for i in range(1, 4):
            func()

    return wrapper

@repeat
def chpok():
    print('Chpok')

# chpok()



# === Декораторы еще раз === #

# функция как аргумент 
def func():
    print('Hello')

func() # вызов ф-ции
hello = func # записываем instance ф-ции в переменную

def startFunc(func):
    func()

startFunc(func)

# Создание и вызов функции внутри функции
def createFunc():
    def func():
        print('Hello, pep')
    
    func()

createFunc()

# Создание декоратора
# Функция, которая принимает функцию в качестве аргумента и возвращает новую функцию
# def decor(func):
#     def wrapper():
#         действия декоратора
#         func()
#         действия декоратора
#     return wrapper
# 
# 1. исходная форма записи
# def func():
#     действия ф-ции
# 
# var = decor(func) 
# var()

# 2. Запись с декоратором
# @decor
# def func():
#     действия ф-ции
# 
# func()

def beautyDecor(func):
    def wrapper():
        print('==========================')
        func()
        print('--------------------------')

    return wrapper

@beautyDecor
def sayHello():
    print('Этот текст стал очень красивый уииии')

sayHello()

# декораторы с аргументами
def hzDecor(func):
    def wrapper(a, b):
        print('==========================')
        func(a, b)
        print('--------------------------')
    return wrapper

@hzDecor
def sum(a, b):
    print(a + b)

sum(10, 20)

# Декоратор с указателями
def smartDecor(func):
    # * - аргументы в виде множества значений
    # ** - аргументы в виде словаря
    def wrapper(*args, **kwargs):
        print(f"Вызываем {func.__name__} с аргументами:")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@smartDecor
def sum(a, b, c, d, e):
    return a + b + c + d + e

print(sum(1, 2, 3, 4, 5))

@smartDecor
def hello(age, name = 'Tom', city = 'New York'):
    return f'Hello, {name}, {age}, {city}'

@smartDecor
def compare(a, b, c):
    if a > b and a > c:
        return f'{a} больше'
    elif b > a and b > c:
        return f'{b} больше'
    else:
        return f'{c} больше'
    
print(compare(1, 2, 3))

print(hello(12))

# Декоратор для проверки возраста

@decor
def checkAge(name, age):
    return f'Привет, {name}, ты уже дед'

if age < 18:
    'ты мелкий'
else:
    checkAge()

# Декоратор для проверки пароля
# Создайте декоратор, который проверяет, что число положительное