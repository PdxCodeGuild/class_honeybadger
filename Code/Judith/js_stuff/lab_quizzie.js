//lab_quizzie.js

let quiz = {
    title: 'JavaScript Quiz',
    questions: [{
      text: 'How do you increment a number in JavaScript?',
      answers: [{
        text: 'i = i + 1',
        correct: false
      },{
        text: 'i += 1',
        correct: false
      },{
        text: 'i++',
        correct: false
      },{
        text: '++i',
        correct: false
      },{
        text: 'i -= -1',
        correct: false
      },{
        text: 'all of the above',
        correct: true
      }]
    },{
      text: 'In what order are the parts of a for loop?',
      answers: [{
        text: 'initialization, condition, increment',
        correct: true
      },{
        text: 'condition, initialization, increment',
        correct: false
      },{
        text: 'initialization, increment, condition',
        correct: false
      },{
        text: 'condition, initialization, increment',
        correct: false
      }]
    },{
      text: 'What\'s the difference between == and ===?',
      answers: [{
        text: 'nothing',
        correct: false
      },{
        text: '== coerces types, === does not',
        correct: true
      },{
        text: '=== coerces types, == does not',
        correct: false
      }]
    }]
  }

function quizGen(quiz) {
    quizTitle.innerText = quiz.title

    let questions = quiz.questions
    let questNum = 0
    
    for (let q of questions) {
        ++questNum
        
        let questWrapper = document.createElement("div")
        questWrapper.setAttribute("id", `questNum-${questNum}-wrapper`)

        let questText = document.createElement("h3")
        questText.setAttribute("id", `questNum-${questNum}`)
        questText.innerText = q.text
        questWrapper.appendChild(questText)

        let answers = q.answers
        let ansNum = 0
        for (let {text: t, correct: c} of answers) {
            ++ansNum
            let ansWrapper = document.createElement("div")
            ansWrapper.setAttribute("id", `${questNum}-${ansNum}-wrapper`)

            let answer = document.createElement("input")
            answer.setAttribute("id", `${questNum}-${ansNum}`)
            answer.setAttribute("type", "radio")
            answer.setAttribute("name", `${questNum}-answers`)
            answer.setAttribute("data-correct", c)

            let ansLabel = document.createElement("label")
            ansLabel.setAttribute("for", `${questNum}-${ansNum}`)
            ansLabel.innerText = t
            ansWrapper.appendChild(answer)
            ansWrapper.appendChild(ansLabel)
            questWrapper.appendChild(ansWrapper)

        }

        let subBtn = document.createElement("button")
        subBtn.setAttribute("id", `${questNum}-btn`)
        questWrapper.appendChild(subBtn)

        subBtn.addEventListener("click", function() {
            scoreNext()
        })

        quizBody.appendChild(questWrapper)

        
    }
}

let quizTitle = document.querySelector("#quizTitle")
let quizBody = document.querySelector("#quizBody")

quizGen(quiz)

