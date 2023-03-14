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
}
module.exports = Rectangle;
