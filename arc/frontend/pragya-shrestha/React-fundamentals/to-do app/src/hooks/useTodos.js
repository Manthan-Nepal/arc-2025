import { useEffect, useState } from "react";
import { v4 as uuidv4 } from "uuid";

export function useTodos() {
  const [todos, setTodos] = useState(() => {
    try {
      const savedTodos = localStorage.getItem("todos");
      return savedTodos ? JSON.parse(savedTodos) : [];
    } catch (err) {
      console.error("Error parsing todos from localStorage", err);
      return [];
    }
  });

  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);

  // cross tab sync
  useEffect(() => {
    function syncTodos(event) {
      if (event.key === "todos") {
        try {
          const newTodos = event.newValue ? JSON.parse(event.newValue) : [];
          setTodos(newTodos);
        } catch (error) {
          console.error("Failed to parse from storage event:", error);
        }
      }
    }

    window.addEventListener("storage", syncTodos);
    return () => {
      window.removeEventListener("storage", syncTodos);
    };
  }, []);

  const addTodo = (todo) => {
    setTodos([
      ...todos,
      { id: uuidv4(), task: todo, isEditing: false, isCompleted: false },
    ]);
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter((todo) => todo.id !== id));
  };

  const editTodo = (id) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id ? { ...todo, isEditing: !todo.isEditing } : todo
      )
    );
  };

  const completedTask = (id) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id ? { ...todo, isCompleted: !todo.isCompleted } : todo
      )
    );
  };

  const editTask = (id, task) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id ? { ...todo, task, isEditing: false } : todo
      )
    );
  };
  return {
    todos,
    addTodo,
    deleteTodo,
    editTodo,
    completedTask,
    editTask,
  };
}
