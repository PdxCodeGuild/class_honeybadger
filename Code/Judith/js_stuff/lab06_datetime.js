
const msDisplay = document.querySelector("#ms")

const secDisplay = document.querySelector("#sec")

const minDisplay = document.querySelector("#min")

const hrDisplay = document.querySelector("#hr")

const dayDisplay = document.querySelector("#day")

const yrDisplay = document.querySelector("#yr")

const stopDisplay = document.querySelector("#stopDisplay")

const stopBtn = document.querySelector("#stopBtn")

const saveBtn = document.querySelector("#saveBtn")

const clearBtn = document.querySelector("#clearBtn")

const saveList = document.querySelector("#saveList")

function keyWatch() {
    const total = Date.now() // milliseconds since Jan. 1st, 1970 in UST
    const milliseconds = total % 1000
    const seconds = Math.floor(total/1000) % 60
    const minutes = Math.floor(total/60000) % 60
    const hours = (Math.floor(total/3600000) + 17) % 24 //set to PST
    const days = Math.floor(total/86400000) % 365
    const years = Math.floor(total/31536000000) + 1970

    let timeArray = [milliseconds,seconds,minutes,hours,days,years]
    return timeArray

}

function displayUpdate(timeArray) {
    
    msDisplay.innerText = timeArray[0]
    secDisplay.innerText = timeArray[1]
    minDisplay.innerText = timeArray[2]
    hrDisplay.innerText = timeArray[3]
    dayDisplay.innerText = timeArray[4]
    yrDisplay.innerText = timeArray[5]

}

let interval = null

function stopWatch() {
    if (interval) {
        clearInterval(interval)
        interval = null
        return
    }
    
    timeStart = Date.now() //keyWatch()
    // const msStart = timeStart[0]
    // const secStart = timeStart[1]
    // const minStart = timeStart[2]

    interval = setInterval(function() {
        // let time = keyWatch()
        let diff = Date.now()-timeStart

        // const ms = time[0]
        // const sec = time[1]
        // const min = time[2]
        // stopDisplay.innerText = `${min-minStart}:${sec-secStart}:${ms-msStart}`
        const milliseconds = diff
        const seconds = Math.floor(diff/1000) % 60
        const minutes = Math.floor(diff/60000) % 60
        stopDisplay.innerText = `${minutes}:${seconds}:${milliseconds}`
    

    }, 1)

    

    
}

setInterval(function() {
    displayUpdate(keyWatch())
}, 1)

stopBtn.addEventListener("click", function() {
    stopWatch()
})

let count = 0

saveBtn.addEventListener("click", function() {
    if (stopDisplay.innerText) {
    ++count
    const savedItem = document.createElement("li")
    let time = `${stopDisplay.innerText}`
    let lap = `Time #${count} `
    savedItem.innerText = lap.concat(time)
    saveList.appendChild(savedItem)
}})

clearBtn.addEventListener("click", function() {
    saveList.innerHTML = ''
})
