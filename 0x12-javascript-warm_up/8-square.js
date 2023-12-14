#!/usr/bin/node

const process = require('process');
const m = parseInt(process.argv[2]);
const mes = 'Missing size';
if (isNaN(m)) {
  console.log(mes);
} else {
  for (let k = 0; k < m; k++) {
    console.log('X'.repeat(m));
  }
}

