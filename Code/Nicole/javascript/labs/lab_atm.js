
let div_balance = document.querySelector("#div_balance")

let withdraw_input = document.querySelector("#withdraw_input")
let deposit_input = document.querySelector("#deposit_input")

let submit_withdraw = document.querySelector("#submit_withdraw")
let submit_deposit = document.querySelector("#submit_deposit")

let log = document.querySelector("#log")


let balance = 0.00
div_balance.innerText = balance.toFixed(2)


submit_deposit.addEventListener("click", function() {
    let amount = parseInt(deposit_input.value)
    balance += amount
    // log.innerText += "User deposited $" + amount + "\n";
    div_balance.innerText = balance.toFixed(2)
    deposit_input.value = ""
    let li = document.createElement("li")
    li.innerText = "User deposited $" + amount
    log.appendChild(li)
})

submit_withdraw.addEventListener("click", function() {
    let amount = parseInt(withdraw_input.value)
    balance -= amount
    // log.innerText += "User withdrew $" + amount;
    div_balance.innerText = balance.toFixed(2)
    withdraw_input.value = ""
    let li = document.createElement("li")
    li.innerText = "User withdrew $" + amount
    log.appendChild(li)
})

reset.addEventListener("click", function() {
    withdraw_input.value = ""
    deposit_input.value = ""
    balance = 0.00
    div_balance.innerText = balance.toFixed(2)
    log.innerText = ""
})