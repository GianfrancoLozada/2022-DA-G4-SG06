//window
console.log("Window");
console.log(window.location);
console.log(window.location.href);
console.log(window.location.hostname);
console.log(window.location.host);
console.log(window.location.pathname);
console.log(window.location.protocol);
setTimeout(function() { 
    alert("Chocolate, ya pasaron 3 segundos");
    console.log("Ya paso 3 segundos");
}, 3000);

setTimeout(function(){ 
    console.log("Ahora pasaron 5");
  }, 5000); 
setInterval(function(){ 
    console.log("este mensaje se repetira cada 10 segundos");
  }, 10000);


localStorage.setItem('Nombre', 'Eduardo');
localStorage.getItem('Nombre');
localStorage.removeItem('Nombre');
localStorage.getItem('Nombre');

let referenciaObjetoVentana;
const strCaracteristicasVentana = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

function abrirPopupSolicitado() {
  referenciaObjetoVentana = window.open("https://virtual.ucsm.edu.pe/ultra/stream", "fCC_WindowName", strCaracteristicasVentana);
}

abrirPopupSolicitado();

//array
let mego = ["Icecream", "and shout", "And let it all out"];
console.log(mego.length);
let primero = mego[0]
let ultimo = mego[mego.length - 1]
console.log(primero);
console.log(ultimo);
mego.forEach(function(elemento, indice, array) {
    console.log(elemento, indice);
})
let nuevaLongitud = mego.push('before you go go');
console.log(nuevaLongitud[0]);

//Number
var a = new Number(98765);
var b = Number(98765);
console.log(a);
console.log(a instanceof Number);
console.log(b);
console.log(b instanceof Number);
console.log(Number("Pony"));
console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.MAX_VALUE);
console.log(Number.MIN_SAFE_INTEGER);
console.log(Number.MIN_VALUE);
console.log(Number.NEGATIVE_INFINITY);
console.log(Number.POSITIVE_INFINITY);
console.log(Number.isFinite(123));
console.log(Number.isFinite(Number.POSITIVE_INFINITY));
console.log(Number.isInteger(1));
console.log(Number.isInteger(1.1));
console.log(Number.isSafeInteger(98));
console.log(Number.isSafeInteger(999999999999999999999999));
