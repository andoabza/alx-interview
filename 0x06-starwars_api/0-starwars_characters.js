//* #!/usr/bin/node
/* star wars api */
const request = require('request');
const arg = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;

const CharacterUrl = () => {
  request({ uri: url, json: true }, function (error, response, body) {
    if (error) {
      console.log('');
    }
    console.log(error);
    const char = body.characters;
    for (let i = 0; i in char; i++) {
      const charactersUrl = char[i];
      request({ uri: charactersUrl, json: true }, function (error, response, body) {
        if (error) {
          console.log('');
        }
        const name = body.name;
        console.log(name);
      });
    }
  });
};
setTimeout(CharacterUrl, 15);
CharacterUrl();
