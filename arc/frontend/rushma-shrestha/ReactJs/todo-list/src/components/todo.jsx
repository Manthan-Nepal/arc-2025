import React, { useState } from 'react'
import './todo.css'
import Toast from './toast';

export default function Todo() {  
    // toast box
    const errorMsg = `<p><i class="error fa-solid fa-circle-exclamation"></i> Empty tasks cannot be added</p>`;
    const successMsg = `<p><i class="success fa-solid fa-circle-check"></i> Task Added Successfully</p>`;
    const taskComplete = `<p><i class="info fa-solid fa-circle-info"></i> Task completed</p>`;
    const taskUncomplete = `<p><i class="info fa-solid fa-circle-info"></i> Task incomplete</p>`;
    const taskDeleted = `<p><i class="delete fa-solid fa-trash"></i> Task Deleted</p>`;

    const [tasks, setTasks]=useState([]);
    const [newTask, setNewTask]= useState("");
    const[toasts,setToasts]= useState([]);
    
    function showToast(message){
        const id=Date.now();//for unique id
        setToasts(prev=>[...prev,{id,message}])
        setTimeout(() => {
            removeToast(id);
        }, 3000);;
    }

    function removeToast(id) {
    setToasts(prev => prev.filter(t => t.id !== id));
    }
    // handle change
    function handleChange(event){
        setNewTask(event.target.value);
    }

    // arrow function for adding new task
    const addTask=()=>{
       if (newTask.trim()!=="") {
        setTasks(t=>[...t,newTask]);
        setNewTask("");
        showToast(successMsg);
       }else{
        showToast(errorMsg);
       }
    }
    const deleteTask=(index)=>{
        const updatedTasks= tasks.filter((_,i)=>i!==index);
        setTasks(updatedTasks);
        showToast(taskDeleted);
    }


return (    

    <>
    <header>
        <h1>To-do List</h1>
    </header>
    <section class="todo-container">
    <input id="input-box" type="text" value={newTask} onChange={handleChange} />
        <button id="btn" onClick={addTask}>+</button>
        <ul id="task-container">
            {tasks.map((task,index)=>
            <li  key={index}> 
                {task}
                <span onClick={()=>deleteTask(index)}>&times;</span>
            </li>
            )} 
        </ul>
    </section>
    <div id="toastBox">
        {toasts.map(toast=>(<Toast key={toast.id} message={toast.message} onClose={() => removeToast(toast.id)}/>))}</div></>
  )
}

