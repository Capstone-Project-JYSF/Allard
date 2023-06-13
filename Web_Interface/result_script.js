
const logoLink = document.getElementById("logo-link");

function redirectToHomePage(event) {
    event.preventDefault();
    // Replace "home.html" with the desired URL of the home page
    window.location.href = "index.html";
}

logoLink.addEventListener("click", redirectToHomePage);
