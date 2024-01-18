function Arithmetics(a, b) {
	if (typeof a == typeof b) {
		let sum = a + b;
		let diff = a - b;
		let prod = a * b;
		console.log(sum);
		console.log(diff);
		console.log(prod);
		return sum, diff, prod;
	} else {
		console.log(`there is data type error`);
	}
}

Arithmetics(3, 2);
Arithmetics(2.5, 6.8);
