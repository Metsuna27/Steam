
const API_URL = "/api/v1/games";

const gamesContainer = document.getElementById("games-container");
const previousButton = document.getElementById("previous");
const nextButton = document.getElementById("next");
const pageInfo = document.getElementById("page-info");
const totalGames = document.getElementById("total-games");
const message = document.getElementById("message");

let currentPage = 1;
let totalPages = 1;
const limit = 12;

function createGameCard(game) {
    const card = document.createElement("article");
    card.className = "game-card";

    const image = document.createElement("img");
    image.src = game.image || "";
    image.alt = game.title || "Jeu Steam";
    image.loading = "lazy";

    const info = document.createElement("div");
    info.className = "game-info";

    const title = document.createElement("h3");
    title.textContent = game.title || "Sans titre";

    const year = document.createElement("p");
    year.textContent = `Sortie : ${game.release_year ?? "Inconnue"}`;

    const platforms = document.createElement("p");
    platforms.textContent = Array.isArray(game.platforms)
        ? game.platforms.join(", ")
        : "Plateformes inconnues";

    info.append(title, year, platforms);
    card.append(image, info);

    return card;
}

async function loadGames(page = 1) {
    const skip = (page - 1) * limit;

    message.textContent = "Chargement des jeux...";
    previousButton.disabled = true;
    nextButton.disabled = true;

    try {
        const response = await fetch(
            `${API_URL}?limit=${limit}&skip=${skip}`
        );

        if (!response.ok) {
            throw new Error(`Erreur HTTP ${response.status}`);
        }

        const data = await response.json();

        gamesContainer.replaceChildren();

        data.items.forEach(game => {
            gamesContainer.appendChild(createGameCard(game));
        });

        currentPage = page;
        totalPages = data.totalPages;

        pageInfo.textContent = `Page ${currentPage} / ${totalPages}`;
        totalGames.textContent = `${data.totalItems} jeux`;

        message.textContent = data.items.length === 0
            ? "Aucun jeu à afficher."
            : "";

        previousButton.disabled = currentPage <= 1;
        nextButton.disabled = currentPage >= totalPages;

    } catch (error) {
        message.textContent = `Impossible de charger les jeux : ${error.message}`;
        previousButton.disabled = true;
        nextButton.disabled = true;
    }
}

previousButton.addEventListener("click", () => {
    if (currentPage > 1) {
        loadGames(currentPage - 1);
    }
});

nextButton.addEventListener("click", () => {
    if (currentPage < totalPages) {
        loadGames(currentPage + 1);
    }
});

loadGames();
