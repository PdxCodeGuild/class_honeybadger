
let user_input = document.querySelector("#user_input")
let btn_user_input = document.querySelector("#btn_user_input")
let list = document.querySelector("#list")
let completed = document.querySelector("#completed")

user_input.focus()

user_input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Trigger the button element with a click
    btn_user_input.click() //puts focus on the input field on loading
  }
})

btn_user_input.addEventListener("click", function() {
    if (user_input.value != "") {
        
        let li = document.createElement("li")
        li.classList.add("list_item")
        
        let checkbox = document.createElement("input")
        checkbox.type = "checkbox"
        
    
        checkbox.addEventListener("change", function() {
            if (checkbox.checked) {
                completed.appendChild(li)
            } else {
                list.appendChild(li)
            }
        })

        let span = document.createElement("span")
        span.innerText = user_input.value
    
        li.appendChild(checkbox)
        list.appendChild(li)
        li.appendChild(span)
        user_input.value = ""
        user_input.focus(); //puts focus on the input field after each entry
    } 
})


// this clears the completed items from the list
btn_clear.addEventListener("click", function() {
    completed.innerHTML = ""
})

// this allows the user to print the list
btn_print.addEventListener("click", function() {
    let content = list.innerHTML
    let mywindow = window.open();
    mywindow.document.write(`
    <html>
        <head>
            <title>My List</title>
            <link href="https://fonts.googleapis.com/css?family=Roboto+Mono|Source+Sans+Pro&display=swap" rel="stylesheet">
            <style>
                ul {
                    list-style: none;
                    font-family: 'Roboto Mono', monospace;
                }
                input::checkbox {
                    display: none;
                }
            </style>
        </head>
        <body>
            <ul>
                ${content}
            </ul>
        </body>
    </html>
        
        `)
    mywindow.document.close();
    mywindow.focus()
    mywindow.print();
    mywindow.close();
    return true;
})
