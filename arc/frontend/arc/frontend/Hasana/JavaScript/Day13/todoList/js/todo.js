class addTask {
    constructor() {
        this.init();
        this.eventListener();
    }

    init() {
        this.taskInput = document.querySelector(
            ".todo__container__input>input"
        );
        this.addBtn = document.querySelector(".todo__container__addBtn");
        this.taskListContainer = document.querySelector(".todo__container");
    }
    saveTasks(tasks) {
        localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    eventListener() {
        // let tasks = [];
        let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

        this.addBtn.addEventListener("click", () => {
            if (!this.checkValidation(this.taskInput.value)) {
                alert("no task to add");
            } else {
                this.taskInput = this.addTaskToList(this.taskInput, tasks);
            }
        });

        this.taskInput.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                if (!this.checkValidation(this.taskInput.value)) {
                    alert("no task to add");
                } else {
                    this.taskInput = this.addTaskToList(this.taskInput, tasks);
                }
            }
        });

        this.renderTasks(tasks);
    }

    checkValidation(taskInput) {
        if (taskInput === "") {
            return false;
        } else {
            return true;
        }
    }

    addTaskToList(taskInput, tasks) {
        const taskText = taskInput.value.trim();

        const taskObj = {
            name: taskText,
            status: "todo",
        };

        tasks.push(taskObj);
        this.renderTasks(tasks);
        taskInput.value = "";
        this.saveTasks(tasks);

        return taskInput;
    }

    renderTasks(tasks) {
        document
            .querySelectorAll(".todo__container__task")
            .forEach((el) => el.remove());

        tasks.forEach((taskObj, index) => {
            const task = document.createElement("div");
            task.classList.add("todo__container__task");

            task.innerHTML = `
                <div class="todo__container__taskName">${taskObj.name}</div>
                        <div class="todo__container__task__status">
                            <select name="status">
                                <option value="todo" ${
                                    taskObj.status === "todo" ? "selected" : ""
                                }>To do</option>
                                <option value="inprogress" ${
                                    taskObj.status === "inprogress"
                                        ? "selected"
                                        : ""
                                }>In Progress</option>
                                <option value="completed" ${
                                    taskObj.status === "completed"
                                        ? "selected"
                                        : ""
                                }>Completed</option>
                            </select>
                        </div>
                        <div class="todo__container__task__edit">
                            <img src="../public/edit.png" alt="" />
                        </div>
                        <div class="todo__container__task__delete">
                            <img src="../public/delete.webp" alt="" />
                        </div>
            `;

            this.bindTasksActions(task, index, tasks);
            this.taskListContainer.appendChild(task);
        });
    }

    bindTasksActions(task, index, tasks) {
        const deleteBtn = task.querySelector(".todo__container__task__delete");
        const editBtn = task.querySelector(".todo__container__task__edit");
        const taskName = task.querySelector(".todo__container__taskName");
        const statusSelect = task.querySelector("select");

        // Delete task
        deleteBtn.addEventListener("click", () => {
            tasks.splice(index, 1);
            this.renderTasks(tasks);
            this.saveTasks(tasks);
        });

        // Edit task
        editBtn.addEventListener("click", () => {
            const input = document.createElement("input");
            input.type = "text";
            input.value = tasks[index].name;
            input.className = "edit-input";
            input.style.width = "100%";
            input.style.height = "100%";
            input.style.backgroundColor = "#fcbc40";

            taskName.replaceWith(input);
            input.focus();

            input.addEventListener("keydown", (e) => {
                if (e.key === "Enter") {
                    const updatedText = input.value.trim();
                    if (updatedText !== "") {
                        tasks[index].name = updatedText;
                        this.renderTasks(tasks);
                        this.saveTasks(tasks);
                    }
                }
            });
        });

        // Status change logic
        const updateStatusStyle = () => {
            const status = statusSelect.value;

            task.style.backgroundColor = "#fcbc40";
            editBtn.style.pointerEvents = "auto";
            editBtn.style.opacity = "1";

            if (status === "completed") {
                taskName.style.backgroundColor = "white";
                taskName.style.opacity = "0.5";
                task.style.backgroundColor = "grey";
                editBtn.style.pointerEvents = "none";
                editBtn.style.opacity = "0.5";
            } else if (status === "inprogress") {
                task.style.backgroundColor = "green";
            }
        };

        updateStatusStyle(); // Initial style set

        statusSelect.addEventListener("change", () => {
            tasks[index].status = statusSelect.value;
            this.saveTasks(tasks);
            updateStatusStyle();
        });
    }
}

const c1 = new addTask();
