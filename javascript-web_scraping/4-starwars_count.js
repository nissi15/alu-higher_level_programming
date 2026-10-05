#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
