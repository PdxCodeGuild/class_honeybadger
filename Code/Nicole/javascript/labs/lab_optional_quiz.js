let title = document.querySelector("#title")
let question = document.querySelector("#question")
let answers = document.querySelector("#answers")

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

window.addEventListener("load", function() {
  answers.style.display = "none"
  question.style.display = "none"
  btn_submit.style.display = "none"
  btn_paginate_next.style.display = "none"
  btn_paginate_previous.style.display = "none"
})

btn_begin.addEventListener("click", function() {
  btn_begin.style.display = "none"
  question.style.display = null
  answers.style.display = null
  btn_submit.style.display = null
  btn_paginate_next.style.display = null
  btn_paginate_previous.style.display = null
})



function getAnswers(x) {
  for (let i = 0; i < (quiz.questions[x].answers).length; ++i) {
    answers.style.display = "block"
    question.innerHTML = quiz.questions[x].text

    let label = document.createElement("LABEL")
    label.setAttribute("id", "label")
    answers.appendChild(label)

    let input = document.createElement("INPUT")
    input.setAttribute("id", "input")
    label.appendChild(input)
    input.setAttribute("type", "radio")
    input.setAttribute("name", "radio_answer")
    input.setAttribute("class", "answer_choice")

    let span = document.createElement("SPAN")
    span.setAttribute("id", "span")
    input.appendChild(span)
    span.innerHTML = quiz.questions[x].answers[i].text

    console.log((quiz.questions[x].answers).length) //6
    console.log(label)
    console.log(input)
    console.log(span)
  }
}

getAnswers(0)


// btn_paginate_next.addEventListener("click", function() {
//   for (let i = 1; i < (quiz.questions).length; ++i) {
//     getAnswers(i)
// 
//   }
// })








// console.log(quiz.questions[0].text)
// question.innerHTML = quiz.questions[0].text
// a1.innerHTML = quiz.questions[0].answers[0].text