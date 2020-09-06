const fs = require('fs')
const csv = require('csv-parser')
let exposureResults = []
let coronalResults = []
let labialResults = []
let dorsalResults = []
let assetPaths = []

const buildOutput = (word, coronal, labial, dorsal, assets) => `
var exposure_stimuli = ${JSON.stringify(word, null, 2)}

var test_stimuli_cor = ${JSON.stringify(coronal, null, 2)}
var test_stimuli_lab = ${JSON.stringify(labial, null, 2)}
var test_stimuli_dor = ${JSON.stringify(dorsal, null, 2)}

var assetPaths = ${JSON.stringify(assets.flat(), null, 2)}`


// This is which stims.js file is getting written
const writeResults = (word, coronal, labial, dorsal, assets) => {
	fs.writeFile('P_right_D_first/js/stims.js', buildOutput(word, coronal, labial, dorsal, assets), err => {
		if (err) {
			console.error(err)
		}
		console.log("stims.js written")
	})
}

// Getting read for trial
fs.createReadStream('P_right_D_first/trial_csv/exposure_P_right.csv')
	.pipe(csv())
	.on('data', data => {
		exposureResults.push(data)
		// This is just for preloading!
		assetPaths.push([
			'audio/exposure_P/' + data.path, 
		])
	})
	.on('end', () => {
		console.log('done reading exposure_P_right.csv')
		fs.createReadStream('P_right_D_first/trial_csv/test_P_right_coronal.csv')
			.pipe(csv())
			.on('data', data => {
				coronalResults.push(data)
				assetPaths.push([
					'audio/test/' + data.path, 
				])
			})
			.on('end', () => {
				console.log('done reading test_P_right_coronal.csv')
				fs.createReadStream('P_right_D_first/trial_csv/test_P_right_labial.csv')
					.pipe(csv())
					.on('data', data => {
						labialResults.push(data)
						assetPaths.push([
							'audio/test/' + data.path,
						])
					})
					.on('end', () => {
						console.log('done reading test_P_right_labial.csv')
						fs.createReadStream('P_right_D_first/trial_csv/test_P_right_dorsal.csv')
							.pipe(csv())
							.on('data', data => {
								dorsalResults.push(data)
								assetPaths.push([
									'audio/test/' + data.path,
								])
							})
							.on('end', () => {
								console.log('done reading test_P_right_dorsal.csv')
								writeResults(exposureResults, coronalResults, labialResults, dorsalResults, assetPaths)
						})
					})

			})
	})









