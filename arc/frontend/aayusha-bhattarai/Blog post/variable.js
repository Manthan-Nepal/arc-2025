const themeBtns = document.querySelectorAll(".buttons > button");

themeBtns.forEach(button => {
    button.addEventListener("click", () => {
        if (button.value === "DarkMode") {
            document.documentElement.style.setProperty('--primary-color', 'black');
            document.documentElement.style.setProperty('--secondary-color', 'white');
            document.documentElement.style.setProperty('--third-color', 'white');
        } else if (button.value === "LightMode") {
            document.documentElement.style.setProperty('--primary-color', 'white');
            document.documentElement.style.setProperty('--secondary-color', 'rgb(42, 28, 47)');
            document.documentElement.style.setProperty('--third-color', 'black');
        }
    });
});
