async function loadStats(){

try{

let response = await fetch("api/stats.json")

let data = await response.json()

document.getElementById("capital").innerText = data.capital
document.getElementById("equity").innerText = data.equity
document.getElementById("profit_today").innerText = data.profit_today
document.getElementById("strategy").innerText = data.active_strategy
document.getElementById("market").innerText = data.market_regime
document.getElementById("ai_health").innerText = data.ai_health
document.getElementById("evolution_score").innerText = data.evolution_score
document.getElementById("mining_mode").innerText = data.mining_mode
document.getElementById("last_trade").innerText = data.last_trade

}catch(error){

console.log("Stats loading error:",error)

}

}



async function loadEvolution(){

try{

let response = await fetch("api/evolution.json")

let data = await response.json()

drawEvolution(data)

}catch(error){

console.log("Evolution loading error:",error)

}

}



function drawEvolution(data){

let canvas = document.getElementById("evolutionChart")

let ctx = canvas.getContext("2d")

ctx.clearRect(0,0,canvas.width,canvas.height)

let x = 50
let y = 150

data.forEach((node,index)=>{

ctx.beginPath()

ctx.arc(x,y,5,0,Math.PI*2)

ctx.fill()

ctx.fillText(node.score,x-5,y-10)

x += 50

y = 150 - (node.score * 50)

})

}



function startDashboard(){

loadStats()

loadEvolution()

}



setInterval(loadStats,2000)

setInterval(loadEvolution,5000)

startDashboard()
