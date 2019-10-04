
let adj_1 = document.querySelector("#adj_1")
let noun_1 = document.querySelector("#noun_1")
let verb_1 = document.querySelector("#verb_1")
let adverb_1 = document.querySelector("#adverb_1")
let adj_2 = document.querySelector("#adj_2")
let noun_2 = document.querySelector("#noun_2")
let noun_3 = document.querySelector("#noun_3")
let adj_3 = document.querySelector("#adj_3")
let verb_2 = document.querySelector("#verb_2")
let adverb_2 = document.querySelector("#adverb_2")
let verb_3 = document.querySelector("#verb_3")
let adj_4 = document.querySelector("#adj_4")
let button_submit = document.querySelector("#button_submit")

function val(input) {
    return '<b>' + input.value.toLowerCase().trim() + '</b>'
}

button_submit.addEventListener('click', function() {
    form_output.innerHTML = "Today I went to the zoo. I saw a " + val(adj_1) + " "+ val(noun_1) + " jumping up and down in its tree. He " + val(verb_1) + " " + val(adverb_1) + " through the large tunnel that led to its " + val(adj_2) + " "+ val(noun_2) + ". I got some peanuts and passed them through the cage to a gigantic gray " + val(noun_3) + " towering above my head. Feeding that animal made me hungry. I went to get a " + val(adj_3) + " scoop of ice cream. It filled my stomach. Afterwards I had to " + val(verb_2) + " " + val(adverb_2) + " to catch our bus. When I got home I " + val(verb_3) + " my mom for a " + val(adj_4) + " day at the zoo."
})

