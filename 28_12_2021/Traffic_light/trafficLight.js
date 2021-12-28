let button1 = document.getElementById("stopButton");
let button2 = document.getElementById("readyButton");
let button3 = document.getElementById("goButton");
let div1 = document.getElementById("stopLight");
let div2 = document.getElementById("readyLight");
let div3 = document.getElementById("goLight");

function redButton() {
    button1.style.backgroundColor = "#cf1124";
    div1.style.backgroundColor = "#cf1124";
    button2.style.backgroundColor = "#1f1d41";
    div2.style.backgroundColor = "#4b5069"
    button3.style.backgroundColor = "#1f1d41";
    div3.style.backgroundColor = "#4b5069";
}

function yellowButton() {
    button2.style.backgroundColor = "#f7c948";
    div2.style.backgroundColor = "#f7c948";
    button1.style.backgroundColor = "#1f1d41";
    div1.style.backgroundColor = "#4b5069"
    button3.style.backgroundColor = "#1f1d41";
    div3.style.backgroundColor = "#4b5069";
}

function greenButton() {
    button3.style.backgroundColor = "#199473";
    div3.style.backgroundColor = "#199473";
    button2.style.backgroundColor = "#1f1d41";
    div2.style.backgroundColor = "#4b5069"
    button1.style.backgroundColor = "#1f1d41";
    div1.style.backgroundColor = "#4b5069";
}