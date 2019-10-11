
let btn_password = document.querySelector("#btn_password")
let password_output = document.querySelector("#password_output")
let input_number = document.querySelector("#input_number")
let alert_copy = document.querySelector("#alert_copy")

input_number.focus() //sets focus on the input box


// randomize function
function randomizer(array) {
    let rando = Math.floor(Math.random()*array.length)
    return array[rando]
}

// allow enter key to work
input_number.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Trigger the button element with a click
    btn_password.click() 
  }
})

btn_password.addEventListener("click", function() {
    let special = [",", ".", "'","\"", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*"]
    let alpha = "abcdefghijklmnopqrstuvwxyz"
    let abc_lower = alpha.toLowerCase().split("")
    let abc_upper = alpha.toUpperCase().split("")
    let all_chars = [special, abc_lower, abc_upper]
    
    let password = ""
    for (let i = 0; i < input_number.value; ++i) {
        let rando_array = randomizer(all_chars)
        let rando_item = randomizer(rando_array)
        password += rando_item
    }
    
    password_output.innerText = password
    
    copyText()
    // setTimeout(alert_copy.innerText = "", 3000)
    
    alert_copy.innerText = "Your password has been copied to the clipboard"
    alert_copy.style.color = "red"
    delay()
    // delay()
    // copyText(password)
    
    input_number.focus()
    // input_number.value = "&nbsp"
})

// function copyText(pw_copy){
//     pw_copy.select()
//     document.execCommand("copy")
//     alert("Your password is copied to the clipboard")
// }

function copyText() {
    document.getElementById("password_output").select()
    document.execCommand("copy")
    // alert("Your password is copied to the clipboard")
}

function delay() {
  setTimeout(function(){ alert_copy.innerText = ""; }, 2000);
}
