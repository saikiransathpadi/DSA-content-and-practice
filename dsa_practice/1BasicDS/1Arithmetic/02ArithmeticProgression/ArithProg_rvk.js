let fs=require("fs");
let data=fs.readFileSync(0,'utf-8');
let idx=0;
data=data.split("\n");
function readLine(){
    idx++;
    return data[idx-1];
}
let first_num=parseInt(readLine());
let second_num=parseInt(readLine());
let third_num=parseInt(readLine());
let diff=second_num-first_num;
let output=third_num+diff;
console.log(output);