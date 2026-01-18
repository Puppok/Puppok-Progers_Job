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

// Значение по умолчанию (необязательное значение)
function greet(name, age, country = 'Russia') {
    console.log(`Name: ${name}, age: ${age}, country: ${country}`)
}

greet('Bob', 64, 'USA') // возьмет USA
greet('Sam', 15) // возьмет Russia

// === Funcion Expression ===
let hello = function() {
    console.log('Hello')
}

console.log(hello) // отображаем instance функции (шаблон)
hello() // вызываем переменную как функцию

let copyFunc = hello
copyFunc()

// === Функции обратного вызова (callback) ===
// function ask(question, yes, no) {
//     if(confirm(question)) yes()
//     else no()
// }

function yes() {
    console.log('Ok')
}

function no() {
    console.log('Bad')
}

// ask('Yes or No?', yes, no)

// === Лямбда функции (стрелочные / анонимные) ===
// let func = ([параметры]) => { блок кода }

let multi = (a, b) => a * b
console.log(multi(12, 8))

// если 1 параметр, круглые скобки не обязательны
let power = n => n ** 3
console.log(power(3))

// Пример использования лямбды в качестве callback
// let button = ...
// button.addEventListener('click', () => {
//      ... блок кода ...
// })

