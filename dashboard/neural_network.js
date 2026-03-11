function drawConnections(ctx,nodes){

for(let i=0;i<nodes.length;i++){

for(let j=i+1;j<nodes.length;j++){

let dx=nodes[i].x-nodes[j].x;
let dy=nodes[i].y-nodes[j].y;

let dist=Math.sqrt(dx*dx+dy*dy);

if(dist<120){

ctx.beginPath();

ctx.moveTo(nodes[i].x,nodes[i].y);
ctx.lineTo(nodes[j].x,nodes[j].y);

ctx.strokeStyle="rgba(0,255,200,0.2)";
ctx.stroke();

}

}

}

}
