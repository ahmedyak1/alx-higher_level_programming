#!/usr/bin/node
const process = require('process');
const request = require('request');

// The first argumeent is the request URL

const url = process.argv[2];

request(url, function (error, response) {
  if (error == null) {
    // display the status code of a get request
    console.log(`code: ${response.statusCode}`);
  }
});
