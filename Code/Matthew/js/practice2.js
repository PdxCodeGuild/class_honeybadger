

function double_letters(s) {
  let double = ''
  for (let i=0; i<s.length; ++i) {
    double += s[i] + s[i]
  }
  return  double
}
// console.log(double_letters('hello')) // hheelllloo


function missing_char(s) {
  let output = []
  for (let i=0; i<s.length; ++i) {
    output.push(s.substring(0, i) + s.substring(i+1, s.length))
    // output.append(s[:i] + s[i+1:]) python way
  }
  return output
}
// console.log(missing_char('kitten')) // ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']



function latest_letter(s) {
  let midput = s.split('')
  midput.sort()
  return midput[midput.length-1]
}
function latest_letter2(s) {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz'
  let running_max = 0
  for (let i=0; i<s.length; ++i) {
    let index = alphabet.indexOf(s[i])
    if (index > running_max) {
      running_max = index
    }
  }
  return alphabet[running_max]
}
// console.log(latest_letter2('pneumonoultramicroscopicsilicovolcanoconiosis')) // v


function count_hi(s) {
  s = s.toLowerCase()
  let matches = s.match(/hi/g)
  return (matches != null)? matches.length: 0
  
  // let count = 0
  // for (let i=0; i<s.length-1; ++i) {
  //   if (s[i] == 'h' && s[i+1] == 'i') {
  //     count += 1
  //   }
  // }
  // return count
  
}
// console.log(count_hi('hihihey34hiHI'))
console.log(count_hi('h    iello'))






