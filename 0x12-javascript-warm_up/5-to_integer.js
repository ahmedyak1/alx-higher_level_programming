#!/usr/bin/node
const process = require('process');
let n;
let mes = 'Not a number';
if (process.argv.length > 2) {
  n = parseInt(process.argv[2]);
  if (!isNaN(n)) {
    n = String(n);
    mes = `My number: ${n}`;
  }
}
console.log(mes);

