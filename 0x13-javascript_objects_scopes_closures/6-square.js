#!/usr/bin/node

const SQUARE = require('./5-square');

class Square extends SQUARE {
  charPrint (c) {
    const chr = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let mySquare = '';
      let j = 0;
      while (j < this.width) {
        mySquare += chr;
        j++;
      }
      console.log(mySquare);
    }
  }
}

module.exports = Square;
