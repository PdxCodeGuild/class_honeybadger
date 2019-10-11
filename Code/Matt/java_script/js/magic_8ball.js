
function random_item(choices_list)
{

return choices_list[Math.floor(Math.random()*choices_list.length)];

}

var choices_list = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","no","negative ghostrider",]
var random_choice = choices_list[Math.floor(Math.random()*choices_list.length)];
alert(random_choice)
console.log(random_item(choices_list));
