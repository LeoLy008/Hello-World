var fs = require('fs')

function countLine(fileName, output) {
		fs.readFile(fileName, 'utf-8', function (err, fileContents) {
				//console.log('file contents:' + fileContents)
				var lines = fileContents.split('\n').length - 1
				//console.log('lines:' + lines)
				output(lines)
		})
}

countLine(process.argv[2], function (lines) {
		console.log('file:[' + process.argv[2] + '] line count:' + lines)
})

console.log('Main done here!')


