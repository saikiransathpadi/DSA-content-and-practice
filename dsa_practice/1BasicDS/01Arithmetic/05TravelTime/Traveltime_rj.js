let fs = require('fs');
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1];
}

let speed = +readLine();
let distance = 600
console.log(parseInt(distance/speed))