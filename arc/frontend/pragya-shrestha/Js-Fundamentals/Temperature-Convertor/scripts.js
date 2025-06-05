const sun = document.getElementById("light-icon");
const moon = document.getElementById("dark-icon");

// sun.addEventListener("click", () => {
//   document.body.classList.remove("dark-mode");
//   sun.classList.add("toggle-icon");
//   moon.classList.remove("toggle-icon");
// });
// moon.addEventListener("click", () => {
//   document.body.classList.add("dark-mode");
//   moon.classList.add("toggle-icon");
//   sun.classList.remove("toggle-icon");
// });

const toggleTheme = () => {
  const isDark = document.body.classList.toggle("dark-mode");
  console.log(isDark);
  sun.classList.toggle("toggle-icon", isDark);
  moon.classList.toggle("toggle-icon", !isDark);
  if (isDark) {
    localStorage.setItem("theme", "dark");
  } else {
    localStorage.removeItem("theme");
  }
};

sun.addEventListener("click", toggleTheme);
moon.addEventListener("click", toggleTheme);

window.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme");
  const isDark = savedTheme === "dark";
  document.body.classList.toggle("dark-mode", isDark);
  sun.classList.toggle("toggle-icon", isDark);
  moon.classList.toggle("toggle-icon", !isDark);
});

// Dropdown functionality for temperature converter
const toggleDropdown = (containerId, dropdownId) => {
  const container = document.getElementById(containerId);
  const dropdown = document.getElementById(dropdownId);

  container.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdown.classList.toggle("visible");
  });
  dropdown.querySelectorAll("li").forEach((unit) => {
    unit.addEventListener("click", (e) => {
      const input = container.querySelector("input");
      input.value = e.target.textContent;
      dropdown.classList.remove("visible");
      e.stopPropagation();
    });
  });
};

toggleDropdown("from-unit-container", "dropdown-from");
toggleDropdown("to-unit-container", "dropdown-to");

document.getElementById("button").addEventListener("click", () => {
  const fromUnit = document.getElementById("from-unit").value;
  const toUnit = document.getElementById("to-unit").value;
  const inputValue = parseFloat(document.getElementById("temp").value);
  const result = document.getElementById("result");

  if (isNaN(inputValue)) {
    result.value = "Error: Enter valid number";
    return;
  }

  let convertedValue;

  if (fromUnit === toUnit) {
    convertedValue = inputValue;
  } else if (fromUnit === "Celsius") {
    convertedValue =
      toUnit === "Fahrenheit" ? (inputValue * 9) / 5 + 32 : inputValue + 273.15;
  } else if (fromUnit === "Fahrenheit") {
    convertedValue =
      toUnit === "Celsius"
        ? ((inputValue - 32) * 5) / 9
        : ((inputValue - 32) * 5) / 9 + 273.15;
  } else if (fromUnit === "Kelvin") {
    convertedValue =
      toUnit === "Celsius"
        ? inputValue - 273.15
        : ((inputValue - 273.15) * 9) / 5 + 32;
  }

  result.value = `${convertedValue.toFixed(2)} ${toUnit}`;
});
