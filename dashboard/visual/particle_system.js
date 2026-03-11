const canvas = document.getElementById("aiCanvas");
const ctx = canvas.getContext("2d");

let particles = [];

function createParticle(){

    return {

        x: Math.random()*canvas.width,
        y: Math.random()*canvas.height,
        size: Math.random()*4+1,
        speedX: (
