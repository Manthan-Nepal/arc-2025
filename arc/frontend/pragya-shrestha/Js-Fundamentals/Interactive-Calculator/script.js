function calculate() {
  const num1 = parseFloat(document.getElementById("num1").value);
  const num2 = parseFloat(document.getElementById("num2").value);
  const operation = document.getElementById("actionInput").value;

  let result;
  if (isNaN(num1) || isNaN(num2)) {
    result = "Error: Enter valid number";
  } else {
    switch (operation) {
      case "Add":
        result = num1 + num2;
        break;
      case "Subtract":
        result = num1 - num2;
        break;
      case "Multiply":
        result = num1 * num2;
        break;
      case "Divide":
        result = num1 / num2;
        break;
      default:
        result = "Error: Invalid Operation";
    }
  }
  if (typeof result === "string") {
    document.getElementById("result").innerHTML = result;
    document.getElementById("result").className = "error";
  } else {
    document.getElementById("result").innerHTML = `Output: ${parseFloat(
      result.toFixed(5)
    )}`;
    document.getElementById("result").className = "result";
  }
}

function show_dropdown() {
  document.getElementById("dropdown").classList.toggle("visible");
  document.getElementById("caret-down").classList.toggle("rotate");
}

function selectOperation(action, e) {
  document.getElementById("actionInput").value = action;
  show_dropdown();
  e.stopPropagation();
}
