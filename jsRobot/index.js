const robot = require('./robot/text.js')

const content = {
    "searchTerm": "Irlande",
    "lang"      : "fr",
    "sourceContentOriginal" : ""
}

async function start() {
    
    await robot(content)
}

start()