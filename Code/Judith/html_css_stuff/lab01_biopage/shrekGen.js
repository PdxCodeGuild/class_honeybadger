//filename: shrekGen.js

var quotes = [
    "'It's not ogre, 'till it's ogre...'",
    "'This is my swamp, you're just living in it.'",
    "'Ogres are like onions.'",
    "'Onions have layers.'",
    "'You're better than they think you are.'"
]

function genQuote() {
    var randNum = Math.floor(Math.random() * (quotes.length));

    document.getElementById('quoteDisplay').innerHTML = quotes[randNum];
}