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
let output1=first_num+second_num;
let output2=first_num-second_num;
let output3=first_num*second_num;
console.log(output1);
console.log(output2);
console.log(output3);