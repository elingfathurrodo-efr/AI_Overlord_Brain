async function loadStats(){

let response = await fetch("api/stats.json");

let data = await response.json();

document.getElementById("capital").innerText = data.capital;
document.getElementById("equity").innerText = data.equity;
document.getElementById("strategy").innerText = data.active_strategy;
document.getElementById("market").innerText = data.market_regime;
document.getElementById("evolution").innerText = data.evolution_score;

}

setInterval(loadStats,2000);
