# Словари / объекты
# имя = {
#   'ключ': значение,
#   'ключ': значение,
#   'ключ': значение
# }

shopList = {
    'apple': 5,
    'banana': 10,
    'orange': 20
}

#^ Создание словаря
empty = {} # {}
moreEmpty = dict() # {}

#^ Создание словаря из массива
arr = ['asgard', 'sdhsrd', 'dfndrd']
newDict = dict(enumerate(arr))

#^ Добавление элементов в словарь
x = 10 # создание обычной переменной (для сравнения)

shopList['pomelo'] = 3 # (обращаемся к словарю по создаваемому ключу и задаем значение)

#^ Получение элементов из словаря
     #& 1. способ по ключу
print(shopList['banana'])
# print(shopList['pep']) - ошибка, ключа нет в словаре

    #& 2. с помощью .get()
print(shopList.get('banana'))
print(shopList.get('pep', 'такого ключа нет')) # если ключа нет, срабатывает default параметр

#^ Удаление элементов из словаря
    #& 1. с помощью del
del shopList['apple']
print(shopList) # {'banana': 10, 'orange': 20, 'pomelo': 3}
# del shopList['pep'] - ошибка, ключ не существует

    #& 2. с помощью .pop()
# удаляем элемент и записываем удаленное значение в переменную
deletedOranges = shopList.pop('orange') 
print(shopList) # смотрим получившийся словарь
print(deletedOranges) # смотрим удаленное значение

# shopList.pop('ppe') - ошибка, ключа нет в словаре
print(shopList.pop('ppe', 'такого ключа нет')) # сработает default параметр

print('--------------')

#^ Перебор словарей
#~ 1. с помощью обычного цикла
for item in shopList: # item получает ключи словаря
    print(item, shopList[item]) # пример, вывод ключа и значения по ключу

print('--------')
#~ 2. перебор ключей напрямую через .keys()
for item in shopList.keys(): 
    print(item, shopList[item]) # пример, вывод ключа и значения по ключу

print('--------')
#~ 3. перебор значений через .values() 
for item in shopList.values():
    print(item)

print('--------')
#~ 4. комплексный способ через .items()
for key, value in shopList.items():
    print(f'ключ: {key}, значение: {value}')

#^ Вложенные словари
character = {
    'name': 'Artem',
    'health': 100,
    'stamina': 100,
    'isAlive': True,
    'skills': ['boom boom', 'babah', 'mazafaka'],
    'armor': {
        'head': 10,
        'torso': 80,
        'hands': 20,
        'legs': 20
    }
}

print(character['name']) # Artem
print(character['skills']) # ['boom boom', 'babah', 'mazafaka']
print(character['armor']) # {'head': 10, 'torso': 80, 'hands': 20, 'legs': 20}

print(f'броня на руках: {character["armor"]['hands']}') # получаем значение вложенного словаря
print(f'последний скил: {character["skills"][2]}') # получаем значение по индексу вложенного массива