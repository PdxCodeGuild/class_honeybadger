

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

// render quiz title
document.getElementById("title_div").innerHTML = quiz.title

// grab the question box
let questions = quiz.questions[0].text
let question_box = document.getElementById("question_box")
let answers = quiz.questions[0].answers

//render the quiz questions
document.getElementById("question_box").innerHTML = quiz.questions[0].text
//render the quiz answers
// console.log(document.getElementById("answers").innerHTML = quiz.questions[0].answers[0].text)

// for question in questions:
    // build html and enter questions[i].text

// console.log(questions)


for (i = 0; i < answers.length; i++) {
    var answer_btns = document.createElement("input");
    var answer_text = document.createElement("span");
    var break_line = document.createElement("br")
    answer_btns.setAttribute("type" , "radio")
    answer_btns.setAttribute("name" , "answer")
    answer_text.innerHTML = quiz.questions[0].answers[i].text;
    document.body.appendChild(answer_btns);
    document.body.appendChild(answer_text);
    document.body.appendChild(break_line);
    console.log(answer_text)

}
