//filename: lab_passgen.js

const upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

const lower = 'abcdefghijklmnopqrstuvwxyz'

const numbers = '0123456789'

const special = '!?#$%&~'

const display = document.querySelector("#display")

const submit = document.querySelector("#submit")



function produce(upperNum,lowerNum,numberNum,specialNum,includeThis) {

    const product = []
    
    for (let i = 0; i < upperNum; i++) {product.push(upper[Math.floor(Math.random() * upper.length)])}

    for (let i = 0; i < lowerNum; i++) {product.push(lower[Math.floor(Math.random() * lower.length)])}

    for (let i = 0; i < specialNum; i++) {product.push(special[Math.floor(Math.random() * special.length)])}

    for (let i = 0; i < numberNum; i++) {product.push(numbers[Math.floor(Math.random() * numbers.length)])}

    product.push(includeThis)
   
    for (let i = 0; i < product.length; i++) {
        if (Math.round(Math.random())) {
            console.log(product)
            character = product[i]
            console.log(character)
            product.splice(product.indexOf(product[i]), 1)
            console.log(product)
            product.splice(Math.floor(Math.random() * product.length), 0, character)
            console.log(product)
        }
    }



    display.innerText = product.join('')
}

const upperNum = document.querySelector("#upperNum")

const lowerNum = document.querySelector("#lowerNum")

const numberNum = document.querySelector("#numberNum")

const specialNum = document.querySelector("#specialNum")

const includeThis = document.querySelector("#includeThis")

const selectors = [upperNum, lowerNum, numberNum, specialNum, includeThis];

function getValues() {
    return selectors.map((selector) => selector.value);
}

submit.addEventListener("click", function() {
    /*const upperNum = document.querySelector("#upperNum").value

    const lowerNum = document.querySelector("#lowerNum").value

    const numberNum = document.querySelector("#numberNum").value

    const specialNum = document.querySelector("#specialNum").value

    const includeThis = document.querySelector("#includeThis").value
    */

    produce(...getValues());
    //produce(upperNum,lowerNum,numberNum,specialNum,includeThis)
})
