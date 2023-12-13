#!/usr/bin/node

const process = require('process');
let m;
if (process.argv.length === 3) {
  m = 'Argument found';
} else if (process.argv.length < 3) {
  m = 'No argument';
} else {
  m = 'Arguments found';
}
console.log(m);

