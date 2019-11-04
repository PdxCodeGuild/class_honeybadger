let flickr_photos = document.querySelector("#flickr_photos")
let flickr_search = document.querySelector("#flickr_search")
let flickr_sort = document.querySelector("#flickr_sort")
let radios = document.getElementsByName("sort_radio")

let btn_next = document.querySelector("#btn_next")
let btn_previous = document.querySelector("#btn_previous")

let span_current_page = document.querySelector("#span_current_page")
let span_total_pages = document.querySelector("#span_total_pages")
let div_page_nums = document.querySelector("#div_page_nums")
let div_per_page_select = document.querySelector("#div_per_page_select")
let class_num_per_page = document.querySelector(".class_num_per_page")
let results = document.querySelector("#results")


flickr_search.focus() // puts focus on the input

btn_next.style.display = "none" // hides the "next" button on load
btn_previous.style.display = "none" // hides the "previous" button on load
div_page_nums.style.display = "none"

let page_num = 1
let sort_order = "interestingness-desc" // sets default sort order
let num_per_page = results.value
// console.log(results.value)

// this is the function that loads the photos from the search/sort paramaters
function loadFlickrPhotos() {
    let url = "https://www.flickr.com/services/rest/?method=flickr.photos.search"
    axios({
            method: "get",
            url: url,
            responseType: "text",
            params: {
                api_key: flickr_api_key,
                text: flickr_search.value,
                format: "json",
                nojsoncallback: 1,
                content_type: 1,
                page: page_num,
                per_page: num_per_page,
                sort: sort_order,
                safe_search: 1
            }
        })
        .then(function(response) {
            let photos = response.data.photos.photo
            console.log(photos)
            let total_pages = response.data.photos.pages
            for (let i = 0; i < photos.length; ++i) {
                let owner_name = photos[i].owner_name
                let id = photos[i].id
                let farm = photos[i].farm
                let server = photos[i].server
                let secret = photos[i].secret
                let owner = photos[i].owner
                let title = photos[i].title
                let photo_url = `https://farm${farm}.staticflickr.com/${server}/${id}_${secret}.jpg`

                let a = document.createElement("A")
                a.setAttribute("href", `https://www.flickr.com/photos/${owner}/${id}`)
                a.setAttribute("target", "_blank")
                a.setAttribute("title", `${title} (Click to view on Flickr)`)
                flickr_photos.appendChild(a)

                let img = document.createElement("IMG")
                img.setAttribute("src", photo_url)

                a.appendChild(img)

                div_page_nums.style.display = null
                span_total_pages.innerText = addCommas(total_pages)
            }
        })
}

function addCommas(intNum) {
    return (intNum + '').replace(/(\d)(?=(\d{3})+$)/g, '$1,');
}

flickr_search.addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
        // Trigger the button element with a click
        flickr_search_btn.click()
    }
})


// sets sort order
flickr_sort.addEventListener("change", function() {
    flickr_photos.innerHTML = ""
    sort_order = document.querySelector('input[name="sort_radio"]:checked').value
    console.log(sort_order)
    loadFlickrPhotos()
})

// activates search based on the input value
flickr_search_btn.addEventListener("click", function() {
    flickr_photos.innerHTML = ""
    loadFlickrPhotos()
    flickr_search.select()
    btn_next.style.display = null
    span_current_page.innerText = addCommas(page_num)
})

// ensures the search input is active when clicked
flickr_search.addEventListener("click", function() {
    flickr_search.focus()
})


// this clears the main photos window when the search input is changed
flickr_search.addEventListener("change", function() {
    flickr_photos.innerHTML = ""
})

// "Next" button, goes to the next page when clicked
btn_next.addEventListener("click", function() {
    page_num += 1
    flickr_photos.innerHTML = ""
    loadFlickrPhotos()
    btn_previous.style.display = null
    span_current_page.innerText = addCommas(page_num)
})

// "Previous" button, goes to the previous page when clicked
btn_previous.addEventListener("click", function() {
    page_num -= 1
    flickr_photos.innerHTML = ""
    loadFlickrPhotos()
    if (page_num == 1) {
        btn_previous.style.display = "none"
    }
    span_current_page.innerText = addCommas(page_num)
})

// changes number of results per page when changed
div_per_page_select.addEventListener("change", function() {
    num_per_page = results.value
    flickr_photos.innerHTML = ""
    // calling the loadFlickrPhotos function triggered it twice; that's why it's not here
})


///////////////////////////

// materialize
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems, {});
})

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
});