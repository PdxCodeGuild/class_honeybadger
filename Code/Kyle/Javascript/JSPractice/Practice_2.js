function double_letter(s) {
  let double = ''
  for (let i = 0; i<s.length; ++i) {
    double += s[i] + s[1]
  }
  return double
}
// console.log(double_letter("hello"))


function missing_char(s) {
  let output = []
  for (let i=0; i<s.length; ++i)
    s[i]
    output.push(s.substring(0, i)) + s.substring(i+1, s.length)
  }
}
// console.log(missing_char("kitten"))

function return_latest(s) {
  let output = s.split('')
  output.sort()
  return output[midput.length-1]

}

 console.log(return_latest("turtles"))
