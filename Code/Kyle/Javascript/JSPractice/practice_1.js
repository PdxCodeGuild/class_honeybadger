function add(a, b) {
  return a + b
}
// console.log(add(5, 2))

function is_even(a) {
  return a % 2 == 0
}
// console.log(is_even(2))

function opposites(a, b) { // true if one num is pos and other is neg
 return (a < 0 && b > 0) || (a > 0 && b < 0) // || is "or" in js
}
// console.log(opposites(4, -2))

function near_100(a) {
  return (a > 89 && a < 111)
}
// console.log(near_100(97))

function max3(a, b, c) {
  if (a > b && a > c) {
    return a
  }
  else if (b > a && b > c) {
  return b
  }
  else {
    return c
  }
}
// console.log(max3(2, 9, 11))

function power2(a) {
  for(let i = 0; i <= 20; i++) {
  console.log(Math.pow(a, i))
  }
}
console.log(power2(2))
