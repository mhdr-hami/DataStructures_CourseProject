function fix_dpi(canvasId) {
    //get DPI
    let dpi = window.devicePixelRatio;
    //get canvas
    let canvas = document.getElementById(canvasId);
    //get context
    let ctx = canvas.getContext('2d');
    //get CSS height
    //the + prefix casts it to an integer
    //the slice method gets rid of "px"
    let style_height = +getComputedStyle(canvas).getPropertyValue("height").slice(0, -2);
    //get CSS width
    let style_width = +getComputedStyle(canvas).getPropertyValue("width").slice(0, -2);
    //scale the canvas
    canvas.setAttribute('height', style_height * dpi);
    canvas.setAttribute('width', style_width * dpi);
}
var size = 25;
var colors = [
    "#000000", "reset", "#28fd25", "#212121", "#1B5E20", "#000000"
];

function Random(LastValue) {
    x = Math.floor(Math.random() * colors.length);
    while (x == LastValue) {
        x = Math.floor(Math.random() * colors.length);
    }
    return colors[x];
}
function shuffle0(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[0].length; j++) {
            do {
                arr[i][j] = Random(arr[i][j]);
            } while (arr[i][j] == "reset");
        }
    }
    var c = document.getElementById("c1");
    var ctx = c.getContext("2d");
    for (let i = 0; i < parseInt(arr.length); i++) {
        for (let j = 0; j < parseInt(arr[0].length); j++) {



            if (arr[i][j] == "reset") {
                ctx.beginPath();
                ctx.clearRect(j * size, i * size, (j + 1) * size, (i + 1) * size);
                ctx.fill();
            }
            else {
                ctx.beginPath();
                ctx.rect(j * size, i * size, (j + 1) * size, (i + 1) * size);
                ctx.fillStyle = arr[i][j];
                ctx.fill();
            }

        }
    }

}
function shuffle(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[0].length; j++) {
            if (arr[i][j] != "reset") {
                arr[i][j] = Random(arr[i][j]);
            }
        }
    }
    var c = document.getElementById("c1");
    var ctx = c.getContext("2d");
    for (let i = 0; i < parseInt(arr.length); i++) {
        for (let j = 0; j < parseInt(arr[0].length); j++) {



            if (arr[i][j] == "reset") {
                ctx.beginPath();
                ctx.clearRect(j * size, i * size, (j + 1) * size, (i + 1) * size);
                ctx.fill();
            }
            else {
                ctx.beginPath();
                ctx.rect(j * size, i * size, (j + 1) * size, (i + 1) * size);
                ctx.fillStyle = arr[i][j];
                ctx.fill();
            }

        }
    }

}
function fadeOut() {
    var timer = setInterval(shuffle, 1, arr);
    setTimeout(function () {
        clearInterval(timer);
        var c = document.getElementById("c1");
        var ctx = c.getContext("2d");

        ctx.beginPath();
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.fillStyle = "black";
        ctx.fill();
        c.style.display = "none";
    }, 2000);
}
$(document).ready(function () {
    $("#logInput").innerHTML = "";
    document.body.innerHTML += "<canvas id = 'c1' class = 'c1'>"
    fix_dpi("c1");
    var c = document.getElementById("c1");
    var ctx = c.getContext("2d");
    ctx.beginPath();
    ctx.rect(0, 0, c.width, c.height);
    ctx.fillStyle = "black";
    ctx.fill();
    var nx = parseInt(c.width / size);
    var ny = parseInt(c.height / size);
    arr = new Array(ny);
    for (let i = 0; i < arr.length; i++) {
        arr[i] = new Array(nx);
    }
    for (let i = 0; i < ny; i++) {
        for (let j = 0; j < nx; j++) {
            arr[i][j] = 0;
        }
    }
    shuffle0(arr);
    document.body.style.visibility = "visible";
    var time0 = setInterval(shuffle0, 10, arr);
    setTimeout(function () {
        clearInterval(time0);
        fadeOut();
    }, 4500);
    
    
});