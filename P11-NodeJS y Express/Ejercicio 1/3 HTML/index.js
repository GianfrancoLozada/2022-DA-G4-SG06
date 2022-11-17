
var http = require('http'),
    fs = require('fs');

var html = fs.readFileSync("./index.html");

http.createServer(function(req,res){ 
    res.write(html);
    res.end();
}).listen(3500);
console.log('vaya a 127.0.0.1:3500');