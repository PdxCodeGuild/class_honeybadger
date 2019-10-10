
let btn_password = document.querySelector("#btn_password")
let password_output = document.querySelector("#password_output")
let input_number = document.querySelector("#input_number")
let alert_copy = document.querySelector("#alert_copy")

let uppercase = document.querySelector("#uppercase")
let lowercase = document.querySelector("#lowercase")
let spec_char = document.querySelector("#spec_char")

input_number.focus() //sets focus on the input box

// randomize function
function randomizer(array) {
    let rando = Math.floor(Math.random()*array.length)
    return array[rando]
}

// allow enter/return key to work
input_number.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Trigger the button element with a click
    btn_password.click() 
  }
})

input_number.addEventListener("input", function() {
    if (parseInt(input_number.value) > 32) {
        input_number.value = 32
    }
    if (parseInt(input_number.value) < 8) {
        input_number.value = 8
    }
})

btn_password.addEventListener("click", function() {
    let special = [",", ".", "'","\"", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*"]
    let alpha = "abcdefghijklmnopqrstuvwxyz"
    let abc_lower = alpha.toLowerCase().split("")
    let abc_upper = alpha.toUpperCase().split("")
    let all_chars = []
    let password = []
    
    if (spec_char.checked) {
        all_chars.push(special)
        password.push(randomizer(special)) // adds a special character to the password
    }
    
    if (lowercase.checked) {
        all_chars.push(abc_lower)
        password.push(randomizer(abc_lower)) // adds a lowercase character to the password
    }
    
    if (uppercase.checked) { 
        all_chars.push(abc_upper)
        password.push(randomizer(abc_upper)) // adds an uppercase character to the password
    }
    
    if (all_chars.length == 0) { // checks to make sure that at least one box is checked
        alert("Please check at least one option")
        spec_char.checked = true
        lowercase.checked = true
        uppercase.checked = true   
        return  
    }
    
    for (let i = 0; i < input_number.value - all_chars.length; ++i) { // adds items to the password
        let rando_array = randomizer(all_chars)
        let rando_item = randomizer(rando_array)
        password.push(rando_item)
    }
    
    shuffle(password) // shuffles the password
    let pw_string = password.join("") // turn it into a string
    
    
    password_output.innerText = pw_string // show the password on the page
    
    copyText()
    
    // materialize toast
    M.toast({html: 'Copied!', classes: 'rounded toast red accent-2 ', inDuration: 500, outDuration: 1000, displayLength: 2000,});

    input_number.focus()  //sets focus back on the input box
})

password_output.addEventListener("click", function() {
    copyText()
    M.toast({html: 'Copied!', classes: 'rounded toast red accent-2 ', inDuration: 500, outDuration: 1000, displayLength: 2000,});
    input_number.focus()
})

// copies the password text
function copyText() {
    document.getElementById("password_output").select()
    document.execCommand("copy")
}

// function to shuffle an array, I found this online :)
function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
}