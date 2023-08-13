#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  const id = process.argv[2];
  const request = require('request');

  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const charactersArr = JSON.parse(body).characters;

      charactersArr.forEach(element => {
        request(element, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const char = JSON.parse(body).name;
            console.log(char);
          }
        });
      });
    }
  });
}
