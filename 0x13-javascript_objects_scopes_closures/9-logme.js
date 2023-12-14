#!/usr/bin/node
/**
 * func prints number of arg before printed and the
 * new arg value
 * @param {item} str - arg of function
 * @returns void
 */
let nr = 0;
exports.logMe = function (item) {
  console.log(`${nr}: ${item}`);
  nr++;
};
