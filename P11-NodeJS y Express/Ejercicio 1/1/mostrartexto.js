var http = require('http');

var server = http.createServer();

function mensaje(petic, resp){
    resp.writeHead(200,{'content-type':'text/plain'});
    resp.write('Experimento en nodejs   ');
    resp.write('<h2>aaaaaaaa</h2>');
    resp.write('\nSalto\nDe\nLINEA!');
    resp.write('\n¡men')
    resp.end();
}

server.on('request',mensaje);


server.listen(8000,function(){
    console.log('vaya a 127.0.0.1:8000');
});