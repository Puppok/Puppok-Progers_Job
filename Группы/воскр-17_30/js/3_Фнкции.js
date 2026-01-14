// Функции

// === Function Declaration ===
// function имя_функции(параметры) {
//      ... тело функции ...
// }
//
// имя_функции(аргументы) - вызов функции

// 1. Ф-ция, выдающая что то в консоль (alert)
function sayHello() {
    console.log('Привет, чебуреки!')
}

sayHello()

// 2. Ф-ция, которая принимает аргументы
function compare(num1, num2) {
    if (num1 > num2) console.log(`${num1} > ${num2}`)
    else if (num1 < num2) console.log(`${num1} < ${num2}`)
    else console.log('Числа равны')
}

compare(23, 98)

let x = 352, y = 5678
compare(x, y)

// 3. Ф-ция, которая возвращает значение
function sum(num1, num2) {
    return num1 + num2
}

let result = sum(23, 59) // записывает полученное значение в переменную
console.log(result)

console.log(sum(64, result)) // использование новой переменной

// Function Expression
// Lambda (callback)


// Значение по умолчанию (необязательное значение)
function greet(name, age, country = 'Russia') {
    console.log(`Name: ${name}, age: ${age}, country: ${country}`)
}

greet('Bob', 64, 'USA') // возьмет USA
greet('Sam', 15) // возьмет Russia