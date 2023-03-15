#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
