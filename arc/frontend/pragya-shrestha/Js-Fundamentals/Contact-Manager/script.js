const contactForm = document.getElementById("contact-form");
const contactList = document.getElementById("contact-list");
const searchInput = document.getElementById("search");
const filterGroup = document.getElementById("filter-group");
const sortSelect = document.getElementById("sort");

let contacts = [];

contactForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const contact = {
    name: document.getElementById("name").value.trim(),
    email: document.getElementById("email").value.trim(),
    phone: document.getElementById("phone").value.trim(),
    group: document.getElementById("group").value,
  };

  contacts.push(contact);
  contactForm.reset();
  renderContacts();
});

function renderContacts() {
  const searchTerm = searchInput.value.toLowerCase();
  console.log(`search:${searchTerm}`);
  const groupFilter = filterGroup.value;
  const sortOrder = sortSelect.value;

  let filtered = contacts.filter(
    (c) =>
      c.name.toLowerCase().includes(searchTerm) &&
      (groupFilter === "" || c.group === groupFilter)
  );

  filtered.sort((a, b) => {
    if (sortOrder === "az") return a.name.localeCompare(b.name);
    if (sortOrder === "za") return b.name.localeCompare(a.name);
    return 0;
  });

  contactList.innerHTML = "";

  if (filtered.length === 0) {
    contactList.innerHTML = "<li>No contacts found.</li>";
    return;
  }

  filtered.forEach((c) => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${c.name}</strong><br>
      <i class="fa-solid fa-envelope"></i> ${c.email}<br>
      <i class="fa-solid fa-phone"></i> ${c.phone}<br>
      <i class="fa-solid fa-user-group"></i> ${c.group}`;
    contactList.appendChild(li);
  });
}

searchInput.addEventListener("input", renderContacts);
filterGroup.addEventListener("change", renderContacts);
sortSelect.addEventListener("change", renderContacts);
