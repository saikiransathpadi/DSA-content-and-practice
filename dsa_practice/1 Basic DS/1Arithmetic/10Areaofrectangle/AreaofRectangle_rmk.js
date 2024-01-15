function AreaofRectangle(a, b) {
	if (((typeof a === typeof b) === (typeof b === 'number') && a, b > 0)) {
		let Rarea = a * b;
		console.log(Rarea);
		return Rarea;
	} else {
		console.log(0);
	}
}

AreaofRectangle(5, 3);
AreaofRectangle(6, -5);
AreaofRectangle(0, 100);
