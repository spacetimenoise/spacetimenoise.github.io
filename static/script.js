// static/script.js

// Function to change the text when the button is clicked
function changeText() {
    const button = document.getElementById("myButton");
    button.textContent = "Text Changed!";
}

// Add an event listener to the button
document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("myButton");
    button.addEventListener("click", changeText);
});
