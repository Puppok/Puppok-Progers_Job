const input = document.querySelector('.input')
const list_section = document.querySelector('.list')
const completed_count = document.querySelector('.comleted')
const uncompleted_count = document.querySelector('.uncomleted')

const add_btn = document.querySelector('.add_btn')

function update_counter() {
    const all = document.querySelectorAll('.list_element').length
    const done = document.querySelectorAll('.checkbox:checked').length
    completed_count.textContent = `Completed: ${done}`
    uncompleted_count.textContent = `Uncompleted: ${all - done}`
}

add_btn.addEventListener('click', () => {
    if (input.value === '') {
        input.setCustomValidity('Can\'t be empty')
        input.reportValidity()
        return
    }
    input.setCustomValidity('')

    const task_element_html = `<input type="checkbox" class="checkbox">
                                     <p class="element_text">${input.value}</p>
                                     <button class="btn delete_btn">Delete</button>
                                     <button class="btn edit_btn">Edit</button>`

    const task_element = document.createElement('div')
    task_element.classList.add('list_element')
    task_element.innerHTML = task_element_html
    list_section.append(task_element)
    input.value = ''
    update_counter()

    const element_text = task_element.querySelector('.element_text')
    task_element.addEventListener('change', (event) => {
        element_text.classList.toggle('completed', event.target.checked)
        update_counter()
    })

    task_element.querySelector('.delete_btn').addEventListener('click', () => {
        task_element.remove()
        update_counter()
    })

    const edit_btn = task_element.querySelector('.edit_btn')
    edit_btn.addEventListener('click', () => {
        if (edit_btn.textContent === 'Edit') {
            const edit_input = document.createElement('input')
            edit_input.type = 'text'
            edit_input.value = element_text.textContent
            edit_input.classList.add('edit_input')
            element_text.replaceWith(edit_input)
            edit_btn.textContent = 'Save'
            edit_input.focus()
        } else {
            const new_text = task_element.querySelector('.edit_input').value
            const new_p = document.createElement('p')
            new_p.classList.add('element_text')
            new_p.textContent = new_text
            if (task_element.querySelector('.checkbox').checked) {
                new_p.classList.add('completed')
            }
            task_element.querySelector('.edit_input').replaceWith(new_p)
            edit_btn.textContent = 'Edit'
        }
    })
})

input.addEventListener('input', () => {
    input.setCustomValidity('')
})
