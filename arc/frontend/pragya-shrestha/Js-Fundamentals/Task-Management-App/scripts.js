let isEditing = false;
let currentEditingCard = null;

const modal = document.querySelector(".add-modal");
const form = document.querySelector(".add-modal__form");
const submitBtn = document.getElementById("modal-submit-btn");
const modalTitle = document.getElementById("modal-title");

function openAddTaskModal() {
  modal.classList.add("open");
}

function closeAddModal() {
  modal.classList.remove("open");
  form.reset();
  modalTitle.textContent = "Add New Task";
  submitBtn.textContent = "Add Task";
  isEditing = false;
  currentEditingCard = null;
}

function createTaskCard(
  title,
  description,
  priority,
  className,
  formattedDate,
  rawDate
) {
  const priorityValue = { H: 3, M: 2, L: 1 }[priority];
  const taskCard = document.createElement("div");
  taskCard.classList.add("task");
  taskCard.setAttribute("draggable", "true");
  taskCard.setAttribute("data-priority", priorityValue);
  taskCard.innerHTML = `
    <div class="task__tags">
      <span class="task__tag task__tag--copyright">${title}</span>
      <div class="icon">
        <i class="fa-solid fa-pencil"></i>
        <i class="fa-solid fa-trash"></i>
      </div>
    </div>
    <p>${description}</p>
    <div class="task__stats">
      <span><time datetime="${rawDate}"><i class="fas fa-flag"></i>${formattedDate}</time></span>
      <span class="task__priority ${className}">${priority}</span>
    </div>
  `;
  return taskCard;
}

function getPriorityClass(priority) {
  switch (priority) {
    case "H":
      return "high-priority";
    case "M":
      return "medium-priority";
    default:
      return "low-priority";
  }
}
function sortTasksInColumnsByPriority() {
  const columns = document.querySelectorAll(".project-column");

  columns.forEach((column) => {
    const tasks = Array.from(column.querySelectorAll(".task"));

    const sortedTasks = tasks.sort((a, b) => {
      const priorityA = parseInt(a.dataset.priority);
      const priorityB = parseInt(b.dataset.priority);
      return priorityB - priorityA;
    });

    sortedTasks.forEach((task) => column.appendChild(task));
  });
}

document.querySelector(".add-task").addEventListener("click", openAddTaskModal);

document.querySelector(".add-modal__submit").addEventListener("click", (e) => {
  e.preventDefault();

  const title = document.getElementById("task-title").value.trim();
  const description = document.getElementById("task-description").value.trim();
  const priority = document.getElementById("task-priority").value;
  const dueDateInput = document.getElementById("task-date").value;

  if (!title || !dueDateInput) {
    alert("Please fill in all required fields.");
    return;
  }

  const currentDate = new Date();
  currentDate.setHours(0, 0, 0, 0);
  const dueDate = new Date(dueDateInput + "T00:00:00");

  if (dueDate < currentDate) {
    alert("Due date cannot be in the past.");
    return;
  }

  const formattedDate = dueDate.toLocaleDateString("en-US", {
    month: "short",
    day: "numeric",
  });
  const rawDate = dueDateInput;
  const className = getPriorityClass(priority);

  if (isEditing && currentEditingCard) {
    currentEditingCard.querySelector(".task__tag").textContent = title;
    currentEditingCard.querySelector("p").textContent = description;
    const timeElem = currentEditingCard.querySelector("time");
    timeElem.innerHTML = `<i class='fas fa-flag'></i>${formattedDate}`;
    timeElem.setAttribute("datetime", rawDate);

    const priorityElem = currentEditingCard.querySelector(".task__priority");
    priorityElem.textContent = priority;
    priorityElem.className = `task__priority ${className}`;

    const priorityValue = { H: 3, M: 2, L: 1 }[priority];
    currentEditingCard.setAttribute("data-priority", priorityValue);
    sortTasksInColumnsByPriority();
  } else {
    const taskCard = createTaskCard(
      title,
      description,
      priority,
      className,
      formattedDate,
      rawDate
    );
    document.querySelector(".column-todo").appendChild(taskCard);
    sortTasksInColumnsByPriority();
  }

  closeAddModal();
  saveTasksToStorage();
});

document.addEventListener("click", (e) => {
  if (e.target.classList.contains("fa-pencil")) {
    const taskCard = e.target.closest(".task");
    document.getElementById("task-title").value =
      taskCard.querySelector(".task__tag").textContent;
    document.getElementById("task-description").value =
      taskCard.querySelector("p").textContent;
    document.getElementById("task-priority").value = taskCard
      .querySelector(".task__priority")
      .textContent.charAt(0);
    document.getElementById("task-date").value = taskCard
      .querySelector("time")
      .getAttribute("datetime");
    modalTitle.textContent = "Edit Task";
    submitBtn.textContent = "Update Task";
    isEditing = true;
    currentEditingCard = taskCard;
    openAddTaskModal();
  } else if (e.target.classList.contains("fa-trash")) {
    e.target.closest(".task").remove();
    saveTasksToStorage();
  }
});

document
  .querySelector(".add-modal__close")
  .addEventListener("click", closeAddModal);

document.addEventListener("dragstart", (e) => {
  if (e.target.classList.contains("task")) {
    e.target.classList.add("dragging");
  }
});

document.addEventListener("dragend", (e) => {
  if (e.target.classList.contains("task")) {
    e.target.classList.remove("dragging");
    saveTasksToStorage();
    sortTasksInColumnsByPriority();
  }
});

document.querySelectorAll(".project-column").forEach((column) => {
  column.addEventListener("dragover", (e) => {
    e.preventDefault();
    const dragging = document.querySelector(".dragging");
    const afterEl = getAfterElement(column, e.clientY);
    if (!afterEl) {
      column.appendChild(dragging);
    } else {
      column.insertBefore(dragging, afterEl);
    }
  });
});

function getAfterElement(container, y) {
  return [...container.querySelectorAll(".task:not(.dragging)")].reduce(
    (closest, child) => {
      const box = child.getBoundingClientRect();
      const offset = y - box.top - box.height / 2;
      return offset < 0 && offset > closest.offset
        ? { offset, element: child }
        : closest;
    },
    { offset: Number.NEGATIVE_INFINITY, element: null }
  ).element;
}

function saveTasksToStorage() {
  const tasks = [];
  document.querySelectorAll(".task").forEach((task) => {
    const rawDate = task.querySelector("time").getAttribute("datetime");

    // Safely format the date again from the raw value
    const formattedDate = new Date(rawDate).toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
    });
    const column = task.closest(".project-column");
    const columnId = column ? column.id : "to-do";
    tasks.push({
      title: task.querySelector(".task__tag").textContent,
      description: task.querySelector("p").textContent,
      priority: task.querySelector(".task__priority").textContent,
      rawDate,
      formattedDate,
      columnId,
    });
  });
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasksFromStorage() {
  const columns = document.querySelectorAll(".project-column");
  columns.forEach((column) => {
    column.querySelectorAll(".task").forEach((task) => task.remove());
  });
  const savedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
  savedTasks.forEach(
    ({ title, description, priority, rawDate, formattedDate, columnId }) => {
      const className = getPriorityClass(priority);
      const taskCard = createTaskCard(
        title,
        description,
        priority,
        className,
        formattedDate,
        rawDate
      );
      const column =
        document.getElementById(columnId) || document.getElementById("to-do");
      column.appendChild(taskCard);
    }
  );
  sortTasksInColumnsByPriority();
}

loadTasksFromStorage();

window.addEventListener("storage", (event) => {
  if (event.key === "tasks") {
    loadTasksFromStorage();
  }
});
