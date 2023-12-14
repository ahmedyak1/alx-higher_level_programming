#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }


  /**
   * @property {method} print - sys out  rectangle with the character X
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


   /**
   * @property {method} rotate - exchanges the w and the h of the rectangle
   * @returns void
   */
  rotate () {
    const t = this.width;
    this.width = this.height;
    this.height = t;
  }

  /**
   * @property {method} double - multiples the w and the h rectangle * 2
   * @returns void
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
