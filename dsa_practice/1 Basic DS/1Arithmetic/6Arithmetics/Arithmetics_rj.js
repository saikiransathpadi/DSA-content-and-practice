let fs = require('fs');
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1];
}

let x = +readLine();
let y = +readLine();

console.log(x + y)
console.log(x - y)
console.log(x * y)