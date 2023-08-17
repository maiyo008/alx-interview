#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
    console.log('Please provide a movie ID as a command-line argument.');
    process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error('API request failed with status code:', response.statusCode);
        return;
    }
    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;
    if (charactersUrls.length === 0) {
        console.log('No characters found for this movie.');
        return;
    }
    fetchAndPrintCharacters(charactersUrls, 0);
});

function fetchAndPrintCharacters(urls, index) {
    if (index >= urls.length) {
        return;
    }
    const characterUrl = urls[index];
    request(characterUrl, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }
        if (response.statusCode !== 200) {
            console.error('API request failed with status code:', response.statusCode);
            return;
        }
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        fetchAndPrintCharacters(urls, index + 1);
    });
}
