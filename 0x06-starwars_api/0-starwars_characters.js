#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const movieId = process.argv[2];

async function fetchStarWarsChars (movieId) {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
  let movieData = await (await request(apiUrl)).body;
  movieData = JSON.parse(movieData);
  const charUrls = movieData.characters;

  for (let i = 0; i < charUrls.length; i++) {
    const charUrl = charUrls[i];
    let charData = await (await request(charUrl)).body;
    charData = JSON.parse(charData);
    console.log(charData.name);
  }
}

fetchStarWarsChars(movieId);
