#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0) {
      this.width = w;
    }
    if (typeof h === 'number' && h > 0) {
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      let j = 0;
      while (j < this.width) {
        rect += 'X';
        j++;
      }
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
