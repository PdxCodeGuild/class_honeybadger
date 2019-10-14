let clock = document.querySelector("#clock")
let day_of_week = document.querySelector("#day_of_week")
let month = document.querySelector("#month")
let day = document.querySelector("#day")
let year = document.querySelector("#year")
let hour = document.querySelector("#hour")
let minute = document.querySelector("#minute")
let second = document.querySelector("#second")

let christian_now = document.querySelector("#christian_now")
let hunter_now = document.querySelector("#hunter_now")
let lily_now = document.querySelector("#lily_now")
let ashlyn_now = document.querySelector("#ashlyn_now")

let christian_next = document.querySelector("#christian_next")
let hunter_next = document.querySelector("#hunter_next")
let lily_next = document.querySelector("#lily_next")
let ashlyn_next = document.querySelector("#ashlyn_next")

let christian_days = document.querySelector("#christian_days")
let hunter_days = document.querySelector("#hunter_days")
let lily_days = document.querySelector("#lily_days")
let ashlyn_days = document.querySelector("#ashlyn_days")

let test = document.querySelector("#test")

let date = new Date()

function addZero(num) {
    return (num < 10) ? "0" + num : num
}

function dayName(num) {
    let day_name = null
    if (date.getDay() == 0) {
        day_name = "Sunday"
    } else if (date.getDay() == 1) {
        day_name = "Monday"
    } else if (date.getDay() == 2) {
        day_name = "Tuesday"
    } else if (date.getDay() == 3) {
        day_name = "Wednesday"
    } else if (date.getDay() == 4) {
        day_name = "Thursday"
    } else if (date.getDay() == 5) {
        day_name = "Friday"
    } else if (date.getDay() == 6) {
        day_name = "Saturday"
    }
    return day_name
}

function monthName(num) {
    let month_name = null
    if (date.getMonth() == 0) {
        month_name = "January"
    } else if (date.getMonth() == 1) {
        month_name = "February"
    } else if (date.getMonth() == 2) {
        month_name = "March"
    } else if (date.getMonth() == 3) {
        month_name = "April"
    } else if (date.getMonth() == 4) {
        month_name = "May"
    } else if (date.getMonth() == 5) {
        month_name = "June"
    } else if (date.getMonth() == 6) {
        month_name = "July"
    } else if (date.getMonth() == 7) {
        month_name = "August"
    } else if (date.getMonth() == 8) {
        month_name = "September"
    } else if (date.getMonth() == 9) {
        month_name = "October"
    } else if (date.getMonth() == 10) {
        month_name = "November"
    } else if (date.getMonth() == 11) {
        month_name = "December"
    }
    return month_name
}


let myTime = setInterval(myClock, 1000);

function myClock() {
    let date = new Date()
    day_of_week.innerText = dayName(date.getDay())
    month.innerText = monthName(date.getMonth())
    day.innerHTML = date.getDate()
    year.innerHTML = date.getFullYear()
    hour.innerHTML = addZero(date.getHours())
    minute.innerHTML = addZero(date.getMinutes())
    second.innerHTML = addZero(date.getSeconds())
}



function convertAge(date) {
    let d1 = new Date(); //"now"
    let d2 = new Date(date)
    // let d2 = new Date("1979/10/01") // some date
    let diff = Math.abs(d1 - d2)
    return diff
}

function convertAgeNow(ms) {
    let age = ms * 3.1689E-11
    return Math.round(age)
}

function convertAgeNext(ms) {
    let next_age = ms * 3.1689E-11
    return Math.round(next_age) + 1
}

function convertDaysToBD(month, day) {
    let bd_1 = new Date(date)
    console.log("bd_1 = " + bd_1)
    let next_year = date.getFullYear() + 1
    console.log(next_year)
    let bd_2 = new Date(next_year + "/" + month + "/" + day)
    console.log("bd_2 = " + bd_2)
    let days_to_bd = Math.abs(bd_1 - bd_2)
    // console.log("days_to_bd = " days_to_bd)
    let diff = days_to_bd * 1.1574074074074E-8
    if (Math.round(diff) > 365) {
        return Math.round(diff) - 365
    } else {
        return Math.round(diff)
    }
}


christian_now.innerText = convertAgeNow(convertAge("2004/10/21"))
hunter_now.innerText = convertAgeNow(convertAge("2006/05/24"))
lily_now.innerText = convertAgeNow(convertAge("2007/09/27"))
ashlyn_now.innerText = convertAgeNow(convertAge("2008/11/28"))

christian_next.innerText = convertAgeNext(convertAge("2004/10/21"))
hunter_next.innerText = convertAgeNext(convertAge("2006/05/24"))
lily_next.innerText = convertAgeNext(convertAge("2007/09/27"))
ashlyn_next.innerText = convertAgeNext(convertAge("2008/11/28"))

christian_days.innerText = convertDaysToBD(10, 21)
hunter_days.innerText = convertDaysToBD(05, 24)
lily_days.innerText = convertDaysToBD(09, 27)
ashlyn_days.innerText = convertDaysToBD(11, 28)