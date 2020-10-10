const container = document.querySelector('.container');
var inputValue = document.querySelector('.input');
const add = document.querySelector('.add');

if(window.localStorage.getItem("shopList") == undefined){
     var shopList = [];
     window.localStorage.setItem("shopList", JSON.stringify(shopList));
}

var todosEX = window.localStorage.getItem("shopList");
var shopList = JSON.parse(todosEX);


class item{
	constructor(name){
		this.createItem(name);
	}
    createItem(name){
    	var itemBox = document.createElement('div');
        itemBox.classList.add('item');

    	var input = document.createElement('input');
    	input.type = "text";
    	input.disabled = true;
    	input.value = name;
    	input.classList.add('item_input');

    	var edit = document.createElement('button');
    	edit.classList.add('edit');
    	edit.innerHTML = "Edit";
    	edit.addEventListener('click', () => this.edit(input, name));

    	var remove = document.createElement('button');
    	remove.classList.add('remove');
    	remove.innerHTML = "Remove";
    	remove.addEventListener('click', () => this.remove(itemBox, name));

    	container.appendChild(itemBox);

        itemBox.appendChild(input);
        itemBox.appendChild(edit);
        itemBox.appendChild(remove);

    }

    edit(input, name){
        if(input.disabled == true){
           input.disabled = !input.disabled;
          // edit.innerHTML = "Save";
        }
    	else{
            input.disabled = !input.disabled;
           // edit.innerHTML = "Edit";
            let indexof = shopList.indexOf(name);
            shopList[indexof] = input.value;
            window.localStorage.setItem("shopList", JSON.stringify(shopList));
        }
    }

    remove(itemBox, name){
        itemBox.parentNode.removeChild(itemBox);
        let index = shopList.indexOf(name);
        todos.splice(index, 1);
        window.localStorage.setItem("shopList", JSON.stringify(shopList));
    }
}

add.addEventListener('click', check);
window.addEventListener('keydown', (e) => {
	if(e.which == 13){
		check();
	}
})

function check(){
	if(inputValue.value != ""){
		new item(inputValue.value);
        shopList.push(inputValue.value);
        window.localStorage.setItem("shopList", JSON.stringify(shopList));
		inputValue.value = "";
	}
}


for (var i = 0 ; i < shopList.length ; i++){
    new item(shopList[i]);
}


new item("Shop with us!");
