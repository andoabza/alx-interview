#!/usr/bin/node
/* star wars api */
const request = require('request');

function getStarWarsCharacters(movieId) {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    request({ url: url, json: true }, (error, response, body) => {
        if (!error && response.statusCode ===  200) {
            // Check if the movie exists
            if (body.title) {
                console.log(`Movie Title: ${body.title}`);
                // Fetch each character URL and print the character name
                body.characters.forEach((characterUrl, index) => {
                    request({ url: characterUrl, json: true }, (error, response, characterBody) => {
                        if (!error && response.statusCode ===  200) {
                            console.log(`Character ${index +  1}: ${characterBody.name}`);
                        } else {
                            console.error(`Error fetching character ${index +  1}:`, error);
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
