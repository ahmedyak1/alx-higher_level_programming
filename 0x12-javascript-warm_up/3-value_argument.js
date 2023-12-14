#!/usr/bin/node

const process = require('process');
const m = 'No argument';
if (process.argv[2] === undefined) {
  console.log(m);
} else {
  console.log(process.argv[2]);
}

