class NewsAggregator {
    constructor() {
        this.init();
        this.EventHandler();
        this.loadPreviousSearch();
    }

    init() {
        this.input = document.querySelector("input");
        this.searchIcon = document.querySelector(
            ".container__search__image img"
        );
        this.newsList = document.getElementById("newsList");
    }

    EventHandler() {
        this.input.addEventListener("keypress", (e) => {
            if (e.key === "Enter") {
                const searchValue = this.input.value.trim();
                if (searchValue) {
                    this.fetchNews(searchValue);
                    this.saveToLocalStorage(searchValue);
                }
            }
        });

        this.searchIcon.addEventListener("click", () => {
            const searchValue = this.input.value.trim();
            if (searchValue) {
                this.fetchNews(searchValue);
                this.saveToLocalStorage(searchValue);
            }
        });
    }
    saveToLocalStorage(searchValue) {
        localStorage.setItem("lastSearch", searchValue);
    }

    loadPreviousSearch() {
        const lastSearch = localStorage.getItem("lastSearch");
        if (lastSearch) {
            this.input.value = lastSearch;
            this.fetchNews(lastSearch);
        }
    }

    async fetchNews(searchValue) {
        const API_NEWSAPI = "pub_a4e9d5329f5642b9bd0e9e1369f64e8f";
        const API_NEWSDATA = "80cb37a29c47412d95f2ab981dab04c9";
        const url1 = `https://newsapi.org/v2/everything?q=${encodeURIComponent(
            searchValue
        )}&apiKey=${API_NEWSDATA}`;
        const url2 = `https://newsdata.io/api/1/latest?apikey=${API_NEWSAPI}&q=${encodeURIComponent(
            searchValue
        )}&language=en`;

        // Show loader before fetching
        this.newsList.innerHTML = "";
        this.showLoader();

        try {
            const [res1, res2] = await Promise.all([fetch(url1), fetch(url2)]);

            if (!res1.ok) throw new Error("NewsAPI failed");
            if (!res2.ok) throw new Error("NewsData.io failed");

            const data1 = await res1.json();
            const data2 = await res2.json();

            this.newsList.innerHTML = ""; // Clear loader before rendering content

            if (data1?.articles?.length) {
                this.renderNewsFromNewsAPI(data1.articles);
            } else {
                this.renderError("No articles from NewsAPI");
            }

            if (data2?.results?.length) {
                this.renderNewsFromNewsData(data2.results);
            } else {
                this.renderError("No articles from NewsData.io");
            }
        } catch (error) {
            this.newsList.innerHTML = ""; // Clear loader if error
            this.renderError(error.message);
        }
    }

    renderNewsFromNewsAPI(articles) {
        articles.forEach((article) => {
            const item = document.createElement("div");
            item.className = "newsItem";
            item.innerHTML = `
                <a href="${article.url}" target="_blank"> 
                    ${
                        article.urlToImage
                            ? `<img src="${article.urlToImage}" alt=""/>`
                            : ""
                    }
                    <h3>${article.title}</h3>
                    <p class="source">${article.source.name}</p>
                </a>
            `;
            this.newsList.appendChild(item);
        });
    }

    renderNewsFromNewsData(articles) {
        articles.forEach((article) => {
            const item = document.createElement("div");
            item.className = "newsItem";
            item.innerHTML = `
                <a href="${article.link}" target="_blank">
                    ${
                        article.image_url
                            ? `<img src="${article.image_url}" alt=""/>`
                            : ""
                    }
                    <h3>${article.title}</h3>
                    <p class="source">${article.source_id || "NewsData.io"}</p>
                </a>
            `;
            this.newsList.appendChild(item);
        });
    }

    renderError(message) {
        const errorItem = document.createElement("div");
        errorItem.className = "error";
        errorItem.innerText = message;
        this.newsList.appendChild(errorItem);
    }

    showLoader() {
        const loader = document.createElement("div");
        loader.className = "loader";
        loader.innerHTML = `<div class="spinner"></div>`;
        this.newsList.appendChild(loader);
    }
}

window.onload = () => new NewsAggregator();
