const form = document.querySelector('form');
const displaySection = document.querySelector('.displayContact');
const searchInput = document.getElementById('searchIn');

let contacts = JSON.parse(localStorage.getItem("contacts")) || [];

// Get selected gender
function getGender() {
  const genderInputs = document.getElementsByName('gender');
  for (let radio of genderInputs) {
    if (radio.checked) {
      return radio.value;
    }
  }
  return "";
}

function renderContacts(filter = "") {
  const filteredContacts = contacts.filter(contact =>
    contact.name &&
    contact.name.toLowerCase().includes(filter.toLowerCase())
  );

  let html = `
    <div style="margin-top: 20px;">
      <h3 style="text-align:center;">Saved Contacts</h3>
      <table border="1" cellpadding="8" cellspacing="0" style="width:100%;">
        <thead>
          <tr>
            <th>#</th>
            <th>Full Name</th>
            <th>Gender</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Address</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          ${
            filteredContacts.length === 0
              ? `<tr><td colspan="7" style="text-align:center;">No contacts found.</td></tr>`
              : filteredContacts
                  .map((c, index) => `
                    <tr>
                      <td>${index + 1}</td>
                      <td>${c.name}</td>
                      <td>${c.gender}</td>
                      <td>${c.email}</td>
                      <td>${c.contact}</td>
                      <td>${c.address}</td>
                      <td><button onclick="deleteContact(${index})">Delete</button></td>
                    </tr>
                  `)
                  .join("")
          }
        </tbody>
      </table>
    </div>`;

  displaySection.innerHTML = document.querySelector(".search").outerHTML + html;
}

// Add contact
form.addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById("fname").value.trim();
  const email = document.getElementById("email").value.trim();
  const contact = document.getElementById("contact").value.trim();
  const address = document.getElementById("address").value.trim();
  const gender = getGender();

  if (!name || !email || !contact || !address || !gender) {
    alert("Please fill all fields.");
    return;
  }

  const newContact = {
    name,
    gender,
    email,
    contact,
    address,
  };

  contacts.push(newContact);
  localStorage.setItem("contacts", JSON.stringify(contacts));
  form.reset();
  renderContacts();
});

renderContacts();
