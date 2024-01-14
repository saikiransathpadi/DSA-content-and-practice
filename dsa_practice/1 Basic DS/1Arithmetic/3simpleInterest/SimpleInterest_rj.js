let fs = require('fs');
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1];
}

function simpleInterest(p, t, r) {
    si = (p * t * r) / 100
    return si
}

let p = parseInt(readLine());
let t = parseInt(readLine())
let r = +readLine()

console.log(simpleInterest(p, t, r))