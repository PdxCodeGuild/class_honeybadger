let input_quote = document.querySelector("#input_quote")
let div_quote = document.querySelector("#div_quote")
let div_author = document.querySelector("#div_author")

div_quote.style.display = "none"
div_author.style.display = "none"

input_quote.focus()

function loadRandomQuote() {
    let url = "https://favqs.com/api/quotes"
    axios({
            headers: {
                Authorization: `Token token="${quote_api_key}"`
            },
            method: 'get',
            url: url,
            responseType: 'text',
            params: {
                filter: input_quote.value
            },
        })
        .then(function(response) {
            for (let i = 0; i < response.data.quotes.length; ++i) {
                if (response.data.quotes[i].body == "No quotes found") {
                    return
                } else {
                    // adds quotes
                    let blockquote = document.createElement("blockquote")
                    div_quote.appendChild(blockquote)
                    blockquote.innerText = response.data.quotes[i].body

                    // adds author
                    let p = document.createElement("P")
                    p.classList.add("div_author")
                    div_quote.appendChild(p)
                    p.innerText = response.data.quotes[i].author
                }
            }
        });
}

input_quote.addEventListener("input", function() {
    console.log("hello")
    div_quote.style.display = null
    div_author.style.display = null
    loadRandomQuote()
})

input_quote.addEventListener("change", function() {
    console.log("change")
    div_quote.innerText = ""
    div_author.innerText = ""
    input_quote.select()
})