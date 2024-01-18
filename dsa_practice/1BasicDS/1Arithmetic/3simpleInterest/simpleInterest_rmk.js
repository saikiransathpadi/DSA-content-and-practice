function simpleInterest(p, t, r) {
	if ((typeof p === typeof t) === (typeof r === typeof t)) {
		// console.log(typeof a === typeof b === typeof c);
		// console.log(b - a === c - b);
		let si = (p * t * r) / 100;
		console.log(si);
		return si;
	} else {
		console.log(`there might be data type error `);
	}
}

simpleInterest(1000, 10, 5);
simpleInterest(2000, 5, 3);
