

let s = 'hello world'
console.log(s[1]) // e
console.log(s.charCodeAt(1)) // 101 - the ascii code
console.log(s.indexOf('w')) // 6
console.log(s + '!') // hello world!
console.log((s + ' ').repeat(3).trim())
console.log(s.startsWith('hello')) // true
console.log(s.endsWith('world'))
console.log(s.includes('ell'))
console.log('   hello '.trim())
console.log(s.toLowerCase())
console.log(s.toUpperCase())
console.log(s.match(/\w+/gm))
console.log(s.search(/\w+/gm))
console.log(s.replace('world', 'earth'))
console.log(s.split(' ')) // ['hello', 'world']
console.log(s.split('')) // [ 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd' ]
console.log(s.substring(2,5)) // llo

// if (s.includes('hello')) {
// 
// }

console.log(s.includes('hello')? 'includes hello': 'does not include hello')

if (s.includes('hello')) {
  console.log('includes hello')
} else {
  console.log('does not include hello')
}

// reverse an array ================================

function reverse(str) {
  let arr = str.split('')
  arr.reverse()
  return arr.join('')
}

function reverse1(str) {
  let r = ''
  for (let i=0; i<str.length; ++i) {
    r = str[i] + r
  }
  return r
}

function reverse2(str) {
  let r = ''
  for (let i=str.length-1; i>=0; --i) {
    r += str[i]
  }
  return r
}


console.log(reverse(s))
console.log(reverse1(s))
console.log(reverse2(s))



// let myobj = {
//   name: 'matthew',
//   age: 30
// }
// console.log(myobj.name)


let myobj = {
  'name': 'matthew',
  'age': 30
}
console.log(myobj['name'])

for (prop in myobj) {
  console.log(prop + ': ' + myobj[prop])
}



let people = [{
  name: 'matthew',
  age: 30
},{
  name: 'joe',
  age: 2
}]

for (let i=0; i<people.length; ++i) {
  console.log(people[i].age)
}
