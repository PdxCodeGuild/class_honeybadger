//
// function random_element(arr) {
//           let index = Math.floor(Math.random()*arr.length)
//           return arr[index]
//         }
// //
// //       let length = 8
//       let choices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z',1,2,3,4,5,6,7,8,9]
//
//       function randompassword() {
//       let password = random_element(choices)
//       return password
//     }
//     console.log()

// function generatePassword() {
//     let length = 8,
//         charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
//         password = "";
//     for (let i = 0, n = charset.length; i < length; ++i) {
//         password += charset.charAt(Math.floor(Math.random() * 8));
//     }
//     return password;
// }

function randomPassword() {
   let result = ''
   let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
   let password_length = 20
   let len_alpha = alphabet.length
   for (let i = 0; i < password_length; ++i) {
      result += alphabet.charAt(Math.floor(Math.random() * len_alpha))
   }
   return result
}

console.log(randomPassword())
