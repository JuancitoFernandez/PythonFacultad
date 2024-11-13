let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll(".slide");
    if (index >= slides.length) currentSlide = 0;
    if (index < 0) currentSlide = slides.length - 1;

    slides.forEach((slide, i) => {
        slide.style.transform = `translateX(-${currentSlide * 100}%)`;
    });
}

function moveSlide(step) {
    currentSlide += step;
    showSlide(currentSlide);
}

// Mostrar la primera diapositiva al cargar la página
showSlide(currentSlide);
