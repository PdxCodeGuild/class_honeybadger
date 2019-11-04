function random_integer(a, b) {
  return Math.floor(a + Math.random()*(b-a+1))
}

let user_number = document.querySelector('#user_number')
let number_button = document.querySelector('#number_button')
let user_output = document.querySelector('#user_output')
let computer_output = document.querySelector('#computer_output')




let computer_number = random_integer(1,10)

computer_output.innerText = 'Computer number: ' + computer_number




number_button.addEventListener('click', function() {
    user_output.innerText = 'User number: ' + user_number.value
})
