function translate_Into_Roman(input) {
    for (i=0; i<input.length); i++) {
      let count = (input / ints[i])
      let result.push(roman[i] * count)
      let input -= ints[i] * count
    alert(''.join(result))
}
  let ints =  [1000, 900, 500, 400, 100, 90,  50, 40,  10,  9,    5,   4,   1];

  let roman = ['M', 'CM', 'D', 'CD', 'C','XC','L','XL','X', 'IX','V', 'IV','I']

alert(translateIntoRoman(999))
