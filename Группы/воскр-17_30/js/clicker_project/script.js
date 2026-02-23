let click_button = document.querySelector(".click_button")
let click_info = document.querySelector(".header_clicks")

let clicker_status = {
    'counter': 0,
    'power': 1,
    'auto_click': false,
    'timer': 10
}

let shop_info = {
    'upgrade_text': document.querySelector('.click_upgrade'),
    'auto_click_text': document.querySelector('.auto_click_upgrade'),
    'upgrade_cost': 30,
    'auto_click_cost': 1000
}

let upgrades_info = {
    'click_info': document.querySelector('.click_info'),
    'auto_click_info': document.querySelector('.auto_click_info')
}

function change_state() {
    click_info.innerText = clicker_status['counter']

    shop_info["upgrade_text"].innerText = `Click upgrade: ${shop_info['upgrade_cost']}`
    shop_info["auto_click_text"].innerText = `Auto clicks: ${shop_info['auto_click_cost']}`

    upgrades_info['click_info'].innerText = `Click power: ${clicker_status['power']}`
    upgrades_info['auto_click_info'].innerText = `Auto click: ${clicker_status['auto_click'] ? 'Enabled' : 'Disabled'}`
}

function startAutoClick() {
    setInterval(() => {
        if (clicker_status['auto_click']) {
            clicker_status['counter'] += clicker_status['power']
            change_state()
        }
    }, clicker_status['timer'])
}

click_button.addEventListener("click", () => {
    clicker_status['counter'] += clicker_status['power']
    change_state()
})

shop_info['upgrade_text'].addEventListener('click', () => {
    if (clicker_status['counter'] >= shop_info['upgrade_cost']) {
        clicker_status["counter"] -= shop_info['upgrade_cost']
        clicker_status['power'] *= 2
        shop_info['upgrade_cost'] *= 2
        change_state()
    }
    else {
        alert('Not enough')
    }
})

shop_info['auto_click_text'].addEventListener('click', () => {
    if (clicker_status['counter'] >= shop_info['auto_click_cost']) {
        clicker_status['counter'] -= shop_info['auto_click_cost']
        shop_info['auto_click_cost'] = 'TOP'
        clicker_status['auto_click'] = true
        change_state()
        startAutoClick()
    }
})

change_state()