import { useTodos } from "../hooks/useTodos";
import EditTodoForm from "./EditTodoForm";
import Todo from "./Todo";
import TodoForm from "./TodoForm";

export default function TodoWrapper() {
  const { todos, addTodo, deleteTodo, editTodo, completedTask, editTask } =
    useTodos();

  return (
    <div className="TodoWrapper">
      <h1>Path Plan</h1>
      <TodoForm addTodo={addTodo} />
      {todos.map((todo) =>
        todo.isEditing ? (
          <EditTodoForm key={todo.id} todo={todo} editTask={editTask} />
        ) : (
          <Todo
            key={todo.id}
            todo={todo}
            deleteTodo={deleteTodo}
            editTodo={editTodo}
            completedTask={completedTask}
          />
        )
      )}
    </div>
  );
}
