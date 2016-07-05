/* hello 
console.log("HELLO WORLD")
*/

/* hint
var i = 2
var sum = 0
//console.log(process.argv)
for (; i < process.argv.length; ++i) {
	sum += Number(process.argv[i]);
}
console.log(sum)
*/

/* first I/O 
var fs = require('fs')
if (process.argv.length < 3) {
	console.log('require a file name as input parameter!!!')
	return
}
var content = fs.readFileSync(process.argv[2]).toString().split('\n')
console.log(content.length - 1)
*/

/* asynchronous I/O 
var fs = require('fs')
if (process.argv.length < 3) return
 
fs.readFile(process.argv[2], function (err, fileContents) {
	var lines = fileContents.toString().split('\n').length - 1
	console.log(lines)
})

/**/

/* much win 
var fs = require('fs')
if (process.argv.length < 4) return
fs.readdir(process.argv[2], function (err, fileList) {
	for (var idx = 0; idx < fileList.length; ++idx) {
		var tmp = fileList[idx].split('.')
		//console.log(tmp)
		//console.log('"'+tmp[tmp.length - 1] + '", "'+ process.argv[3] + '"',  tmp[tmp.length-1])
		if (tmp.length > 1 && tmp[tmp.length - 1] == process.argv[3]) {
			console.log(fileList[idx])
		}
	}
})
/*
     var fs = require('fs')  
     var path = require('path')  
       
     var folder = process.argv[2]  
     var ext = '.' + process.argv[3]  
       
     fs.readdir(folder, function (err, files) {  
       if (err) return console.error(err)  
       files.forEach(function(file) {  
           if (path.extname(file) === ext) {  
               console.log(file)  
           }  
       })  
     })  
/**/


/* modular */
var myModule = require('./fileNameFilter.js')
//console.log(myModule)
myModule(process.argv[2], process.argv[3], function (err, fileList) {
	if (err) return console.log(err)

	fileList.forEach(function(file) {
		console.log(file)
	})
})

/**/
