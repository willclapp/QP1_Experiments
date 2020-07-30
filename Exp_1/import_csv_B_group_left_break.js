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
	fs.writeFile('B_group_left_break/js/stims.js', buildOutput(word, coronal, labial, dorsal, assets), err => {
		if (err) {
			console.error(err)
		}
		console.log("stims.js written")
	})
}

// Getting read for trial
fs.createReadStream('B_group_left_break/trial_csv/exposure_B_group_left.csv')
	.pipe(csv())
	.on('data', data => {
		exposureResults.push(data)
		// This is just for preloading!
		assetPaths.push([
			'audio/exposure_B_group/' + data.path, 
		])
	})
	.on('end', () => {
		console.log('done reading exposure_B_group_left.csv')
		fs.createReadStream('B_group_left_break/trial_csv/test_B_group_left_coronal.csv')
			.pipe(csv())
			.on('data', data => {
				coronalResults.push(data)
				assetPaths.push([
					'audio/test/' + data.path, 
				])
			})
			.on('end', () => {
				console.log('done reading test_B_group_left_coronal.csv')
				fs.createReadStream('B_group_left_break/trial_csv/test_B_group_left_labial.csv')
					.pipe(csv())
					.on('data', data => {
						labialResults.push(data)
						assetPaths.push([
							'audio/test/' + data.path,
						])
					})
					.on('end', () => {
						console.log('done reading test_B_group_left_labial.csv')
						fs.createReadStream('B_group_left_break/trial_csv/test_B_group_left_dorsal.csv')
							.pipe(csv())
							.on('data', data => {
								dorsalResults.push(data)
								assetPaths.push([
									'audio/test/' + data.path,
								])
							})
							.on('end', () => {
								console.log('done reading test_B_group_left_dorsal.csv')
								writeResults(exposureResults, coronalResults, labialResults, dorsalResults, assetPaths)
						})
					})

			})
	})







