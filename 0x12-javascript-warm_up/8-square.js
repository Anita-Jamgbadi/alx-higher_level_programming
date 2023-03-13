#!/usr/bin/node

if (parseInt(process.argv[2])) {
  const i = parseInt(process.argv[2]);

  for (let row = 0; row < i; row++) {
    let j = 0;
    let square = '';
    while (j < i) {
      square = square + 'X';
      j++;
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
