#!/usr/bin/node
/**
 * funct reverse  list
 * @param {list} list - list 
 * @returns {number} - reversed list
 */
exports.esrever = function (list) {
  const nl = [];
  for (let k = list.length - 1; k >= 0; k--) {
    nl.push(list[k]);
  }
  return nl;
};
