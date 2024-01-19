function naturalNumbersSum(n) {
	if (typeof n === 'number') {
		let s = (n * (n + 1)) / 2;
		console.log(s);
		return s;
	} else {
		console.log(`there is data type error`);
	}
}

naturalNumbersSum(5);
naturalNumbersSum(3);
