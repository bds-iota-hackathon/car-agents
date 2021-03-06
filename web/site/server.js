var http = require('http');
var fileSystem = require('fs');

var server = http.createServer(function(req, resp){
	var filepath = '.' + req.url;
	if (filepath == "./") filepath = "./index.html";

	fileSystem.readFile(filepath, function(error, fileContent){
		if(error){
			resp.writeHead(500, {'Content-Type': 'text/plain'});
			resp.end('Error');
		}
		else{
			resp.writeHead(200, {'Content-Type': 'text/html'});
			resp.write(fileContent);
			resp.end();
		}
	});
});

server.listen(8888);

console.log('Listening at: localhost:8888');
