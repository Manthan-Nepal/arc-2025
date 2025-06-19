import { useState } from "react";

export default function TodoForm({ addTodo }) {
  const [value, setValue] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (value.trim()) {
      addTodo(value);
      setValue("");
      setError("");
    } else {
      setError("Please enter a task");
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
          placeholder="Add task"
          value={value}
          onChange={handleChange}
          className="todo-input"
        />
        <button type="submit" className="todo-btn">Add Task</button>
      </form>
      {error && <p className="error">{error}</p>}
    </>
  );
}
