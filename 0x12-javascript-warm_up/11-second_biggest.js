#!/usr/bin/node

const pro = require('process');
const argv = pro.argv;
const argc = pro.argv.length;
if (argc < 4) {
  console.log(0);
} else {
  const array = argv.slice(2).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}

