import { faPenToSquare, faTrash } from '@fortawesome/free-solid-svg-icons';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
export default function Todo({todo, deleteTodo,editTodo,completedTask}) {
  return (
    <div className="Todo">
      <p className={`${todo.isCompleted ? "completed":"incompleted"}`} onClick={()=>completedTask(todo.id)}>{todo.task}</p>
      <div>
        <FontAwesomeIcon className="edit-icon" icon={faPenToSquare} onClick={()=>editTodo(todo.id)} />

        <FontAwesomeIcon className="delete-icon" icon={faTrash} onClick={()=>deleteTodo(todo.id)}/>
      </div>
    </div>
  );
}
