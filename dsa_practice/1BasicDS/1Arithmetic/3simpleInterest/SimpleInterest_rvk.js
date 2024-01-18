let fs=require("fs");
let data=fs.readFileSync(0,'utf-8');
let idx=0;
data=data.split("\n");
function readLine(){
    idx++;
    return data[idx-1];
}
let P=parseInt(readLine());
let T=parseInt(readLine());
let R=parseInt(readLine());
let SI=parseInt(P*T*R/100);
console.log(SI);