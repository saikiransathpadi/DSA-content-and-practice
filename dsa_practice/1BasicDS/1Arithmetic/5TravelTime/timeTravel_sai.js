DISTANCE = 600 // In Kms

function calculateTime(speed) {
    return parseInt(DISTANCE / speed)
}


console.log(calculateTime(80));