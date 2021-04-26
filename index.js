const opn = require('open');
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("whats da code: ", function(e) {
    const url = `https://nhentai.net/g/${e}`;
    opn(url);
    console.log(url);
    rl.close();
});