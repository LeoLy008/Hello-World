var fs = require('fs')
var path = require('path')

function dirFileExtFilter(dir, ext, callback) {
	ext = '.' + ext
	fs.readdir(dir, function(err, fileList) {
		if (err) return callback(err)

		fileList = fileList.filter(function (file) {
			return path.extname(file) === ext
		})
		callback(null, fileList)
	})
}

module.exports = dirFileExtFilter

