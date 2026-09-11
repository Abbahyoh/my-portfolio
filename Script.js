// Portfolio JavaScript

document.addEventListener("DOMContentLoaded", function () {

    // Welcome message in the browser console
    console.log("Welcome to King Abbahyoh's Portfolio!");

    // Smooth scrolling for links
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener("click", function (event) {
            const target = document.querySelector(this.getAttribute("href"));

            if (target) {
                event.preventDefault();
                target.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });

    // Project cards animation when clicked
    document.querySelectorAll(".card").forEach(function (card) {
        card.addEventListener("click", function () {
            this.style.transform = "scale(0.98)";

            setTimeout(() => {
                this.style.transform = "";
            }, 150);
        });
    });

    // Show current year if an element with id="year" exists
    const year = document.getElementById("year");

    if (year) {
        year.textContent = new Date().getFullYear();
    }

});