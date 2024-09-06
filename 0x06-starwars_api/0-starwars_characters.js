#!/usr/bin/node
const request = require("request");
const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];

request(url, async function (error, response, body) {
    if (error) {
        console.error("error:", error);
    }
    const film = JSON.parse(body);
    for (const character of film.characters) {
        const res = await new Promise((resolve, reject) => {
            request(character, function (error, response, body) {
                if (error) {
                    reject(error);
                }
                resolve(JSON.parse(body));
            });
        });
        console.log(res.name);
    }
});
