var http = require('http')

var url = process.argv[2]

http.get(url, 'utf8', function (response) {
	response.on('data', function (data) {
	})

	response.on('end', function
})
