#!/usr/bin/node
const request = require("request");
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    const result = await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) reject(err);
        else resolve(JSON.parse(body).name);
      });
    });
    console.log(result);
  }
});
