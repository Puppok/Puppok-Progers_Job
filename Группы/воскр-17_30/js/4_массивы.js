// === Массивы ===
let arr = [] // пустой массив
let numbers = [1, 46, 8, 92, 47]
let strs = ['hello', 'world', 'чебурек', 'таракан']
let complex = ['chpok', 64, false, 577]

// Массив через конструктор
array = new Array(5)
console.log(array)

array_2 = new Array(12, 46, 87, 25)
console.log(array_2)

// Получение значения из массива
// индекс массива - порядковый номер элемента массива (начиная с 0)
console.log(strs[2]) // чебурек
console.log(strs[6]) // undefined

// Перебор массива
// arr.length - возвращает длину массива
for(let i = 0; i < numbers.length; i++) {
    console.log(numbers[i])
}

// === Функции массивов ===
let test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// 1. добавить элемент в массив
test_array.push(40) // добавить значение в конец массива
test_array.unshift(100) // добавить в начало массива
console.log(test_array)

// 2. удалить элемент из массива
let last_end = test_array.pop() // удалить элемент из конца
console.log(`последний удаленный элемент: ${last_end}`)

let last_start = test_array.shift() // удалить элемент из начала
console.log(`первый удаленный элемент: ${last_start}`)
console.log(test_array)

// 3. Душные функции
    // 3.1 forEach - действия для каждого элемента
test_array.forEach(number => {
    console.log(number ** 2)
})

    // 3.2 map - копирует массив и изменяет его
let powered = test_array.map(number => number ** 3)
console.log(powered)
console.log(test_array)

    // 3.3 filter - отдает новый отфильтрованный массив
let filtered_arr = test_array.filter(number => number % 2 === 0)
console.log(filtered_arr)
console.log(test_array)