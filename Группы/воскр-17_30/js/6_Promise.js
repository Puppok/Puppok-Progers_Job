// === Promise (промисы) ===
// let promise = new Promise((resolve, reject) => {
//      действия, которые должны когда либо выполниться
//      resolve(результат) - успешное завершение промиса
//      reject(ошибка) - завершение с ошибкой
// })

// .then(callback) - получает resolve ответ
// .catch(callback) - получает reject ответ
// .finally(callback) - получает побочные данные, выполняется всегда

let stop = undefined

let goodPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('ьыъ')
    }, 1500)
})

// обработка успешного завершения промиса
goodPromise.then(result => { // result хранит данные ответа промиса
    console.log(result)
})

let badPromise = new Promise((resolve, reject) => {
    reject(new Error('Ошибка выполнения promise'))
})

badPromise.catch(err => {
    console.log(err)
})

// пример асинхронного выполнения, выполнятся два вывода ниже и после них .then()
console.log("Hello!")
//
// let checkPromise = new Promise((resolve, reject) => {
//     if (2 > 3) {
//         resolve('Условие выполнилось')
//     }
//     else {
//         reject(new Error('Условие не выполнилось'))
//     }
// })

function test_promise(num1, num2) {
    return new Promise((resolve, reject) => {
        if (num1 > num2) {
            resolve('Условие выполнилось')
        }
        else {
            reject(new Error('Условие не выполнилось'))
        }
    })
}

test_promise(34, 8)
    .then(result => { console.log(result) }) // выполнится если промис завершится успешно
    .catch(err => { console.log(err) }) // выполнится если промис завершится с ошибкой
    .finally(() => { console.log('Промис завершен') }) // выполнится всегда
