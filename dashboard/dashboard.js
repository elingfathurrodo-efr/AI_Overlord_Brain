// =========================
// AI DASHBOARD CONTROLLER
// =========================

// =========================
// FETCH AI STATS
// =========================

async function loadStats(){

    try{

        let res = await fetch("../stats.json");

        let data = await res.json();

        document.getElementById("balance").innerText = data.balance;
        document.getElementById("equity").innerText = data.equity;
        document.getElementById("profit").innerText = data.profit;

    }catch(e){

        console.log("Stats error",e);

    }

}

// =========================
// FETCH ORGANISM STATE
// =========================

async function loadOrganism(){

    try{

        let res = await fetch("../organism_state.json");

        let data = await res.json();

        document.getElementById("energy").innerText = data.energy;
        document.getElementById("stress").innerText = data.stress;
        document.getElementById("growth").innerText = data.growth;

    }catch(e){

        console.log("Organism error",e);

    }

}


// =========================
// EVOLUTION DOTS
// =========================

function drawEvolution(){

    let canvas = document.getElementById("evolution_canvas");

    if(!canvas) return;

    let ctx = canvas.getContext("2d");

    ctx.clearRect(0,0,canvas.width,canvas.height);

    let dots = 60;

    for(let i=0;i<dots;i++){

        let x = Math.random()*canvas.width;
        let y = Math.random()*canvas.height;

        ctx.beginPath();
        ctx.arc(x,y,3,0,Math.PI*2);
        ctx.fillStyle="lime";
        ctx.fill();

    }

}


// =========================
// GENERATE AI NODES
// =========================

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


// =========================
// DRAW CONNECTIONS
// =========================

function drawConnections(ctx,nodes){

    for(let i=0;i<nodes.length;i++){

        for(let j=i+1;j<nodes.length;j++){

            let dx = nodes[i].x - nodes[j].x;
            let dy = nodes[i].y - nodes[j].y;

            let dist = Math.sqrt(dx*dx + dy*dy);

            if(dist < 120){

                ctx.beginPath();

                ctx.moveTo(nodes[i].x,nodes[i].y);
                ctx.lineTo(nodes[j].x,nodes[j].y);

                ctx.strokeStyle="rgba(0,255,200,0.2)";
                ctx.stroke();

            }

        }

    }

}


// =========================
// DRAW AI ORGANISM
// =========================

function drawOrganism(nodes){

    let canvas = document.getElementById("ai_brain");

    if(!canvas) return;

    let ctx = canvas.getContext("2d");

    ctx.clearRect(0,0,canvas.width,canvas.height);

    for(let n of nodes){

        ctx.beginPath();

        ctx.arc(n.x,n.y,4,0,Math.PI*2);

        ctx.fillStyle="cyan";

        ctx.fill();

    }

    drawConnections(ctx,nodes);

}


// =========================
// INITIALIZE AI VISUAL
// =========================

let nodes = generateNodes(40);


// =========================
// UPDATE LOOP
// =========================

setInterval(()=>{

    loadStats();

    loadOrganism();

    drawEvolution();

    drawOrganism(nodes);

},2000);
