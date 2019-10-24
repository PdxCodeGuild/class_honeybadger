//code to generate a random element or random number

//an argument "arr" is passed to the random_element function.  arr.length finds the length (how many items in array)
//Math.random returns a random number between 0 and 1.  This random number is multiplied by the length of the array
//multiplying the array length * the random number, expands the pool of possible numbers
//Math.floor returns the an integer by removing the decimal
//the function will return the value located at the index
//the function is called in the html file.  the html file reference the js file and pass the parameter
//code needed in the html file to reference the js file = <script type="text/javascript" src="random.js"></script>
function random_element(arr) {
  let index = Math.floor(Math.random()*arr.length)
  return arr[index]
}




