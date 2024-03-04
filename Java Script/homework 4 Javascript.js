function delete_item(ToDoItem){
    var del=document.createElement("button");
    del.textContent ="X";
    del.className="px-1 border-2 border-solid text-red bg-red-500";
    del.onclick = function() {
        ToDoItem.parentElement.removeChild(ToDoItem)
    }
    ToDoItem.appendChild(del);
}

function duplicates(ToDoList, inputToDo){
    var childElement = ToDoList.children;
    var childArray=Array.from(childElement);

    for(var i=0;i<childArray.length;i++){
        var ToDoItem=childArray[i];
        
        if(ToDoItem.textContent.trim() === inputToDo.value.trim()+"X"){
            return true;
        }
    }
    return false;
}

function addToDo() {
    var inputToDo = document.getElementById("inputToDo");
    var ToDoList = document.getElementById("ToDoList");

    if (inputToDo.value.trim().length>255){
        alert("That is too much to do at once")
        return;
    }else if(duplicates(ToDoList, inputToDo)){
        alert("This is already on the list");
        return;
    }else if(inputToDo.value.trim() == ""){
        alert("You need to type something");
        return;
    } else if (inputToDo.value.trim()!=""){
        var ToDo_Item = document.createElement("li");
        // ToDo_Item.id="ToDo_Item";
        ToDo_Item.textContent= inputToDo.value;
        ToDo_Item.onclick = function(){
            ToDo_Item.classList.toggle("line-through");
        };
        ToDoList.appendChild(ToDo_Item);
        delete_item(ToDo_Item);
    }
    if (ToDoList.children.length<2){
        var Fred = document.createElement("li");
        Fred.textContent = "Find FRED";
        Fred.id="FRED";
        ToDoList.appendChild(Fred);
        delete_item(Fred);
    }

    inputToDo.value="";
}

function FRED(){
    var fred = document.getElementById("FRED");
    fred.className="line-through";
    alert("nice")
}