let click_button = document.querySelector(".click_button")
let click_info = document.querySelector(".header_clicks")
let autoClickInterval = null

let clicker_status = {
    'counter': 0,
    'power': 1,
    'auto_click': false,
    'timer': 1000
}

let shop_info = {
    'upgrade_text': document.querySelector('.click_upgrade'),
    'auto_click_text': document.querySelector('.auto_click_upgrade'),
    'upgrade_cost': 5,
    'auto_click_cost': 1000
}

let upgrades_info = {
    'click_info': document.querySelector('.click_info'),
    'auto_click_info': document.querySelector('.auto_click_info')
}

function counter_convert(info_value, info_text, add_text = '') {
    const units = [
        { threshold: 1e90, divisor: 1e90, suffix: 'Qz' },
        { threshold: 1e87, divisor: 1e87, suffix: 'Qy' },
        { threshold: 1e84, divisor: 1e84, suffix: 'Qx' },
        { threshold: 1e81, divisor: 1e81, suffix: 'Qw' },
        { threshold: 1e78, divisor: 1e78, suffix: 'Qv' },
        { threshold: 1e75, divisor: 1e75, suffix: 'Qu' },
        { threshold: 1e72, divisor: 1e72, suffix: 'Qt' },
        { threshold: 1e69, divisor: 1e69, suffix: 'Qs' },
        { threshold: 1e66, divisor: 1e66, suffix: 'Qr' },
        { threshold: 1e63, divisor: 1e63, suffix: 'Qq' },
        { threshold: 1e60, divisor: 1e60, suffix: 'Qp' },
        { threshold: 1e57, divisor: 1e57, suffix: 'Qo' },
        { threshold: 1e54, divisor: 1e54, suffix: 'Qn' },
        { threshold: 1e51, divisor: 1e51, suffix: 'Qm' },
        { threshold: 1e48, divisor: 1e48, suffix: 'Ql' },
        { threshold: 1e45, divisor: 1e45, suffix: 'Qk' },
        { threshold: 1e42, divisor: 1e42, suffix: 'Qj' },
        { threshold: 1e39, divisor: 1e39, suffix: 'Qi' },
        { threshold: 1e36, divisor: 1e36, suffix: 'Qh' },
        { threshold: 1e33, divisor: 1e33, suffix: 'Qg' },
        { threshold: 1e30, divisor: 1e30, suffix: 'Qf' },
        { threshold: 1e27, divisor: 1e27, suffix: 'Qe' },
        { threshold: 1e24, divisor: 1e24, suffix: 'Qd' },
        { threshold: 1e21, divisor: 1e21, suffix: 'Qc' },
        { threshold: 1e18, divisor: 1e18, suffix: 'Qb' },
        { threshold: 1e15, divisor: 1e15, suffix: 'Qa' },
        { threshold: 1e12, divisor: 1e12, suffix: 'T' },
        { threshold: 1e9,  divisor: 1e9,  suffix: 'B' },
        { threshold: 1e6,  divisor: 1e6,  suffix: 'M' },
        { threshold: 1e3,  divisor: 1e3,  suffix: 'K' }
    ];

    if (info_value >= 1e93) {
        info_text.innerText = add_text + 'Infinity'
        return
    }

    for (let unit of units) {
        if (info_value >= unit.threshold) {
            info_text.innerText = add_text + Math.floor(info_value / unit.divisor) + unit.suffix;
            return;
        }
    }
}

function upgrade_cost_state_change() {
    if (clicker_status['counter'] >= shop_info['upgrade_cost']) {
        shop_info['upgrade_text'].classList.add('active');
    }
    else {
        shop_info['upgrade_text'].classList.remove('active');
    }
}

function auto_clicks_cost_state_change() {
    if (clicker_status['counter'] >= shop_info['auto_click_cost']) {
        shop_info['auto_click_text'].classList.add('active');
    }
    else {
        shop_info['auto_click_text'].classList.remove('active');
    }

    if (clicker_status['timer'] <= 20) {
        shop_info['auto_click_text'].innerText = 'Auto clicks: MAX'
        shop_info['auto_click_text'].classList.remove('active');
        shop_info['auto_click_text'].setAttribute('disabled', 'disabled');
    }
}

function auto_clicks_upgrade_state_change() {
    if (clicker_status['auto_click']) {
        upgrades_info['auto_click_info'].classList.add('active');
    }
}

function change_state() {
    click_info.innerText = clicker_status['counter']

    shop_info["upgrade_text"].innerText = `Click upgrade: ${shop_info['upgrade_cost']}`
    shop_info["auto_click_text"].innerText = `Auto clicks: ${shop_info['auto_click_cost']}`

    upgrades_info['click_info'].innerText = `Click power: ${clicker_status['power']}`
    upgrades_info['auto_click_info'].innerText = `Auto click: ${clicker_status['auto_click'] ? 'Enabled' : 'Disabled'}`

    counter_convert(clicker_status['counter'], click_info)
    counter_convert(shop_info['upgrade_cost'], shop_info["upgrade_text"], 'Click upgrade: ')
    counter_convert(shop_info['auto_click_cost'], shop_info["auto_click_text"], 'Auto clicks: ')
    counter_convert(clicker_status['power'], upgrades_info['click_info'], 'Click power: ')

    upgrade_cost_state_change()
    auto_clicks_cost_state_change()
    auto_clicks_upgrade_state_change()
}

function startAutoClick() {
    if (autoClickInterval) {
        clearInterval(autoClickInterval)  // Останови старый
    }

    autoClickInterval = setInterval(() => {
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
})

shop_info['auto_click_text'].addEventListener('click', () => {
    if (clicker_status['counter'] >= shop_info['auto_click_cost']) {
        if (shop_info['auto_click_cost'] === 1000) {
            clicker_status['auto_click'] = true
        }
        else if (shop_info['auto_click_cost'] > 1000 && (clicker_status['timer'] <= 1000 && clicker_status['timer'] > 20)) {
            clicker_status['timer'] /= 1.3
        }

        clicker_status['counter'] -= shop_info['auto_click_cost']
        shop_info['auto_click_cost'] *= 50
        console.log(clicker_status['timer'])
        startAutoClick()
        change_state()
    }
})

setInterval(() => {
    change_state()
}, 200)