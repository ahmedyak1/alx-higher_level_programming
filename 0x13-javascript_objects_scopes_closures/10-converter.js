#!/usr/bin/node
/**
 * funct 
 * @param {number} base - base exam
 * @returns {any} - converted number
 */
exports.converter = function (base) {
  function converted (number) {
    return number.toString(base);
  }
  return converted;
};
