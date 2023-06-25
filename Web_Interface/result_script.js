
const logoLink = document.getElementById("logo-link");

function redirectToHomePage(event) {
    event.preventDefault();
    // Replace "home.html" with the desired URL of the home page
    window.location.href = "index.html";
}

logoLink.addEventListener("click", redirectToHomePage);


// Retrieve the query parameters from the URL
const urlParams = new URLSearchParams(window.location.search);
const probability1 = urlParams.get('probability1');
const probability2 = urlParams.get('probability2');
const probability3 = urlParams.get('probability3');

// Update the text content of the probability elements
const probabilityElement1 = document.getElementById('probability1');
const probabilityElement2 = document.getElementById('probability2');
const probabilityElement3 = document.getElementById('probability3');


probabilityElement1.textContent = `${probability1}%`;
probabilityElement2.textContent = `${probability2}%`;
probabilityElement3.textContent = `${probability3}%`;
