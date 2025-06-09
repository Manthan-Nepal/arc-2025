function addItem() {
  const inputField = document.getElementById("item-input");
  const itemText = inputField.value.trim();
  if (itemText === "") {
    document.getElementById("error").textContent = "Please enter a valid item.";

    return;
  }
  document.getElementById("error").textContent = "";
  const listItem = document.createElement("li");
  listItem.innerHTML = `
    <span class="task-text">${itemText}</span>
    <i class="fa-solid fa-xmark"></i>
  `;
  document.getElementById("item-list").appendChild(listItem);
  localStorage.setItem(
    "item-list",
    document.getElementById("item-list").innerHTML
  );
  inputField.value = "";
}

const saveList = () => {
  localStorage.setItem(
    "item-list",
    document.getElementById("item-list").innerHTML
  );
};

const renderList = (html) => {
  document.getElementById("item-list").innerHTML = html;
};

const loadList = () => {
  const saved = localStorage.getItem("item-list");
  if (saved) renderList(saved);
};

document.getElementById("add-button").addEventListener("click", (e) => {
  e.preventDefault();
  addItem();
});

document.getElementById("item-input").addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    addItem();
  }
});

//Mark task as completed or remove it
document.getElementById("item-list").addEventListener("click", (e) => {
  if (e.target.classList.contains("fa-xmark")) {
    e.target.parentElement.remove();
  } else if (
    e.target.classList.contains("task-text") ||
    e.target.tagName === "LI"
  ) {
    const li = e.target.closest("li");
    if (li) {
      li.classList.toggle("checked");
    }
  }
  saveList();
});

// Load saved list from localStorage on page load
window.addEventListener("DOMContentLoaded", () => {
  loadList();
});
