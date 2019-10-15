
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

// adds leading zeros to two digit numbers
function addZero(num) {
  return (num < 10) ? "0" + num : num
}

// adds leading zeros to three digit numbers
function addZeroZero(num) {
  if (num < 10) {
    return "00" + num
  } else if (num >= 10 && num < 100) {
    return "0" + num
  } else
    return num
}

date.setHours(0, 0, 0, 0)

let myTime = setInterval(myClock, 1000)

