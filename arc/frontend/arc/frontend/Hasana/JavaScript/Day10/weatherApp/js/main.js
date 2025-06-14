const input = document.querySelector("input");
const searchIcon = document.querySelector(".container__search__image img");
const placeName = document.querySelector(".container__weatherInfo__placeName");
const temp = document.querySelector(".container__weatherInfo__temperature");
const weatherIcon = document.querySelector(".container__weatherInfo__icon img");
const body = document.querySelector("body");

async function fetchWeather(city) {
    const loaderContainer = document.getElementById("weatherLoader");
    loaderContainer.innerHTML = `<div class="loader"><div class="spinner"></div></div>`;

    try {
        const res = await fetch(`https://wttr.in/${city}?format=j1`);
        if (!res.ok) throw new Error("City not found");
        const data = await res.json();

        placeName.textContent = city.toUpperCase();
        temp.textContent = `${data.current_condition[0].temp_C} °C`;
        const description =
            data.current_condition[0].weatherDesc[0].value.toLowerCase();

        if (description.includes("sun")) {
            weatherIcon.src = "../public/sunny.png";
        } else if (description.includes("cloud")) {
            weatherIcon.src = "../public/cloudy.png";
        } else if (description.includes("rain")) {
            weatherIcon.src = "../public/rain.webp";
        } else if (description.includes("wind")) {
            weatherIcon.src = "../public/blocked.png";
        } else {
            weatherIcon.src = "../public/blocked.png";
        }

        // Animate icon (bounce)
        weatherIcon.classList.remove("bounce");
        void weatherIcon.offsetWidth;
        weatherIcon.classList.add("bounce");

        // Background update
        const hour = new Date().getHours();
        let bgColor = "#2C3E50";
        if (hour >= 6 && hour < 12) {
            bgColor = "#FFFACD"; // Morning
        } else if (hour >= 12 && hour < 18) {
            bgColor = "#87CEEB"; // Afternoon
        } else if (hour >= 18 && hour < 20) {
            bgColor = "#FFD700"; // Evening
        }
        body.style.transition = "background-color 1s ease-in-out";
        body.style.backgroundColor = bgColor;

        loaderContainer.innerHTML = "";

    } catch (error) {
        placeName.textContent = "Not Found";
        temp.textContent = "--";
        weatherIcon.src = "../public/blocked.png";
        loaderContainer.innerHTML = "";
    }
}

input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        const city = input.value.trim();
        if (city) fetchWeather(city);
    }
});

searchIcon.addEventListener("click", () => {
    const city = input.value.trim();
    if (city) fetchWeather(city);
});

window.addEventListener("load", () => {
    fetchWeather("Kathmandu");
});
