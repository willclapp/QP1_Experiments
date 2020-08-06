const fs = require('fs')
const csv = require('csv-parser')
let exposureResults = []
let testResults = []
let assetPaths = []

const buildOutput = (word, nonword, assets) => `
var exposure_stimuli = ${JSON.stringify(word, null, 2)}

var test_stimuli = ${JSON.stringify(nonword, null, 2)}

var assetPaths = ${JSON.stringify(assets.flat(), null, 2)}`




// This is which stims.js file is getting written
const writeResults = (word, nonword, assets) => {
	fs.writeFile('P_group_left/js/stims.js', buildOutput(word, nonword, assets), err => {
		if (err) {
			console.error(err)
		}
		console.log("stims.js written")
	})
}

// Getting read for trial
fs.createReadStream('P_group_left/trial_csv/exposure_P_group_left.csv')
	.pipe(csv())
	.on('data', data => {
		exposureResults.push(data)
		// This is just for preloading!
		assetPaths.push([
			'audio/exposure_P_group/' + data.path, 
		])
	})
	.on('end', () => {
		console.log('done reading exposure_P_group_left.csv')
		fs.createReadStream('P_group_left/trial_csv/test_P_group_left.csv')
			.pipe(csv())
			.on('data', data => {
				testResults.push(data)
				assetPaths.push([
					'audio/test/' + data.path, 
				])
			})
			.on('end', () => {
				console.log('done reading test_P_group_left.csv')
				writeResults(exposureResults, testResults, assetPaths)
			})
	})







