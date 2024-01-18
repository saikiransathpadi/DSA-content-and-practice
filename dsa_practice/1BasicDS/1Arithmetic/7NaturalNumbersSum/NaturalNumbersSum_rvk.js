let fs=require("fs");
let data=fs.readFileSync(0,'utf-8');
let idx=0;
data=data.split("\n");
function readLine(){
    idx++;
    return data[idx-1];
}
let input=parseInt(readLine());
let output=0;
for(let i=1;i<=input;i++){
    output+=i;
}
console.log(output);