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
    console.log("La tabla ha sido creada");
});

conexion.query('CREATE TABLE Personajes (Nombre varchar(255) NOT NULL,Rol varchar(255) NOT NULL,Personaje varchar(255) NOT NULL);', function(error,results){
    if(error)
        throw error;
});
conexion.end();