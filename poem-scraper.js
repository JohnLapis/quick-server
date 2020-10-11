const request = require('request');
const cheerio = require('cheerio');
let url = "https://poemasinfantis.blogs.sapo.pt";

request(url, (error, response, body) => {
    const $ = cheerio.load(body);
    const limit = 4;
    const poems = $("#posts").children().slice(2, limit + 2).toArray();
    for(let poem of poems) {
        const textLines = $(".posttext", poem).text().trim().split("\n");
        const title = textLines.shift();
        const text = textLines.join("\n").trim();
        console.log(title);
        console.log();
        console.log(text);
        console.log("=====");
    }
});
