# Условия

# if условие:
#     выполняется если условие True
# else:
#     выполняется если условие False

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

if num1 > num2:
    print(f'{num1} больше {num2}')
else:
    print(f'{num1} меньше {num2}')

# if условие1:
#     выполняется если условие1 True
# elif условие2:
#     выполняется если условие2 True
# else:
#     выполняется если все условия False

if num1 > num2:
    print(f'{num1} больше {num2}')
elif num1 == num2:
    print(f'{num1} равно {num2}')
else:
    print(f'{num2} больше {num1}')

# Логические операторы
# and - и
# or - или
# not - не

# and
# True and True = True
# True and False = False
# False and True = False
# False and False = False
# .... 1 ..< x <.. 50 ...
# if x > 1 and x < 50:

# or
# True or True = True
# True or False = True
# False or True = True
# False or False = False
# ..x < .. 1 .... 50 .. < x ..
# if x < 1 or x > 50:

# not
# not True = False
# not False = True
# not (14 > 6) = False

# Сравнить 3 числа
pep1 = int(input('Введите первое число: '))
pep2 = int(input('Введите второе число: '))
pep3 = int(input('Введите третье число: '))

if pep1 > pep2 and pep1 > pep3:
    print(f'{pep1} больше {pep2} и {pep3}')
elif pep2 > pep1 and pep2 > pep3:
    print(f'{pep2} больше {pep1} и {pep3}')
else:
    print(f'{pep3} больше {pep1} и {pep2}')

