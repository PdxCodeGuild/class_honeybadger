

function add(a, b) {
  return a + b
}
// console.log(add(5, 2))


function is_even(a) {
  return a % 2 === 0
}
// console.log(is_even(984))

function opposites(a,b) {
  return (a < 0 && b > 0) || (a > 0 && b < 0) 
}
// console.log(opposites(0, 4))

function near_100(a) {
  return 90 <= a && a <= 110 
}
// console.log(near_100(-2))

function max3(a, b, c) {
  if (a > b && a > c) {
    return a
  } else if (b > c && b > a){
    return b
  } else {
    return c 
  }
}
// console.log(max3(1,1.7,Math.PI))
// a^0, a^1, a^2, a^3 ... a^20
function power2(a, lower, upper) {
  for(let i=lower, j=1; i <= 20; i++, j*=a) {
    console.log(j)
  }
}
// power2(2)




