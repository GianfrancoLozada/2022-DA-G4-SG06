

var mysql = require('mysql');

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

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

//Pedir datos:
rl.question("Escribe el nombre del personaje:",function(Nombre){
    rl.question("Escribe el rol del personaje:",function(Rol){
        rl.question("Escribe el tipo de personaje:",function(Personaje){
            
            

            conexion.query("insert into Personajes values ('"+Nombre+"','"+Rol+"','"+Personaje+"');", function(error,results){
                if(error)
                    throw error;
            });
            conexion.end();

            console.log("El personaje " + Nombre + " ha sido registrado")

            console.log("Para salir presione Ctrl + C")

        });
    });
});

