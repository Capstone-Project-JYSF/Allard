const startButton = document.getElementById("start-btn");
    
function redirectToAnotherPage() {
    window.location.href = "questionaires.html";
}

startButton.addEventListener("click", redirectToAnotherPage);