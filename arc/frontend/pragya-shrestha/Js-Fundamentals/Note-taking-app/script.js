const notesContainer = document.getElementById("notesContainer");
const addBtn = document.querySelector(".add-btn");

const sampleColors = ["#fde293", "#ffb3ab", "#c2f68d", "#decaff", "#a3f6f3"];
const sampleTitles = [
  "The beginning of screenless design: UI jobs to be taken over",
  "13 Things You Should Give Up If You Want To Be a Successful UX Designer",
  "The Psychology Principles Every UI/UX Designer Needs to Know",
  "10 UI & UX Lessons from Designing My Own Product",
  "52 Research Terms you need to know as a UX Designer",
  "Text fields & Form design — UI components",
];

function createNote(title, color) {
  const note = document.createElement("div");
  note.className = "note";
  note.style.background = color;

  note.innerHTML = `
    <h3>${title}</h3>
    <small>${new Date().toDateString()}</small>
    <button class="icon-btn top-right">★</button>
    <button class="icon-btn bottom-right">⭮</button>
  `;

  note.querySelector(".bottom-right").addEventListener("click", () => {
    note.remove();
  });

  notesContainer.appendChild(note);
}

// Initial notes
for (let i = 0; i < sampleTitles.length; i++) {
  createNote(sampleTitles[i], sampleColors[i % sampleColors.length]);
}

// Add new note
addBtn.addEventListener("click", () => {
  const title = prompt("Enter note title:");
  if (title) {
    const color = sampleColors[Math.floor(Math.random() * sampleColors.length)];
    createNote(title, color);
  }
});
