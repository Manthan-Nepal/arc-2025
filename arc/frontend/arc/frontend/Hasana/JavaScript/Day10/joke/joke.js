const jokeBtn = document.getElementById("jokeBtn");
const jokeText = document.getElementById("jokeText");

async function fetchJoke() {
    const url = "https://icanhazdadjoke.com/";

    try {
        const response = await fetch(url, {
            headers: {
                Accept: "application/json",
            },
        });
        console.log(response)
        const data = await response.json();
        console.log(data);
        jokeText.textContent = data.joke;
    } catch (error) {
        jokeText.textContent = "Oops! Something went wrong.";
        console.error("Fetch error:", error);
    }
}

jokeBtn.addEventListener("click", fetchJoke);
