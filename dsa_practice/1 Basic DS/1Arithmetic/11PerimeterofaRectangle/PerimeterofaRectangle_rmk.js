function PerimeterofaRectangle(l, b) {
	if (((typeof l === typeof b) === (typeof b === 'number') && l, b > 0)) {
		let Rperi = 2 * (l + b);
		console.log(Rperi);
		return Rperi;
	} else {
		console.log(0);
	}
}

PerimeterofaRectangle(7, 3);
PerimeterofaRectangle(4, -6);
PerimeterofaRectangle(24, 0);
