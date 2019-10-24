//code to generate a random element or random number

function random_element(arr) {
  let index = Math.floor(Math.random()*arr.length)
  return arr[index]
}
function random_integer(a, b) {
  return Math.floor(a + Math.random()*(b-a+1))
}