const input = document.querySelector("input");
const searchIcon = document.querySelector(".container__search__image img");
const placeName = document.querySelector(".container__weatherInfo__placeName");
const temp = document.querySelector(".container__weatherInfo__temperature");
const weatherIcon = document.querySelector(".container__weatherInfo__icon img");
const body = document.querySelector("body");

// const API_KEY =

async function fetchWeather(city) {
    try {
        const res = await fetch(`https://wttr.in/${city}?format=j1`);
        if (!res.ok) throw new Error("City not found");
        const data = await res.json();

        placeName.textContent = city.toUpperCase();
        temp.textContent = `${data.current_condition[0].temp_C} °C`;
        const description =
            data.current_condition[0].weatherDesc[0].value.toLowerCase();

        if (description.includes("sun")) {
            weatherIcon.src = "../public/sunny.png"; // use a default weather icon or update based on condition
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
        void weatherIcon.offsetWidth; // restart animation trick
        weatherIcon.classList.add("bounce");

        // Change background based on time
        const hour = new Date().getHours();
        console.log({hour})
        // hour = hour + 12;
        console.log("here");

        let bgColor = "#2C3E50"; // default night
        if (hour >= 6 && hour < 12) {
            bgColor = "#FFFACD"; // Morning
        } else if (hour >= 12 && hour < 18) {
            bgColor = "#87CEEB"; // Afternoon
        } else if (hour >= 18 && hour < 20) {
            bgColor = "#FFD700"; // Evening
        }
        console.log("Background color set to:", bgColor);
        // Animate background color (fade)
        body.style.transition = "background-color 1s ease-in-out";
        body.style.backgroundColor = bgColor;
        // input.value="";
    } catch (error) {
        placeName.textContent = "Not Found";
        temp.textContent = "--";
        weatherIcon.src = "../public/blocked.png";
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
