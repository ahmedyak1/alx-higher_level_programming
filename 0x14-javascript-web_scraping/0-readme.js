#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// The file path is the start point.
const file = process.argv[2];
// The content be write
fs.readFile(file, 'utf8', function (err, data) {
  // In case of a reading error, the error object will be printed.
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
