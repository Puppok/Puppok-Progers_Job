# def func(x):
#   if x == 1: - общий случай
#       return 1
#   return func(x - 1) - основное действие рекурсии

# Вычислить факториал числа
def fac(x):
    if x == 1: 
        return 1
    
    return x * fac(x - 1)

print(fac(5))


# Вывести в консоль сумму чисел от 1 до d
# Вывести в консоль список чисел от 10 до 1
def numList(x):
    if x == 1:
        print(1)
        return 
    
    print(x)
    numList(x - 1)

numList(10)