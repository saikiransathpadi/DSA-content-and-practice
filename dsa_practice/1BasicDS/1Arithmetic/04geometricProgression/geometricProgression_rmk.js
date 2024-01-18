function geometricProgression(a, b, c) {
	if (
		(typeof a === typeof b) === (typeof c === typeof a) &&
		b / a === c / b
	) {
		let r = c / b;
		let d = c * r;
		console.log(d);
		return d;
	} else {
		console.log(`there might be data type error`);
	}
}

geometricProgression(2, 4, 8);
