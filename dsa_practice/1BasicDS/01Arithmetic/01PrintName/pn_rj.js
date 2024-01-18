let fs = require('fs');
let data = fs.readFileSync(0, 'utf-8');
let idx = 0
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1];
}

let str = readLine();
console.log( `Hello ${(str)}`); 

// Taking input form the text file, 
// if that is the case use the command "Get-content text_filename.txt | node code_filename.js"

// command for running the code without the input fiel "node PrintName_rj.js"