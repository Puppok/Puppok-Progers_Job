// DOM дерево (Document Object Model)

// === Получение html элемента ===
// 1. По id
let header_2 = document.getElementById("header")

// 2. Через class
let text = document.querySelector('.text')

// 3. Все элементы одного класса
let list_items = document.querySelectorAll('.list-item')

console.log(header_2.innerText) // отобразить весь внутренний текст
console.log(header_2.innerHTML) // отобразить все внутреннее html содержимое


// Изменение текста html элемента
text.innerText = 'Привет чебупелька, пошли развлекаться'

// Работа с querySelectorAll, всегда через цикл
let i = 1
list_items.forEach(item => {
    console.log(`Item ${i}: ${item.innerText}`)
    i++
})

// === Создание html элемента ===
// Создание html тега
let div_block = document.createElement('div')
document.body.append(div_block)

let header_1 = document.createElement('h1')
header_1.innerText = 'Созданный заголовок'
document.body.append(header_1)

// Создание текстовой вставки
let random_text = document.createTextNode('Случайный текст')
document.body.append(random_text)

// Пример
text_sample = 'Текст для созданного списка на JS'
link_sample = 'https://google.com'
let link_list = document.createElement('div')
link_list.innerHTML = `<ol>
                           <li> <a href="${link_sample}">${text_sample}</a> </li>
                           <li> <a href="${link_sample}">${text_sample}</a> </li>
                           <li> <a href="${link_sample}">${text_sample}</a> </li>
                           <li> <a href="${link_sample}">${text_sample}</a> </li>
                           <li> <a href="${link_sample}">${text_sample}</a> </li>
                       </ol>`
document.body.append(link_list)

// === Способы вставки элемента в структуру html ===
// Внедрение тега или текстовой вставки
let ul = document.querySelector('.ul')

// 1. before() - Вставка перед тегом
let insert_before = document.createTextNode('Before')
ul.before(insert_before)

// 2. after() - Вставка после тега
let insert_after = document.createTextNode('After')
ul.after(insert_after)

// 3. prepend() - Вставка внутри тега в начале
let inside_before = document.createTextNode('Inside before')
ul.prepend(inside_before)

// 4. append() - Вставка внутри тега в конце
let inside_after = document.createTextNode('Inside after')
ul.append(inside_after)

// Вставка куска html кода
let ol = `
    <ol>
        <li>Помидорка</li>
        <li>Помидорка</li>
        <li>Помидорка</li>
        <li>Помидорка</li>
    </ol>`

ul.insertAdjacentHTML('afterbegin', ol) // После начала элемента ul
ul.insertAdjacentHTML('afterend', ol) // Перед началом элемента ul
ul.insertAdjacentHTML('beforebegin', ol) // После конца элемента ul
ul.insertAdjacentHTML('beforeend', ol) // Перед концом элемента ul
