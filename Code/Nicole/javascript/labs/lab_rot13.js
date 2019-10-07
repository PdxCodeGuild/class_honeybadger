
let user_input = document.querySelector("#user_input")
let user_num = document.querySelector("#user_num")
let button_submit = document.querySelector("#button_submit")
let rot13_output = document.querySelector("#rot13_output")

function rot13(phrase, num) {
    let alpha  = "abcdefghijklmnopqrstuvwxyz"
    let cipher = ""
    for (let i=0; i<phrase.length; ++i) {
        // this part is not working
        let phrase_char = phrase[i]
        for (let j=0; j<alpha.length; ++j) {
            if (phrase_char == alpha[j]) {
                cipher += alpha[(j + num)%26]
            }
        }
    }
    return cipher
}

button_submit.addEventListener("click", function() {
    rot13_output.innerText = rot13(user_input.value, parseInt(user_num.value))
    
})