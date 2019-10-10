

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
// console.log(count_hi('h    iello'))

function count_occurrances(text, word) {
  let re = new RegExp(word, 'g')
  let matches = text.match(re)
  return (matches != null)? matches.length: 0
}
// function count_hi(text) {
//   return count_occurrances(text, 'hi')
// }
// console.log(count_occurrances('hihi  hi hi', 'hellooo')) // 4


function cat_dog(text) {
  let cat_count = count_occurrances(text, 'cat')
  let dog_count = count_occurrances(text, 'dog')
  return cat_count == dog_count
}

// console.log(cat_dog('catdog')) // True
// console.log(cat_dog('catcat')) // False
// console.log(cat_dog('catdogcatdog')) // True



function count_letter(letter, word) {
  // return count_occurrances(word, letter)
  let count = 0
  for (let i=0; i<word.length; ++i) {
    if (word[i] == letter) {
      ++count
    }
  }
  return count
}
console.log(count_letter('i', 'antidisestablishmentterianism')) // 5
console.log(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) // 2


function clean_text(text) {
  return text.toLowerCase().trim()
}
console.log(clean_text("SUPER!")) // 'super!'
console.log(clean_text("        NANNANANANA BATMAN        ")) // 'nannananana batman'
