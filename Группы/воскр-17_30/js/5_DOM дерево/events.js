const p = document.querySelector('.test-text')

function clickEvent(element) {
    element.innerText = 'Ты тыкнул!'
    element.style.cssText = `
        background-color: yellow;
        letter-spacing: 20px;
    `
}

function hello() {
    alert('Hello')
}

p.onclick = hello

const header = document.querySelector('.header')
header.addEventListener('click', () => {
    header.innerText = 'Хыыы'
})

const btn_light = document.querySelector('.btn-light')
const btn_dark = document.querySelector('.btn-dark')
const btn_switch = document.querySelector('.btn-switcher')
const body = document.body


btn_light.addEventListener('click', () => {
    body.classList.remove('dark') // убрать класс
    body.classList.add('light') // добавить класс
})

btn_dark.addEventListener('click', () => {
    body.classList.remove('light') // убрать класс
    body.classList.add('dark') // добавить класс
})

btn_switch.addEventListener('click', () => {
    body.classList.toggle('dark') // переключить класс

    // проверить наличие класса
    if (body.classList.contains('dark')) {
        btn_switch.innerText = 'Переключить (темная)'
    }
    else {
        btn_switch.innerText = 'Переключить (светлая)'
    }
})

// Пример с формой
const input = document.querySelector('input')
const submit = document.querySelector('.btn-submit')

submit.addEventListener('click', () => {
    console.log(input.value)
    input.value = ''
})

const add_btn = document.querySelector('.btn-add')
const clickerText = document.querySelector('.clicker-text')
let clicks = 0

function add() {
    clicks++
    clickerText.innerText = 'Clicks: ' + clicks

    if (clicks >= 20) add_btn.setAttribute('disabled', 'disabled')

}

function sub() {
    clicks--
    clickerText.innerText = 'Clicks: ' + clicks

    if (clicks < 20) add_btn.removeAttribute('disabled')
}

