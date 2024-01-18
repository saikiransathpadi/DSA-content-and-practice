let fs = require('fs');
let data = fs.readFileSync(0,'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
    idx++;
    return data[idx - 1]
}

function arithmeticProg(a, b, c) {
    let d1 = b-a;
    let d2 = c-b;

    if(d1 === d2) {
        return d1
    } else {
        console.log("Invalid Pattern")
    }
}

let a = parseInt(readLine())
let b = +readLine()
let c = parseInt(readLine())

console.log(c + arithmeticProg(a, b, c)) //next number