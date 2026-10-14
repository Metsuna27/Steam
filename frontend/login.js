const loginForm = document.getElementById("loginForm");
const registerBtn = document.getElementById("registerBtn");
const message = document.getElementById("message");

async function authenticate(endpoint) {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch(
            `/api/v1/users/${endpoint}`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email, password })
            }
        );

        const data = await response.json();

        if (!response.ok) {
            message.textContent =
                typeof data.detail === "string"
                    ? data.detail
                    : "Une erreur est survenue";
            return;
        }

        if (endpoint === "login") {
            // Démonstration : conservation du token
            sessionStorage.setItem(
                "token",
                data.access_token
            );

            window.location.href = "/";
        } else {
            message.textContent =
                "Compte créé ! Connectez-vous.";
        }

    } catch (error) {
        message.textContent =
            "Impossible de contacter le serveur.";
        console.error(error);
    }
}

loginForm.addEventListener("submit", (event) => {
    event.preventDefault();
    authenticate("login");
});

registerBtn.addEventListener("click", () => {
    authenticate("register");
});