
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

// Display the probabilities on the result page
const probabilitiesContainer = document.createElement('div');
probabilitiesContainer.innerHTML = `
  <p>Probability 1: ${probability1}</p>
  <p>Probability 2: ${probability2}</p>
  <p>Probability 3: ${probability3}</p>
`;
document.body.appendChild(probabilitiesContainer);
