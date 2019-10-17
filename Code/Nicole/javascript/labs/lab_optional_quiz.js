let title = document.querySelector("#title")
let question = document.querySelector("#question")
let answers = document.querySelector("#answers")
let question_area = document.querySelector("#question_area")
let true_or_false = document.querySelector("#true_or_false")

let score_area = document.querySelector("#score_area")
let score = document.querySelector("#score")
let question_length = document.querySelector("#question_length")
let score_percent = document.querySelector("#score_percent")

// buttons
let btn_submit = document.querySelector("#btn_submit")
let btn_paginate_next = document.querySelector("#btn_paginate_next")
let btn_begin = document.querySelector("#btn_begin")
let btn_view_score = document.querySelector("#btn_view_score")
let btn_next_disabled = document.querySelector("#btn_next_disabled")


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
  btn_view_score.style.display = "none"
  score_area.style.display = "none"
  btn_next_disabled.style.display = "none"
  score_percent.style.display = "none"
})

btn_begin.addEventListener("click", function() {
  btn_begin.style.display = "none"
  question.style.display = null
  answers.style.display = null
  btn_next_disabled.style.display = null
})

let label = document.createElement("LABEL")
let span = document.createElement("SPAN")
let input = document.createElement("INPUT")

let score_correct = 0
let score_incorrect = 0

// this works --------->
function getAnswers(x) {
  for (let i = 0; i < (quiz.questions[x].answers).length; ++i) {
    answers.style.display = "block"
    answers.className = "posted"
    question.innerHTML = quiz.questions[x].text

    let label = document.createElement("LABEL")
    label.setAttribute("id", "answer_label")
    label.setAttribute("for", "answer_input_" + i)

    let span = document.createElement("SPAN")
    span.setAttribute("id", "answer_span")
    span.setAttribute("for", "answer_input_" + i)

    let input = document.createElement("INPUT")
    input.setAttribute("id", "answer_input_" + i)
    input.setAttribute("type", "radio")
    input.setAttribute("name", "radio_answer")
    input.setAttribute("class", "answer_choice")
    input.setAttribute("value", quiz.questions[x].answers[i].correct)


    // determines if the chosen answer is correct
    input.addEventListener("change", function() {
      // score_area.style.display = null

      if (input.value == "true") {
        ++score_correct
        true_or_false.innerText = "Correct!"
        true_or_false.style.color = "green"
      } else {
        ++score_incorrect
        true_or_false.innerText = "Incorrect"
        true_or_false.style.color = "red"
      }


      // this sets the final buttons after all questions have been answered
      if ((score_correct + score_incorrect) == quiz.questions.length) {
        console.log("long")
        answers.style.pointerEvents = "none"
        answers.style.opacity = "50%"
        btn_paginate_next.style.display = "none"
        btn_next_disabled.style.display = "none"
        btn_submit.style.display = null
      } else {
        console.log("not long")
        answers.style.pointerEvents = "none"
        answers.style.opacity = "50%"
        btn_paginate_next.style.display = null
        btn_next_disabled.style.display = "none"
      }


      score.innerHTML = score_correct
      console.log(score)
      question_length.innerHTML = quiz.questions.length

    }) //end of event listener

    true_or_false.innerText = ""
    answers.appendChild(label)
    label.appendChild(input)
    label.appendChild(span)
    span.innerHTML = quiz.questions[x].answers[i].text

    answers.style.pointerEvents = "auto"
    answers.style.opacity = "100%"

  } // end of loop
} // end of function

question_i = 0

// goes to the next question
function nextQuestion() {
  btn_paginate_next.style.display = "none"
  btn_next_disabled.style.display = null
  question.innerHTML = ""
  answers.innerHTML = ""
  if (question_i == quiz.questions.length) {
    question_i = 0;

  }
  getAnswers(question_i)
    ++question_i

  // if (question_i == (quiz.questions).length) {
  // 
  //   btn_submit.style.display = null
  //   btn_paginate_next.style.display = "none"
  //   btn_next_disabled.style.display = "none"
  // 
  // }
}

function submitScore() {
  answers.style.display = "none"
  question.style.display = "none"
  score_area.style.display = null
  true_or_false.style.display = "none"
  let percent = score_correct / quiz.questions.length
  score_percent.innerText = Math.round(percent * 100)
  score_percent.style.display = null
  btn_submit.style.display = "none"

}