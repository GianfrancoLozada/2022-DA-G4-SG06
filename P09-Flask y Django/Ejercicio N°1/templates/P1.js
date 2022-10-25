console.log("Window");
console.log(window.location);
console.log(window.location.href);
console.log(window.location.hostname);
console.log(window.location.host);
console.log(window.location.pathname);
console.log(window.location.protocol);

setTimeout(function() {
    alert("¡The best in the world!");
    console.log("1");
}, 2000);
setInterval(function(){
    alert("¡The World is Yours!");
    console.log("2");
}, 5000);
let referenciaObjetoVentana;
const strCaracteristicasVentana = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";
 
function myFunction() {
    var x = document.getElementById("mercedes").href;
    document.getElementById("demo").innerHTML = x;
}
