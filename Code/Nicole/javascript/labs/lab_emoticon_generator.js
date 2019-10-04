
let button_submit = document.querySelector("#button_submit")
let random_emoticon = document.querySelector("#random_emoticon")

function random_element(arr) {
  let index = Math.floor(Math.random()*arr.length)
  return arr[index]
}
button_submit.addEventListener('click', function() {
    let eyes = [":", ";", "):", ":`", "|:"]
    let noses = ["-", "•", ">"]
    let mouths = ["D", "|", "P", ")", "("]

    random_emoticon.innerText = random_element(eyes) + random_element(noses) + random_element(mouths)

})