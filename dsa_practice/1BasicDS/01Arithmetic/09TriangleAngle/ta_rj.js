let fs = require('fs');
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1];
}

let a = +readLine();
let b = +readLine();
console.log(180 - (a + b));