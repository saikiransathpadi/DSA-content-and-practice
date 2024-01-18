let fs=require("fs");
let data=fs.readFileSync(0,'utf-8');
let idx=0;
data=data.split("\n");
function readLine(){
    idx++;
    return data[idx-1];
}
let testcases=parseInt(readLine());
for(let i=0;i<testcases;i++){
    let input=readLine().split(" ");
    let x=parseInt(input[0]);
    let y=parseInt(input[1]);
    if(x>0 && y>0){
        console.log("Q1");
    }
    if(x<0 && y>0){
        console.log("Q2");
    }
    if(x<0 && y<0){
        console.log("Q3");
    }
    if(x>0 && y<0){
        console.log("Q4");
    }
}