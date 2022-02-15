// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
// SoftDev pd0
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = // GET CANVAS
var dotButton = // GET DOT BUTTON
var stopButton = // GET STOP BUTTON

//prepare to interact with canvas in 2D
var ctx = // YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = // YOUR CODE HERE

var requestID;	//init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
	console.log("clear invoked...")

	// YOUR CODE HERE
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
	console.log("drawDot invoked...")

	// YOUR CODE HERE

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
