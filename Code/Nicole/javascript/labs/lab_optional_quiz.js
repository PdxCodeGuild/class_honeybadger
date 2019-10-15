let title = document.querySelector("#title")
let question = document.querySelector("#question")
let answers = document.querySelector("#answers")
let a1 = document.querySelector("#a1")
let a2 = document.querySelector("#a2")
let a3 = document.querySelector("#a3")
let a4 = document.querySelector("#a4")
let a5 = document.querySelector("#a5")
let a6 = document.querySelector("#a6")

// radio inputs
let radio_a1 = document.querySelector("#radio_a1")
let radio_a2 = document.querySelector("#radio_a2")
let radio_a3 = document.querySelector("#radio_a3")
let radio_a4 = document.querySelector("#radio_a4")
let radio_a5 = document.querySelector("#radio_a5")
let radio_a6 = document.querySelector("#radio_a6")

// buttons
let btn_submit = document.querySelector("#btn_submit")
let btn_paginate_next = document.querySelector("#btn_paginate_next")
let btn_paginate_previous = document.querySelector("#btn_paginate_previous")
let btn_begin = document.querySelector("#btn_begin")


let quiz = {
    title: "JavaScript Quiz",
    questions: [{
        text: "How do you increment a number in JavaScript?",
        answers: [{
            text: "i = i + 1",
            correct: false
        }, {
            text: "i += 1",
            correct: false
        }, {
            text: "i++",
            correct: false
        }, {
            text: "++i",
            correct: false
        }, {
            text: "i -= -1",
            correct: false
        }, {
            text: "all of the above",
            correct: true
        }]
    }, {
        text: "In what order are the parts of a for loop?",
        answers: [{
            text: "initialization, condition, increment",
            correct: true
        }, {
            text: "condition, initialization, increment",
            correct: false
        }, {
            text: "initialization, increment, condition",
            correct: false
        }, {
            text: "condition, initialization, increment",
            correct: false
        }]
    }, {
        text: "What's the difference between == and ===?",
        answers: [{
            text: "nothing",
            correct: false
        }, {
            text: "== coerces types, === does not",
            correct: true
        }, {
            text: "=== coerces types, == does not",
            correct: false
        }]
    }]
}

title.innerHTML = quiz.title

answers.style.display = "none"
question.style.display = "none"
btn_submit.style.display = "none"
btn_paginate_next.style.display = "none"
btn_paginate_previous.style.display = "none"


btn_begin.addEventListener("click", function() {
    btn_begin.style.display = "none"
    question.style.display = null
    answers.style.display = null
    btn_submit.style.display = null
    btn_paginate_next.style.display = null
    btn_paginate_previous.style.display = null
})


function generateQuestions() {
    for (let i = 0; i < (quiz.questions).length; ++i) {
        question.innerHTML = quiz.questions[i].text
        if (quiz.questions[i].answers[i].text != "") {
            radio_a1.style.display = null
            a1.innerHTML = quiz.questions[i].answers[i].text
        } else {
            radio_a1.style.display = "none"
        }
        if (quiz.questions[i].answers[i + 1].text != "") {
            radio_a2.style.display = null
            a2.innerHTML = quiz.questions[i].answers[i + 1].text
        } else {
            radio_a2.style.display = "none"
        }
        if (quiz.questions[i].answers[i + 2].text != "") {
            radio_a3.style.display = null
            a3.innerHTML = quiz.questions[i].answers[i + 2].text
        } else {
            radio_a3.style.display = "none"
        }
        if (quiz.questions[i].answers[i + 3].text != "") {
            radio_a4.style.display = null
            a4.innerHTML = quiz.questions[i].answers[i + 3].text
        } else {
            radio_a4.style.display = "none"
        }
        if (quiz.questions[i].answers[i + 4].text != null) {
            radio_a5.style.display = null
            a5.innerHTML = quiz.questions[i].answers[i + 4].text
        } else {
            radio_a5.style.display = "none"
        }
        if (quiz.questions[i].answers[i + 5].text) {
            radio_a5.style.display = null
            a6.innerHTML = quiz.questions[i].answers[i + 5].text
        } else {
            radio_a6.style.display = "none"
        }
        i++

    }

    btn_paginate_next.addEventListener("click", function() {
                for (let i = 1; i < (quiz.questions).length; ++i) {
                    generateQuestions(i)

                }
            }




            // console.log(quiz.questions[0].text)
            // question.innerHTML = quiz.questions[0].text
            // a1.innerHTML = quiz.questions[0].answers[0].text