
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

const countDownInputsHrs = document.querySelector("#countDownInputsHrs")

const countDownInputsMins = document.querySelector("#countDownInputsMins")

const countDownInputsSecs = document.querySelector("#countDownInputsSecs")

const countDownDisplay = document.querySelector("#countDownDisplay")

const countDownStartBtn = document.querySelector("#countDownStartBtn")

function keyWatch() {
    const total = Date.now() // milliseconds since Jan. 1st, 1970 in UST
    const milliseconds = total
    const seconds = Math.floor(total/1000)
    const minutes = Math.floor(total/60000)
    const hours = (Math.floor(total/3600000) + 17) //set to PST
    const days = Math.floor(total/86400000) % 365
    const years = Math.floor(total/31536000000)

    let timeArray = [milliseconds,seconds,minutes,hours,days,years]
    return timeArray

}

function displayUpdate(timeArray) {
    
    msDisplay.innerText = timeArray[0] % 1000
    secDisplay.innerText = timeArray[1] % 60
    minDisplay.innerText = timeArray[2] % 60
    hrDisplay.innerText = timeArray[3] % 24
    dayDisplay.innerText = timeArray[4] % 365
    yrDisplay.innerText = timeArray[5] + 1970

}

let interval = null

function stopWatch() {
    if (interval) {
        clearInterval(interval)
        interval = null
        return
    }
    
    let timeStart = masterTime[0]

    interval = setInterval(function() {
        let diff = masterTime[0]-timeStart

        const milliseconds = diff % 1000
        const seconds = Math.floor(diff/1000) % 60
        const minutes = Math.floor(diff/60000) % 60
        stopDisplay.innerText = `${minutes}:${seconds}:${milliseconds}`
    

    }, 1)
   
}

function countDown() {
    const runHrs = countDownInputsHrs.value * 3600
    const runMins = countDownInputsMins.value * 60
    const runSecs = countDownInputsSecs.value

    runTime = runHrs + runMins + runSecs

    let timeStart = masterTime[1]

    let runFlag = true

    while (runFlag) {   
        interval = setInterval(function() {
            let diff = masterTime[1]-timeStart
            
            let curTime = runTime - diff 

            const seconds = Math.floor(diff/1000)
            const minutes = Math.floor(diff/60000)
            const hours = Math.floor(diff/3600000)

            const endSecs = (runSecs - seconds)
            const endMins = (runMins - minutes)
            const endHrs = runHrs - hours
            countDownDisplay.innerText = `${endHrs}:${endMins}:${endSecs}`
            
            if (curTime == 0) {
                runFlag = false
            }

        }, 1000)
    }

}

let masterTime
setInterval(function() {
    masterTime = keyWatch()
},1)

setInterval(function() {
    displayUpdate(masterTime)
},1)

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

countDownStartBtn.addEventListener("click", function() {
    countDown()
})
