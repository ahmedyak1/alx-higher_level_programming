#!/usr/bin/node

/**
 * funct to nbr number of occu  list
 * @param {list} list - list 
 * @param {number} searchElement - element to look for
 * @returns {number} - number of occcr in a list
*
 */
exports.nbOccurences = function (list, searchElement) {
  let nbr = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      nbr++;
    }
  });
  return nbr;
};
