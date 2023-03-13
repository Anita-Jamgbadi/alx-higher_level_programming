#!/usr/bin/node

if (parseInt(process.argv[2])) {
  let count = 0;
  const setValue = parseInt(process.argv[2]);
  while (count < setValue) {
    console.log('C is fun');
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}
