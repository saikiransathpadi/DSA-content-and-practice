function TravelTime(distance, time) {
	if (typeof distance === typeof time) {
		let speed = parseInt(distance / time);
		console.log(speed);
		return speed;
	} else {
		console.log(`there is a data type error`);
	}
}

TravelTime(600, 60);
TravelTime(600, 80);
