let countdown_icon = document.querySelector("#countdown_icon")
let day = document.querySelector("#day")
let hour = document.querySelector("#hour")
let minute = document.querySelector("#minute")
let second = document.querySelector("#second")
let ms = document.querySelector("#ms")
let btn_start = document.querySelector("#btn_start")
let btn_reset = document.querySelector("#btn_reset")

let input_hour = document.querySelector("#input_hour")
let input_minute = document.querySelector("#input_minute")

let date = new Date()
date.setHours(0, 0, 0, 0)

function addZero(num) {
    return (num < 10) ? "0" + num : num
}

function addZeroZero(num) {
    if (num < 10) {
        return "00" + num
    } else if (num >= 10 && num < 100) {
        return "0" + num
    } else
        return num
}

function getTime() {
    hour.innerHTML = addZero(date.getHours())
    minute.innerHTML = addZero(date.getMinutes())
    second.innerHTML = addZero(date.getSeconds())
    ms.innerHTML = addZeroZero(date.getMilliseconds())
    date.setMilliseconds(date.getMilliseconds() - 10)
}

let myInt = null

window.addEventListener("load", function() {
    getTime()
    myInt = setInterval(getTime, 10)
})

// btn_reset.addEventListener("click", function() {}