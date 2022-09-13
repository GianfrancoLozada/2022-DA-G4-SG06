var answer = 42;
answer = 'Gracias por todo el pescado...';
console.log(answer)

//transformamos los valor a un sistema decimal
parseInt("F", 16);
parseInt("17", 8);
parseInt("15", 10);
parseInt(15.99, 10);
parseInt("FXX123", 16);
parseInt("1111", 2);
parseInt("15*3", 10);
parseInt("12", 13);
parseInt("Hello", 8);   // No es un número en absoluto
parseInt("0x7", 10);    // No es de base 10
parseInt("546", 2);     // Los dígitos no son válidos para representaciones binarias.


var howMany = 10;                                       // declramos howMany
alert("howMany.toString() is " + howMany.toString());   // Displays "10" alertas
alert("45 .toString() is " + 45 .toString());           // Displays "45" alertas
var x = 7;
alert(x.toString(2)) // Displays "111" realiza la transformacion al sistema binario
