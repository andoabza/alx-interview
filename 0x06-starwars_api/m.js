const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/' + 3;
  request(API_URL, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body.characters);
    console.log();
  });