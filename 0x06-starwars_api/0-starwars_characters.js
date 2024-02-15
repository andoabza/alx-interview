#!/usr/bin/node
/* star wars api */
const request = require('request');

function getStarWarsCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/3/`;

  request({ url, json: true }, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      if (body.title) {
        body.characters.forEach((characterUrl, index) => {
          request({ url: characterUrl, json: true }, (error, response, characterBody) => {
            if (!error && response.statusCode === 200) {
              console.log(characterBody.name);
            } else {
              console.error(`Error fetching character ${index + 1}:`, error);
            }
          });
        });
      } else {
        console.error('No movie found with the given ID.');
      }
    } else {
      console.error('Error fetching movie data:', error);
    }
  });
}

getStarWarsCharacters(process.argv[2]);
