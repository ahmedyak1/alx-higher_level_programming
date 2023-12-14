#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }


  /**
   * @property {method} print - prints the rectangle using the character X
   * @returns void
   */
  print () {
    for (let k = 0; k < this.height; k++) {
      let o = '';
      for (let m = 0; m < this.width; m++) {
        o += 'X';
      }
      console.log(o);
    }
  }
}

module.exports = Rectangle;
