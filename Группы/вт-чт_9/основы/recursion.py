# func(x):
#   if x == общее_значение:
#     return общее_значение
#   return func(x - 1)

# Вычислить факториал числа
def factorial(n):
    if n == 1:
        return 1
   
    return n * factorial(n - 1)

print(factorial(10))

# Вычислить сумму чисел от n до 0
# Вывести в консоль все числа от n до 0