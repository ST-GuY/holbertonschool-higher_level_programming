#!/usr/bin/node

// Tableau contenant les lignes à afficher
const languages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

// Construire la chaîne finale avec une boucle
let output = ''; // chaîne temporaire pour stocker le résultat
for (let i = 0; i < languages.length; i++) {
  output += languages[i]; // ajouter la ligne
  if (i !== languages.length - 1) {
    output += '\n'; // ajouter un retour à la ligne sauf pour la dernière ligne
  }
}

console.log(output);

