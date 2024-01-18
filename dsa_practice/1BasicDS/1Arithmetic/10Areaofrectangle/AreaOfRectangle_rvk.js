let fs=require("fs");
let data=fs.readFileSync(0,'utf-8');
let idx=0;
data=data.split("\n");
function readLine(){
    idx++;
    return data[idx-1];
}
let input1=parseInt(readLine());
let input2=parseInt(readLine());
console.log(input1*input2);