function Predictthequadrant(x, y) {
	if (x > 0 && y > 0) {
		console.log(`Q1`);
	} else if (x < 0 && y > 0) {
		console.log(`Q2`);
	} else if (x < 0 && y < 0) {
		console.log(`Q3`);
	} else if (x > 0 && y < 0) {
		console.log(`Q4`);
	}
}

Predictthequadrant(2, -9);
Predictthequadrant(1, 3);
