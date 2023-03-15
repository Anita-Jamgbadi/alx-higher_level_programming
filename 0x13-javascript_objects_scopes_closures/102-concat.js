#!/usr/bin/node

const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

fs.readFile(sourceFilePath1, (err1, data1) => {
  if (err1) throw err1;

  fs.readFile(sourceFilePath2, (err2, data2) => {
    if (err2) throw err2;

    const concatenatedData = Buffer.concat([data1, data2]);

    fs.writeFile(destinationFilePath, concatenatedData, (err3) => {
      if (err3) throw err3;
    });
  });
});
