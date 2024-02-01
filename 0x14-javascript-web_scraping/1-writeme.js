#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// The file path is the start point

const file = process.argv[2];

// The second argument is the string to write
const text = process.argv[3];
// The content be write

fs.writeFile(file, text, 'utf8', function (err, data) {
  //  In case of a reading error, the error object will be printed.
  if (err) {
    console.log(err);
  }
});
