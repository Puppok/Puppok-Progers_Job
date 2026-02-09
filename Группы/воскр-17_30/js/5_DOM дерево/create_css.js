let text = document.querySelector('.text')

// css свойства как на чистом css
text.style.cssText = `
    color: red;
    letter-spacing: 20px;`

// css свойства как JS переменные
text.style.width = '100px'
text.style.backgroundColor = 'yellow'

// === Работа с классами ===
let h1 = document.createElement('h1')
h1.innerHTML = 'Заголовок настоящего мужика'
h1.className = 'header-1' // создать класс для элемента
document.body.append(h1)


