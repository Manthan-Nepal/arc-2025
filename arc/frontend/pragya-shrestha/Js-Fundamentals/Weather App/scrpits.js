const apiKey = "a95311627d004375bc013712250906";
const apiUrl = `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=`;
const searchBox = document.querySelector(".search input");
const searchBtn = document.querySelector(".search button");
const weatherIcon = document.querySelector(".weather-icon");

async function checkWeather(city) {
  if (!city) {
    document.querySelector(".error").innerHTML = "Please enter a city name";
    return;
  }

  try {
    const response = await fetch(apiUrl + city);
    if (!response.ok) throw new Error("City not found");
    const data = await response.json();
    console.log(data);

    document.querySelector(".error").innerHTML = "";
    document.querySelector(".city").innerHTML = data.location.name;
    document.querySelector(".temp").innerHTML =
      Math.round(data.current.temp_c) + "°C";
    document.querySelector(".wind").innerHTML = data.current.wind_kph + " Km/h";
    document.querySelector(".humidity").innerHTML = data.current.humidity + "%";

    if (weatherIcon) {
      weatherIcon.src = data.current.condition.icon;
      weatherIcon.alt = data.current.condition.text;
    }
  } catch (error) {
    document.querySelector(".error").innerHTML = error;
    searchBox.value = "";
  }
}

searchBtn.addEventListener("click", () => {
  checkWeather(searchBox.value.trim());
});

checkWeather("Kathmandu");
