//code to generate a random element or random number

//an argument "arr" is passed to the random_element function.  arr.length finds the lenght (how many items in array)
//Math.random returns a random number between 0 and 1.  This random number is multiplied by the lenght of the array
//multiplying the array length * the random number, expands the pool of possible numbers
//Math.floor returns the an integer by removing the decimal
//the function will return the value located at the index
//the function is called in the html file.  the html file reference the js file and pass the parameter
//code needed in the html file to reference the js file = <script type="text/javascript" src="random.js"></script>
function random_element(arr) {
  let index = Math.floor(Math.random()*arr.length)
  return arr[index]
}


//function receives parameters 5 and 10  
//multiplies the random number by 5, (got 5 by subtracting 10-5 or b-a) 
//Then adds 5 (variable a) to 5, which equals 10; basically expands the range of random numbers
function random_integer(a, b) {
  return Math.floor(a + Math.random()*(b-a+1))
}

for (let i=0; i<10; ++i) {  //while i is less than 100, print console. after each iteration, ++1 increases i by 1. Returns random numbers between 5 and 10
  console.log(random_integer(5,10))
}

//While loop equivalent. 

let i = 0
while (i<100) {
    i++}


