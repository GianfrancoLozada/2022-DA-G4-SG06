// importar librería http
var express = require('express');

// crear servidor
var app = express();

// Creación de mensaje de respuesta cuando se reciba un solicitud
app.get('/',function(req, res){
 res.send('Hola Mundo desde Express');
})

app.get('/login',function(req, res){
    res.send('Aqui se muestra la pagina del login');
   })

// levantando servidor en puerto 3000 y configurando mensaje de confirmación
app.listen(3000,function(){
 console.log('La Aplicación esta funcionando en el puerto 3000');
});