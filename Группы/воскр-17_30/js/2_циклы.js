// Циклы
// 1. while
let num = 11
while (num <= 10) {
    console.log(num)
    num++ // инкремент
}


// 2. do while
let num2 = 11
do {
    console.log(num2)
    num2++ // инкремент
} while (num2 <= 10)


// 3. for
// for (начало; условие; шаг) {
//      тело цикла
// }

for (let i = 1; i <= 10; i += 10) {
    console.log(i)
}

// Break / Continue
for (let i = 10; i <= 100; i++) {
    if (i > 30 && i < 51) {
        continue // переход на новую итерацию
    }
    console.log(i)
}

let count = 0
while (true) {
    if (count === 10_000) {
        console.log('Cycle ended')
        break
    }

    count++
    console.log(count)
}

let x = 435
let first = x % 10
let second = Math.floor(x / 10) % 10
let third = Math.floor(x / 100)

console.log(first)
console.log(second)
console.log(third)
