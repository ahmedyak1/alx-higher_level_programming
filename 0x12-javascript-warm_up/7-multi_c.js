#!/usr/bin/node

const process = require('process');
let not = parseInt(process.argv[2]);
const m1 = 'Missing number of occurrences';
const m2 = 'C is fun';
if (isNaN(not)) {
  console.log(m1);
} else {
  while (not > 0) {
    console.log(m2);
    not--;
  }
}

