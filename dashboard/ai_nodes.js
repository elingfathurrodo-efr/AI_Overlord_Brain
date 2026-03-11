function generateNodes(count){

let nodes=[];

for(let i=0;i<count;i++){

nodes.push({

x:Math.random()*800,
y:Math.random()*400

});

}

return nodes;

}
