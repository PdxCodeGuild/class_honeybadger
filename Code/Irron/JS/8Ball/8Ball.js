//need event selectors for each of these
let btn_question = document.querySelector('#btn_question')
let btn_normal = document.querySelector('#btn_normal')
let btn_sarcasm = document.querySelector('#btn_sarcasm')
let btn_dark = document.querySelector('#btn_dark')
let btn_reset = document.querySelector('#btn_reset')
let normal_text = document.querySelector('#normal_text')
let sarcasm_text = document.querySelector('#sarcasm_text')
let dark_text = document.querySelector('#dark_text')
let div_play_count = document.querySelector('#div_play_count')
let f_string = document.querySelector('#f_string')
let total_count = document.querySelector('#div_total_count')

function random_element(arr) {
    let index = Math.floor(Math.random()*arr.length)
    return arr[index]
  }

let normal_list = random_element(['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'Most likely.', 'Outlook good.',
    'Yes', 'Signs point to yes.'])

let sarcasm_list = random_element(['What do you think?', 'Is that really your question?', 'Oh, come on Man!', 'Dude...Really?','Concentrate....and ask again.','Reply is a bit hazy...try again tomorrow', 'Im Busy At The Moment.'])

let dark_list = random_element(['Glad you asked today because the world is going to end tomorrow.', 'Your going to die!', 'Go To Hell!', 'Very doubtful.', 'Outlook not so good. Please, no more questions!!'])


let user_input = ''

function userQuestion() {
    user_input = prompt('What is your question?')  
    f_string.innerText = `You asked the question: "${user_input}". \n \n The Magic 8 Ball has an answer! \n \n Please select a category to obtain it.`
}
    
function play_8Ball(player_choice){

    if (player_choice == 'normal'){
        //normal_text.innerText = ''
        sarcasm_text.innerText = ''
        dark_text.innerText = ''
        f_string.innerText = `The answer to your "Career" question is:` 
        normal_text.innerText = normal_list
        //console.log (play_count)

    } else if(player_choice == 'sarcasm'){
        normal_text.innerText = ''
        //sarcasm_text.innerText = ''
        dark_text.innerText = ''
        f_string.innerText = `The answer to your "Relationship" question is:`
        sarcasm_text.innerText = sarcasm_list
        //console.log (play_count)

    } else if(player_choice = 'dark') {
        normal_text.innerText = ''
        sarcasm_text.innerText = ''
        //dark_text.innerText = ''
        f_string.innerText = `The answer to your "Happiness & Mindset" question is:`
        dark_text.innerText = dark_list
        //console.log (play_count)
    
    }  }


btn_normal.addEventListener('click', function(){
    play_8Ball('normal')})

btn_sarcasm.addEventListener('click', function(){
    play_8Ball('sarcasm')})

btn_dark.addEventListener('click', function(){
    play_8Ball('dark')})

btn_question.addEventListener('click', function(){
    userQuestion()
    }) 

btn_reset.addEventListener('click', function(){
    resetGame()
})

//Counting Button Clicks
//created an HTML element by creating div ids to gain accessibility to the DOM (#btn_normal)
//used the querySelector method to select the #btn_normal id on the button element
//declared variable to store number of clicks, default value =0
//attached an event listener to the btn_question by using addEventListner method
//inside event listener, specify listening for clicks events and want to execute a function on every click event
//inside function, specify want to add 1 to countButtonNormalClicks variable every time click event is triggered 

let buttonNormal = document.querySelector('#btn_normal')
let countButtonNormalClicks = 0
let total_normal = 0
buttonNormal.addEventListener('click', function() {
    countButtonNormalClicks += 1
    total_normal = countButtonNormalClicks*3
    //console.log(countButtonNormalClicks)
    div_play_count.innerText = `You have asked ${countButtonNormalClicks} "Career" question(s) and invested $${total_normal} to change your career trajectory. Money well spent!
                                Ready for more invaluable insights? Click the QUESTION button and another category.`
    return total_normal})

let buttonSarcasm = document.querySelector('#btn_sarcasm')
let countButtonSarcasmClicks = 0
let total_sarcasm = 0

buttonSarcasm.addEventListener('click', function() {
    countButtonSarcasmClicks += 1
    total_sarcasm = countButtonSarcasmClicks*3
    //console.log(countButtonSarcasmClicks)
    div_play_count.innerText = `You have asked ${countButtonSarcasmClicks} "Relationship" question(s). Congrats! The value of your relationship is worth a whopping $${total_sarcasm}.
                                Click the QUESTION button and another category for additional Magic 8 predictions.`
    return total_sarcasm})

let buttonDark = document.querySelector('#btn_dark')
let countButtonDarkClicks = 0
let total_dark = 0

buttonDark.addEventListener('click', function() {
    countButtonDarkClicks += 1
    total_dark =countButtonDarkClicks*3
    //console.log(countButtonDarkClicks)
    div_play_count.innerText = `You have asked ${countButtonDarkClicks} "Happiness & Mindset" question(s). The total cost of your happy mind is $${total_dark}.
                                Please click the QUESTION button and another category if you want Magic 8 to make another prediction.`
    return total_dark
})

let total_questions = countButtonNormalClicks+countButtonSarcasmClicks+countButtonDarkClicks
//console.log(total_questions)
let total_cost = total_normal+total_sarcasm+total_dark
//total_count.innerText = `You asked a total number of ${total_questions} questions, totaling $${total_cost}`

//resetting game
function resetGame() {
    normal_text.innerText = ''
    sarcasm_text.innerText = ''
    dark_text.innerText = ''
    f_string.innerText = ''
    div_play_count.innerText = ''
    countButtonNormalClicks = 0
    countButtonSarcasmClicks = 0
    countButtonDarkClicks = 0
}

//let magic8_normal = random_element(normal)
//let magic8_sarcasm = random_element(sarcasm)
//let magic8_dark = random_element(dark)
//checking to see if random is working
//alert(magic8_normal)
//alert(magic8_sarcasm)
//alert(magic8_dark)


