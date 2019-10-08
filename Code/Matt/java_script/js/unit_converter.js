let user_number = document.querySelector('#user_number')
let unit_input = document.querySelector('#unit_input')
let user_output = document.querySelector('#user_output')



number_button.addEventListener('click', function() {
    let number = parseFloat(user_number.value)
    let units = unit_input.value

    conversion_obj = {
        'feet': 3.28084,
        'miles': 0.000621371,
        'meters': 1,
        'kilometers': .001
    }
    converted_distance.innerText = 'your converted distance is: ' + (number*conversion_obj[units])


})
