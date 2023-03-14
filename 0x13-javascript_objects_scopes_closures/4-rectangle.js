#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((typeof w === 'number' && w > 0) && (typeof h === 'number' && h > 0)) {
      this.width = w;
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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
