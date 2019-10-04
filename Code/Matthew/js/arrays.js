


let fruits = ['apple', 'banana', 'pear']
fruits[0] += '!'
fruits.push('cherries')
console.log(fruits)
let last_element = fruits.pop()
console.log(fruits)
console.log(last_element)

fruits.unshift('avocado')
console.log(fruits)

let first_element = fruits.shift()
console.log(fruits)
console.log(first_element)

console.log(fruits.indexOf('pear'))

fruits.push('pineapple')
fruits.push('tomato')
fruits.push('mango')
fruits.push('kiwiwiwi')
console.log(fruits)
let rezult = fruits.splice(1, 2)
console.log(fruits)
console.log(rezult)



console.log(fruits.join(' - '))


let fruits2 = fruits.concat(['kumquat', 'orange', 'pomelo', 'pomegranate', 'lychee'])
console.log(fruits)
console.log(fruits2)
fruits = fruits2


console.log(fruits.slice(0, 3))
console.log(fruits)


fruits.push(5)
fruits.push(6)
fruits.push('6')
fruits.sort()
console.log(fruits)




