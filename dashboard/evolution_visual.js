function drawEvolution(canvasId,level){

let canvas=document.getElementById(canvasId);
let ctx=canvas.getContext("2d");

ctx.clearRect(0,0,canvas.width,canvas.height);

for(let i=0;i<level;i++){

let x=Math.random()*canvas.width;
let y=Math.random()*canvas.height;

ctx.beginPath();
ctx.arc(x,y,3,0,Math.PI*2);
ctx.fillStyle="lime";
ctx.fill();

}

}
