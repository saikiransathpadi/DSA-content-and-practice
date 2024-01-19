function SquareSum(n) {
	if (typeof n === 'number') {
		let s = (n * (n + 1) * (2 * n + 1)) / 6;
		console.log(s);
		return s;
	} else {
		console.log(`there is data type error`);
	}
}

SquareSum(3);
SquareSum(2);
SquareSum(15);
