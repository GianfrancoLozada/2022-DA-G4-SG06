// Solicitando paquete de Mysql
var mysql = require('mysql');

var conexion = mysql.createConnection({
    host:'localhost',
    port:'3306',
    database: 'Historia',
    user: 'root',
    password: 'root',
});

conexion.connect(function(err){
    if(err){
        console.log("Error de conexion"+ err.stack);
        return;
    }
    console.log("Conectado al ID "+conexion.threadId);
});

conexion.query('select * from Personajes', function(error,results){
    if(error)
        throw error;
    results.forEach(element => {
        console.log(element);
});
});
conexion.end();