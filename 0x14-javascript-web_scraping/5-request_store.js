#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// 1 argument is  url  to request
const baseURL = process.argv[2];
// 2 argument the file path to store the body response
const bodyResp = process.argv[3];
request(baseURL, (error, response, body) => {
  if (error == null) {
    fs.writeFileSync(bodyResp, body);
  }
});
