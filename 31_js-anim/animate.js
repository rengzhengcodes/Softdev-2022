// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
// SoftDev pd0
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground");// GET CANVAS
var dotButton = document.getElementById("buttonCircle");// GET DOT BUTTON
var stopButton = document.getElementById("buttonStop");// GET STOP BUTTON

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
	clear(e);
	//repaint circle
	ctx.beginPath();
	ctx.arc(c.width/2, c.height/2, radius, 2 * Math.PI, false);
	ctx.fill();
	ctx.stroke();
	requestID = window.requestAnimationFrame();
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
	window.cancelAnimationFrame();
	// YOUR CODE HERE
	/*
		...to
		Stop the animation

		You will need
		window.cancelAnimationFrame()
	*/
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",	stopIt );
