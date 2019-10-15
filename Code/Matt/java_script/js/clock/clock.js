let clock_div = document.querySelector('#clock_div')
let generate_time_button = document.querySelector('#generate_time_button')
let stop_watch_start = document.querySelector('#stop_watch_start')
let stop_watch_stop = document.querySelector('#stop_watch_stop')
let stopwatch_div = document.querySelector('#stopwatch_div')
// let d = new Date();
// d.setHours(0,0,0,0);



// generate_time_button.addEventListener("click", function() {
//     var my_time = setInterval(myTimer, 200);
// });

stop_watch_start.addEventListener('click', function() {
    // setInterval(function() {
        stopwatch_starter()})

    //     d.setSeconds(d.getSeconds()+1)
    //     stopwatch_div.innerText = d
    // }, 1000)
// });



function myTimer() {
    let date = new Date();
                let day = date.getDate()
                let month = date.getMonth()
                let year = date.getFullYear()
    let hours = date.getHours()
    let minutes = date.getMinutes()
let seconds = date.getSeconds()
clock_div.innerText = day + '/' + month + '/' + year + '\n' + 'The time is' + ' ' + hours + ':' + minutes + ':' + seconds
}

function stopwatch_starter() {
var d = new Date();
var h = addZero(d.getHours());
var m = addZero(d.getMinutes());
var s = addZero(d.getSeconds());
  stopwatch_div.innerHTML = h + ":" + m + ":" + s;
}

function addZero(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}
