#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  /**
   * @property {method} charPrint - sys out  rectangle with the character c
   * @returns void
   */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let k = 0; k < this.height; k++) {
      let squa = '';
      for (let m = 0; m < this.width; m++) {
        squa += c;
      }
      console.log(squa);
    }
  }
}
module.exports = Square;
