document.addEventListener("DOMContentLoaded", function () {
	const botonesContacto = document.querySelectorAll(".listado__plan--reserva");
	const modal = document.getElementById("modal");
	const cerrar = document.getElementById("cerrarModal");
	const overlay = document.getElementById("modalOverlay");

	botonesContacto.forEach((boton) => {
		boton.addEventListener("click", () => {
			modal.style.display = "block";
		});
	});

	cerrar.addEventListener("click", () => {
		modal.style.display = "none";
	});

	overlay.addEventListener("click", () => {
		modal.style.display = "none";
	});

	let currentSlide = 0;
	const slides = document.querySelectorAll(".slide");
	const totalSlides = slides.length;

	setInterval(() => {
		slides[currentSlide].classList.remove("active");
		currentSlide = (currentSlide + 1) % totalSlides;
		slides[currentSlide].classList.add("active");
	}, 4000);
});

window.onload = function () {
	if (!localStorage.getItem("cookiesAccepted")) {
		document.getElementById("cookie-banner").style.display = "block";
	}

	document.getElementById("accept-cookies").onclick = function () {
		localStorage.setItem("cookiesAccepted", "true");
		document.getElementById("cookie-banner").style.display = "none";
	};
};
