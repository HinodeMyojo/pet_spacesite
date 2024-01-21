const offersContainer = document.querySelector('.profile-offers');
const offers = document.querySelectorAll('.profile-offer');
let currentIndex = 0;

function updateDisplay() {
    offersContainer.scrollLeft = currentIndex * offers[0].offsetWidth;
}

document.getElementById('prevButton').addEventListener('click', () => {
    currentIndex = Math.max(currentIndex - 1, 0);
    updateDisplay();
});

document.getElementById('nextButton').addEventListener('click', () => {
    currentIndex = Math.min(currentIndex + 1, offers.length - 2); // Оставляем видимыми два элемента за раз
    updateDisplay();
});

updateDisplay();
