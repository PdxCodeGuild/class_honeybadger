let clock = document.querySelector("#clock")
let hour = document.querySelector("#hour")
let minute = document.querySelector("#minute")
let second = document.querySelector("#second")
let ms = document.querySelector("#ms")
let btn_start = document.querySelector("#btn_start")
let ul_lap = document.querySelector("#ul_lap")
let stopwatch_icon = document.querySelector("#stopwatch_icon")
let btn_reset = document.querySelector("#btn_reset")

let stopwatch_off = '<span><i class="fad fa-stopwatch"></i></span>'
let stopwatch_on = '<span style="color: green;"><i class="fad fa-stopwatch"></i></span>'

let date = new Date()
date.setHours(0, 0, 0, 0)

hour.innerHTML = "00"
minute.innerHTML = "00"
second.innerHTML = "00"
ms.innerHTML = "00"

btn_start.innerText = "START TIMER"
stopwatch_icon.innerHTML = stopwatch_off


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
    date.setMilliseconds(date.getMilliseconds() + 10)
}

let myInt = null

btn_start.addEventListener("click", function() {
    let toggle = ""
    if (btn_start.innerText == "START TIMER") {
        toggle = "STOP"
        getTime()
        btn_start.className = "btn-large red lighten-2"
        stopwatch_icon.innerHTML = stopwatch_on
        myInt = setInterval(getTime, 10)
    } else {
        toggle = "START TIMER"
        btn_start.className = "btn-large cyan"
        stopwatch_icon.innerHTML = stopwatch_off
        clearInterval(myInt)
    }
    btn_start.innerText = toggle
})

btn_lap.addEventListener("click", function() {
    let li = document.createElement("li")
    li.innerText = addZero(date.getHours()) + " : " + addZero(date.getMinutes()) + " : " + addZero(date.getSeconds()) + " : " + addZero(date.getMilliseconds())
    ul_lap.appendChild(li)
})

btn_reset.addEventListener("click", function() {
    stopwatch_icon.innerHTML = stopwatch_off
    toggle = "START TIMER"
    date.setHours(0, 0, 0, 0)
    hour.innerHTML = "00"
    minute.innerHTML = "00"
    second.innerHTML = "00"
    ms.innerHTML = "00"
    clearInterval(myInt)
    ul_lap.innerText = ""
})