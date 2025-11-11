document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloDiv = document.getElementById('hello');
      helloDiv.textContent = data.hello; // affiche la traduction dans le div
    })
    .catch(error => {
      console.error('Erreur lors du fetch :', error);
    });
});
