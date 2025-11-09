#!/usr/bin/node

// premier argument converti en entier
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  const output = [];
// boucle pour afficher "C is fun" x fois
  for (let i = 0; i < x; i++) {
    output.push('C is fun');
  }
  console.log(output.join('\n'));
}
