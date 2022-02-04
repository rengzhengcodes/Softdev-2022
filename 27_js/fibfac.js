// Team Z :: Mark Zhu, Renggeng Zheng
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn

function fact(n) {
	if (n <= 1) {
		return 1;
	} else {
		return n * fact(n-1);
	}
}

function fib(n) {
	if (n == 1) {
		return 1;
	} else {
		return n + fib(n-1);
	}
}
//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
