function drawOrganism(canvasId,nodes){

let canvas=document.getElementById(canvasId);
let ctx=canvas.getContext("2d");

ctx.clearRect(0,0,canvas.width,canvas.height);

for(let n of nodes){

ctx.beginPath();

ctx.arc(n.x,n.y,4,0,Math.PI*2);

ctx.fillStyle="cyan";

ctx.fill();

}

drawConnections(ctx,nodes);

}
