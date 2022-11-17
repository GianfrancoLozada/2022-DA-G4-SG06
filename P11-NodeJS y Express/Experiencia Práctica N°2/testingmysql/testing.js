/*create database musicdb;*/

/*use musicdb;*/
/*CREATE TABLE Albums (
	Indexs integer NOT NULL AUTO_INCREMENT,
	Titulo varchar(255) NOT NULL,
	Banda_Compositor varchar(255) NOT NULL,
	PRIMARY KEY (Indexs)
);*/

/*Insert into Albums values 
(1, 'Balance Universal', 'VALV'),
(2, 'Make your mark', 'MLP');*/




// Solicitando paquete de Mysql
var mysql = require('mysql');
// Configurando parámetros de conexión (puede variar según instalación)
var conexion = mysql.createConnection({
    host:'localhost',
    port:'3306',
    database: 'musicdb',
    user: 'root',
    password: 'root',
});
// Realizando conexión o verificando si sucedió un error
conexion.connect(function(err){
    if(err){
        console.log("Error de conexion"+ err.stack);
        return;
    }
    console.log("Conectado al ID "+conexion.threadId);
});

conexion.query('select * from Albums', function(error,results){
    if(error)
        throw error;
    results.forEach(element => {
        console.log(element);
});
});
conexion.end();