#!/usr/bin/node
/* star wars api*/
const request =  require('request');
var arg = process.argv[1];
const url = "https://swapi-api.alx-tools.com/api/films/" + arg;

const character_url = () => {
    request({uri: url, json:true}, function(err, resp, body){
    let char = body.characters;
    for (let i = 0; i in char; i++) {
        let characters_url = char[i];
        request({uri: characters_url, json:true}, function(err, resp, body){
            let name = body.name;
            console.log(name);
        });
    
    }
});
}
setTimeout(character_url, 15)
character_url()