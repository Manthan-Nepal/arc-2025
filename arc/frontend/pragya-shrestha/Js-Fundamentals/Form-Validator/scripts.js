document.getElementById("form").addEventListener("submit", (event) => {
  const name = document.getElementById("name").value;
  const contact = document.getElementById("contact").value;
  const email = document.getElementById("email").value;
  const address = document.getElementById("address").value;
  const gender = document.querySelector('input[name="gender"]:checked')?.value;

  const error = [];

  if (!name || name.length < 2) {
    error.push("Name must be more than 2 characters.");
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email) {
    error.push("Email is required.");
  }
  if (email && !emailRegex.test(email)) {
    error.push("Invalid email");
  }

  const contactRegex = /^\d{10}$/;
  if (!contact) {
    error.push("Contact No. is required.");
  }
  if (contact && !contactRegex.test(contact)) {
    error.push("Invalid contact details");
  }

  if (!gender) {
    error.push("Please select any gender.");
  }
  if (!address) {
    error.push("Address cannot be empty.");
  }
  const output = document.getElementById("result");

  if (error.length > 0) {
    result.innerHTML = error
      .map((err) => `<p class="err-txt">${err}</p>`)
      .join("");
  } else {
    output.textContent = "Form submitted!";
    console.log("Name:", name);
    console.log("Contact:", contact);
    console.log("Email:", email);
    console.log("Address:", address);
    console.log("Gender:", gender);
  }
  event.preventDefault();
});
