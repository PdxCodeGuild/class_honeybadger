
let status = document.querySelector("#status")
let health = document.querySelector("#health")
let money = document.querySelector("#money")
let distance = document.querySelector("#distance")
let time = document.querySelector("#time")
let game = document.querySelector("#game")

health.innerText = 30
money.innerText = 50
distance.innerText = 10
time.innerText = 25

game.style.display = "none"

button_play.addEventListener("click", function() {
    welcome.style.display = "none"
    game.style.display = "block"    
})

