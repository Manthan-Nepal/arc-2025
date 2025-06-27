// const celsiusInput = document.getElementById("celsius").value;
// const fahrenheitInput = document.getElementById("farenheit").value;
// const kelvinInput = document.getElementById("kelvin").value;

// const inputs = document.getElementsByClassName("input");


// for (let i = 0; i < inputs.length; i++) {
//     let input = input[i];
    
// }

document.querySelector(".button").addEventListener("click", function () {
    // Get the input values as strings
    let c = document.getElementById("celsius").value;
    let f = document.getElementById("fahrenheit").value;
    let k = document.getElementById("kelvin").value;

    // Convert to numbers
    c = parseFloat(c);
    f = parseFloat(f);
    k = parseFloat(k);

    // If Celsius is entered
    if (!isNaN(c)) {
        document.getElementById("fahrenheit").value = (c * 9/5 + 32).toFixed(2);
        document.getElementById("kelvin").value = (c + 273.15).toFixed(2);
    }
    // If Fahrenheit is entered
    else if (!isNaN(f)) {
        document.getElementById("celsius").value = ((f - 32) * 5/9).toFixed(2);
        document.getElementById("kelvin").value = ((f - 32) * 5/9 + 273.15).toFixed(2);
    }
    // If Kelvin is entered
    else if (!isNaN(k)) {
        document.getElementById("celsius").value = (k - 273.15).toFixed(2);
        document.getElementById("fahrenheit").value = ((k - 273.15) * 9/5 + 32)/toFixed(2);
    }
    // If nothing valid is entered
    else {
        alert("Please enter a number in one field.");
    }
});
