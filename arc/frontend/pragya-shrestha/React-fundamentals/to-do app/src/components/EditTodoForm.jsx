import { useState } from "react";

export default function EditTodoForm({ todo, editTask }) {
  const [value, setValue] = useState(todo.task);
  const handleSubmit = (e) => {
    e.preventDefault();
    if (value.trim()) {
      editTask(todo.id, value);
      setValue("");
    }
  };
  const handleChange = (e) => {
    setValue(e.target.value);
  };
  return (
    <>
      <form onSubmit={handleSubmit} className="TodoForm">
        <input
          type="text"
          placeholder="Update task"
          value={value}
          onChange={handleChange}
          className="todo-input"
        />
        <button type="submit" className="todo-btn">
          Update Task
        </button>
      </form>
    </>
  );
}
