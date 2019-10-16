let title = document.querySelector("#title")
let question = document.querySelector("#question")
let answers = document.querySelector("#answers")
let question_area = document.querySelector("#question_area")

// buttons
let btn_submit = document.querySelector("#btn_submit")
let btn_paginate_next = document.querySelector("#btn_paginate_next")
let btn_begin = document.querySelector("#btn_begin")
let btn_view_score = document.querySelector("#btn_view_score")


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
})

btn_begin.addEventListener("click", function() {
  btn_begin.style.display = "none"
  question.style.display = null
  answers.style.display = null
  btn_submit.style.display = null
  btn_paginate_next.style.display = null
})

let label = document.createElement("LABEL")
let span = document.createElement("SPAN")
let input = document.createElement("INPUT")


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
    input.setAttribute("checked", "checked")
    input.setAttribute("value", quiz.questions[x].answers[i].correct)

    answers.appendChild(label)
    label.appendChild(input)
    label.appendChild(span)
    span.innerHTML = quiz.questions[x].answers[i].text

  }

  // this determines if the answer is true or false
  btn_submit.addEventListener("click", function() {
    for (let i = 0; i < (quiz.questions[x].answers).length; ++i) {
      if (quiz.questions[x].answers[i].correct == answers.checked) {
        console.log("hello!")
      }
    }
    // if (input.value.checked == true) {
    //   console.log("true")
    // } else {
    //   console.log("false")
    // }
  })

  answers.addEventListener("change", function() {
    // for (let i = 0; i < (quiz.questions[x].answers).length; ++i) {
    //   let is_checked = document.getElementById("answer_input_" + i).value
    //   if (quiz.questions[x].answers[i].correct == is_checked.checked) {
    //     console.log("hello!")
    //   }
    // 
    // }
    for (let i = 0; i < (quiz.questions[x].answers).length; ++i) {
      let is_checked = quiz.questions[x].answers[i].correct
      console.log(input.checked)
      if (is_checked == input.checked) {
        console.log("hello!")
      }

    }
  })
}


question_i = 0

function nextQuestion() {
  question.innerHTML = ""
  answers.innerHTML = ""
  if (question_i == (quiz.questions).length) question_i = 0; {
    getAnswers(question_i)
      ++question_i
  }
  if (question_i == (quiz.questions).length) {
    console.log("yoyo")
  }
}







// console.log(quiz.questions[0].text)
// question.innerHTML = quiz.questions[0].text
// a1.innerHTML = quiz.questions[0].answers[0].text