// You Can Pick - Christopher Liu, Renggeng Zheng
// SoftDev pd1
// K32 -- DVD Screensaver
// 2022-02-17r

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground");// GET CANVAS
var dotButton = document.getElementById("buttonCircle");// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON
var dvdButton = document.getElementById("dvd");
//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");// YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "#0000ff"; // YOUR CODE HERE

var requestID;	//init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
	console.log("clear invoked...");
	ctx.clearRect(0, 0, c.width, c.height);
	// YOUR CODE HERE
};


var radius = 0;
var growing = true;

//var drawDot = function() {
var drawDot = () => {
	console.log("drawDot invoked...")
	// YOUR CODE HERE
	window.cancelAnimationFrame(requestID);
	clear(event);
	//repaint circle
	ctx.beginPath();
	ctx.arc(c.width/2, c.height/2, radius, 2 * Math.PI, false);
	ctx.fill();
	ctx.stroke();
	//growing/ shrinking
	if (growing) {
		radius += 1;
	} else {
		radius -= 1;
	}
	//growing and shrinking behavior
	if (radius <= 0) {
		growing = true;
	} else if (radius >= c.height/2 ) {
		growing = false;
	}
	requestID = window.requestAnimationFrame(drawDot); //tells it this is the function doing the animating, and to continue doing this function to continue the animation
	/*
		...to
		Wipe the canvas,
		Repaint the circle,

		...and somewhere (where/when is the right time?)
		Update requestID to propagate the animation.
		You will need
		window.cancelAnimationFrame()
		window.requestAnimationFrame()

	 */
};


//var stopIt = function() {
var stopIt = () => {
	console.log("stopIt invoked...")
	console.log( requestID );
	requestID = window.cancelAnimationFrame(requestID);
	// YOUR CODE HERE
	/*
		...to
		Stop the animation

		You will need
		window.cancelAnimationFrame()
	*/
};

let img = new Image(60, 40);
img.src = "logo_dvd_change.png";
let x = Math.floor(Math.random() * (c.width - img.width));
let y = Math.floor(Math.random() * (c.height - img.height));

let xVelo = -1;
let yVelo = Math.PI;

let hue = 90;

let dvd = () => {
	console.log("screensaving");
	requestID = window.cancelAnimationFrame(requestID);
	clear();
	ctx.beginPath();
	ctx.filter = `invert() saturate(50%) hue-rotate(${hue}deg)`;
	ctx.drawImage(img, x, y, img.width, img.height);
	ctx.filter = "none"; // so it doesn't affect other stuff

	if (x <= 0 || x >= c.width - img.width) {
		xVelo = -1 * xVelo;
		hue += 45;
		hue %= 360;
	}

	if (y <= 0 || y >= c.height - img.height) {
		yVelo = -1 * yVelo;
		hue += 45;
		hue %= 360;
	}

	x += xVelo;
	y += yVelo;

	requestID = window.requestAnimationFrame(dvd);
}

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",	stopIt );
dvdButton.addEventListener( "click",
function dvdSaver() {
	x = Math.floor(Math.random() * (c.width - img.width));
	y = Math.floor(Math.random() * (c.height - img.height));
	dvd();
});
