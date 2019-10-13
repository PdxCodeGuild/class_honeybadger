let clock = document.querySelector("#clock")
let hour = document.querySelector("#hour")
let minute = document.querySelector("#minute")
let second = document.querySelector("#second")

function addZero(num) {
    return (num < 10) ? "0" + num : num
}

window.addEventListener("load", function() {
    let myTime = setInterval(myClock, 1000);

    function myClock() {
        let date = new Date();
        hour.innerHTML = addZero(date.getHours())
        minute.innerHTML = addZero(date.getMinutes())
        second.innerHTML = addZero(date.getSeconds())
    }


})