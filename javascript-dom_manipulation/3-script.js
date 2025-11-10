document.getElementById("toggle_header").onclick = function () {
	const header = document.querySelector("header");
	header.classList.toggle("red");
	header.classList.toggle("green");
};