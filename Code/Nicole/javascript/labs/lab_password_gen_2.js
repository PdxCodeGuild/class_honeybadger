let btn_password = document.querySelector("#btn_password")
let password_output = document.querySelector("#password_output")
let input_number = document.querySelector("#input_number")
let alert_copy = document.querySelector("#alert_copy")

let uppercase = document.querySelector("#uppercase")
let lowercase = document.querySelector("#lowercase")
let spec_char = document.querySelector("#spec_char")
let digits = document.querySelector("#digits")

let strength_text = document.querySelector("#strength_text")
let strength = document.querySelector("#strength")

input_number.focus() //sets focus on the input box

updatePasswordStrength()
// randomize function
function randomizer(array) {
    let rando = Math.floor(Math.random() * array.length)
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


function updatePasswordStrength() {
    let score = 0
    let v = parseInt(input_number.value)
    let progress = ""
    if (v < 10) {
        score += 10
    }
    if (v >= 10 && v < 20) {
        score += 30
    }
    if (v >= 20 && v <= 32) {
        score += 50
    }

    if (uppercase.checked) {
        score += 10
    } else {
        score -= 10
    }

    if (lowercase.checked) {
        score += 10
    } else {
        score -= 10
    }

    if (spec_char.checked) {
        score += 10
    } else {
        score -= 10
    }

    if (digits.checked) {
        score += 10
    } else {
        score -= 10
    }

    if (score <= 10) {
        progress = '<div class="determinate deep-orange" style="width: 10%"></div>'
        strength_text.innerText = "Meh"
    } else if (score > 10 && score < 20) {
        progress = '<div class="determinate deep-orange lighten-1" style="width: 20%"></div>'
        strength_text.innerText = "Meh"
    } else if (score >= 20 && score < 30) {
        progress = '<div class="determinate deep-orange lighten-2" style="width: 30%"></div>'
        strength_text.innerText = "Too easy to guess"
    } else if (score >= 30 && score < 40) {
        progress = '<div class="determinate deep-orange lighten-3" style="width: 40%"></div>'
        strength_text.innerText = "Too easy to guess"
    } else if (score >= 40 && score < 50) {
        progress = '<div class="determinate amber accent-3" style="width: 50%"></div>'
        strength_text.innerText = "Keep going..."
    } else if (score >= 50 && score < 60) {
        progress = '<div class="determinate amber accent-2" style="width: 60%"></div>'
        strength_text.innerText = "Keep going..."
    } else if (score >= 60 && score < 70) {
        progress = '<div class="determinate amber accent-1" style="width: 70%"></div>'
        strength_text.innerText = "Keep going..."
    } else if (score >= 70 && score < 80) {
        progress = '<div class="determinate lime accent-1" style="width: 80%"></div>'
        strength_text.innerText = "Almost there ..."
    } else if (score >= 80 && score < 90) {
        progress = '<div class="determinate lime accent-2" style="width: 90%"></div>'
        strength_text.innerText = "Almost there ..."
    } else if (score >= 90 && score <= 100) {
        progress = '<div class="determinate green accent-2" style="width: 100%"></div>'
        strength_text.innerText = "Yippee!"
    }
    console.log(progress)
    console.log(score)
    return strength.innerHTML = progress
}

uppercase.addEventListener("input", updatePasswordStrength)
lowercase.addEventListener("input", updatePasswordStrength)
spec_char.addEventListener("input", updatePasswordStrength)
digits.addEventListener("input", updatePasswordStrength)


input_number.addEventListener("input", function() {
    if (parseInt(input_number.value) > 32) {
        input_number.value = 32
    }
    if (parseInt(input_number.value) < 8) {
        input_number.value = 8
    }
    updatePasswordStrength()
})



btn_password.addEventListener("click", function() {
    let special = [",", ".", "'", "\"", "(", ")", "!", "@", "#", "$", "%", "^", "&", "*"]
    let alpha = "abcdefghijklmnopqrstuvwxyz"
    let abc_lower = alpha.toLowerCase().split("")
    let abc_upper = alpha.toUpperCase().split("")
    let dig_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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

    if (digits.checked) {
        all_chars.push(dig_num)
        password.push(randomizer(dig_num)) // adds an uppercase character to the password
    }

    if (all_chars.length == 0) { // checks to make sure that at least one box is checked
        alert("Please check at least one option")
        spec_char.checked = true
        lowercase.checked = true
        uppercase.checked = true
        digits.checked = true
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
    M.toast({
        html: 'Copied!',
        classes: 'rounded toast red accent-2 ',
        inDuration: 500,
        outDuration: 1000,
        displayLength: 2000,
    });

    input_number.focus() //sets focus back on the input box
})

password_output.addEventListener("click", function() {
    copyText()
    M.toast({
        html: 'Copied!',
        classes: 'rounded toast red accent-2 ',
        inDuration: 500,
        outDuration: 1000,
        displayLength: 2000,
    });
    input_number.focus()
})

// copies the password text
function copyText() {
    document.getElementById("password_output").select()
    document.execCommand("copy")
}

// function to shuffle an array, I found this online :)
function shuffle(array) {
    array.sort(() => Math.random() - 0.5)
}