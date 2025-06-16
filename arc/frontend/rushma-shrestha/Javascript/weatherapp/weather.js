async function getWeather() {
  const apiKey = "2bea82c08d9243993f7b6dcd05c2da29";  // Replace with your OpenWeatherMap API key
  const city = document.getElementById("cityInput").value;
  const result = document.getElementById("result");

  if (!city) {
    result.innerHTML = "Please enter a city name.";
    return;
  }

  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(url);
    const data = await response.json();

    if (data.cod === "404") {
      result.innerHTML = "City not found.";
    } else {
      result.innerHTML = `
        <h3>${data.name}, ${data.sys.country}</h3>
        <p>Temperature: ${data.main.temp} °C</p>
        <p>Weather: ${data.weather[0].description}</p>
      `;
    }
  } catch (error) {
    result.innerHTML = "Error fetching data.";
  }
}
