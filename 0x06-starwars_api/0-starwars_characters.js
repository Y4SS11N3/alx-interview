#!/usr/bin/node

const request = require('request');

// Check if movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api';

// Function to get character name from URL
function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`API request failed with status code ${response.statusCode}`));
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

// Main function to fetch and print character names
async function printCharacters (movieId) {
  try {
    const movieUrl = `${baseUrl}/films/${movieId}/`;
    const movieData = await new Promise((resolve, reject) => {
      request(movieUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode !== 200) {
          reject(new Error(`Movie not found. Status code: ${response.statusCode}`));
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    const characterPromises = movieData.characters.map(getCharacterName);
    const characterNames = await Promise.all(characterPromises);

    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Run the script
printCharacters(movieId);
