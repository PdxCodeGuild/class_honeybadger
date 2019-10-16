let div_quote = document.querySelector("#div_quote")
let btn_quote = document.querySelector("#btn_quote")
let div_author = document.querySelector("#div_author")

div_quote.style.display = "none"
div_author.style.display = "none"

function loadRandomQuote() {
    let url = "https://favqs.com/api/qotd"
    axios({
            method: 'get',
            url: url,
            responseType: 'text',
        })
        .then(function(response) {
            div_quote.innerText = response.data.quote.body
            div_author.innerText = response.data.quote.author
        });
}

btn_quote.addEventListener("click", function() {
    div_quote.style.display = null
    div_author.style.display = null
    loadRandomQuote()
})