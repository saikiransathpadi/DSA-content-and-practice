let fs = require('fs');
let data = fs.readFileSync(0, 'utf-8');
let idx = 0
data = data.split('\n')

function readLine() {
    idx++
    return data[idx - 1]
}

function geoProg(a, b, c) {
    let r1 = b/a;
    let r2 = c/b;

    if(r1 = r2) {
        return r1;
    } else {
        console.log("invalid Pattern")
    }
}

let a = +readLine()
let b = +readLine()
let c = +readLine()

console.log(c * geoProg(a, b, c))