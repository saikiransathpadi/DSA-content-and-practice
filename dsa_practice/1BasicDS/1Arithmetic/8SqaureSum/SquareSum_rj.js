let fs = require('fs');
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1];
}

let n = +readLine();
let i = 1
let result = 0;
while (i <= n) {
    result += i * i
    i++
}

console.log(result)