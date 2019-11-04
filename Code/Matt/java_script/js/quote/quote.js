let quote_div = document.querySelector("#quote_div")
let get_quote_button = document.querySelector("#get_quote_button")
let filter_text = document.querySelector("#filter_text")
let filter_input_button = document.querySelector("#filter_input_button")
let url = 'https://favqs.com/api/quotes/'
let quote_output = document.querySelector("#quote_output")



// gets the the quote using a filter
get_quote_button.addEventListener('click', function(){
    let filter = filter_text.value

    axios({

        url: url,
        method: 'get',
        headers: {
          'Authorization': 'Token token="' + api_key + '"'
        },

        params: {
         filter: filter
        },


    }).then(function(response) {
        for (let i=0;i<10;++i){
            var output_div = document.createElement("h3")
            quote_output.appendChild(output_div);
            output_div.innerText = response.data.quotes[i].body

            console.log(response.data.quotes[0].body)
            console.log(response.data)
            // let author = response.data.quote.author
            // let quote = response.data.quote.body
            // quote_div.innerText = `Author: ${author} \n Quote: ${quote}`
        }
    })
    console.log(filter_text)
})
