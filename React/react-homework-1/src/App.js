import './App.css';
import {useState} from "react";


function App() {
  const [inputItem, setInputItem] = useState("")
  const [todo, setTodo]= useState([])
  const completeTaskCount = todo.filter(task => task.completed === true).length
  const remainingTaskCount = todo.filter(task => task.completed === false).length

  function handleSubmit(e){
    e.preventDefault()

    if (inputItem !== "" && inputItem.length <255 && todo.filter(task => task.title === inputItem).length < 1){
      setTodo((currentTodo) => {
        return [...currentTodo, { id:crypto.randomUUID(), title: inputItem, completed: false, taskTail: "pl-2 pb-2 hover:line-through"},]})
        setInputItem("")
    } else {
      alert("There is something wrong with this task: Too short, Too long or already existing" + {inputItem})
    }
  }
  console.log(todo)

  function deleteTask(taskID){
    setTodo(currentTodo => {
      return currentTodo.filter(tasks => tasks.id !== taskID)
    })
  }

  function CrossOut(taskID) {
    setTodo((currentTodo) => {
      return currentTodo.map((task) => {
        if (task.taskTail === "pl-2 pb-2 hover:line-through"){
           return task.id === taskID ? { ...task, completed: true, taskTail: "pl-2 pb-2 line-through" } : task
        }else{
          return task.id === taskID ? { ...task, completed: false, taskTail: "pl-2 pb-2 hover:line-through" } : task
        }  
      })})
  }

  return (
    <form onSubmit={handleSubmit} className="min-w-screen min-h-screen bg-topleft bg-no-repeat bg-auto bg-[url(https://i.ebayimg.com/images/g/eg0AAOSwqytijTn8/s-l1200.webp)]"
          >
      <h1 className="absolute left-24 top-16 outline-black text-black text-xl underline">
        To do List
      </h1>
      <h2 className="absolute left-64 pl-96 top-8 text-xl">Completed:{completeTaskCount}</h2>
      <h2 className="absolute left-64 pl-96 top-16 text-xl">Remaining:{remainingTaskCount}</h2>
      <p className="absolute left-24 top-32 pr-20 text-xl">
        I have <input type="text" 
                      placeholder=" Type your task"
                      className="border-b-2 border-black"
                      value={inputItem}
                      onChange={(e) =>{setInputItem(e.target.value)}}
                      ></input>
        to do: <button type="submit" 
                      className="px-1 border-2 border-black"
                      >Add</button>
      </p>
      <ul className="space-y-6 absolute left-24 top-44 text-xl">
        {todo.map((tasks)=> (
          <li key ={tasks.id}>
            <button type="button"
                    className="px-2 border-2 border-rose-400 bg-rose-100" 
                    onClick={() => deleteTask(tasks.id)}>X</button>
            <button type="button" 
                    onClick={() => CrossOut(tasks.id)} 
                    className={tasks.taskTail}>{tasks.title}</button>
          </li>
        ))
      }
      </ul>

    </form>
  );
}

export default App;
