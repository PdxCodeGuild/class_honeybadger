let count = 0;
let bt_add = document.querySelector('#bt_add')
      bt_add.addEventListener('click', function() {
        let ul = document.getElementById("todo_list")
        let item = document.getElementById("item")
        let li = document.createElement("li")
        li.id="liId"+count.toString()
        li.innerText = item.value
        let bt = document.createElement('button')
        bt.innerText = 'remove'
        bt.id="btId"+count.toString()
      })

        bt.addEventListener('click', function() {
          document.querySelector("#liId"+bt.id[bt.id.length-1]).remove()
        })

        let bt_remove = document.querySelector('#bt_remove')

        bt_remove.addEventListener('click', function() {
        	count--;
          li.remove()
        })

        li.appendChild(bt)
        ul.appendChild(li)
				count++;
      })
