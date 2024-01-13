function arithmeticProgression(a, b, c) {
	if (
		(typeof a === typeof b) === (typeof c === typeof b) &&
		b - a === c - b
	) {
		// console.log(typeof a === typeof b === typeof c);
		// console.log(b - a === c - b);
		let diff = c - b;
		let d = c + diff;
		console.log(d);
		return d;
	} else {
		console.log(
			`there might be data type error or numbers might not be  in AP`
		);
	}
}

arithmeticProgression(1, 3, 5);
arithmeticProgression(0, 1, 8);
arithmeticProgression(100, 150, 200);
