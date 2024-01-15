function TriangleAngle(a, b) {
	if ((typeof a === typeof b) === (typeof b === 'number') && a + b < 180) {
		let Tang = 180 - (a + b);
		console.log(Tang);
		return Tang;
	} else {
		console.log(
			`there might be data type errror or its not triangle angle`
		);
	}
}

TriangleAngle(30, 110);
TriangleAngle(150, 60);
