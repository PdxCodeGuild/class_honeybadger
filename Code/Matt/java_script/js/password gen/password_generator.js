

function copyDivToClipboard() {
               var range = document.createRange();
               range.selectNode(document.getElementById("password_div"));
               window.getSelection().removeAllRanges(); // clear current selection
               window.getSelection().addRange(range); // to select text
               document.execCommand("copy");
               window.getSelection().removeAllRanges();
               // to deselect
               }
function randomsort(a, b) {
  return Math.random()>.5 ? -1 : 1;
}

function random_element(arr) {
  let index = Math.floor(Math.random()*arr.length)
  return arr[index]
}

function pw_gen(alphabet, length){
    let password = ''
    for (let i=0; i<length; ++i){
        password += random_element(alphabet)
    }
    return password
}



let alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += alphabet.toUpperCase()
alphabet += '!@#$%^&*()'




let number_of_chars = document.querySelector('#number_of_chars')
let generate_pass = document.querySelector('#generate_pass')
let password_div = document.querySelector('#password_div')




generate_pass_button.addEventListener("click", function() {
    let password = pw_gen(alphabet, number_of_chars.value)

    let shuffled_password = password.split('').sort(randomsort);
    let shuffled_password_string = shuffled_password.join('')
    console.log(shuffled_password_string)
    password_div.innerText = shuffled_password_string



  })

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems, {});
});

password_div.addEventListener("click", function() {
    copyDivToClipboard(password_div)
      M.toast({html: 'copied!'})
});
