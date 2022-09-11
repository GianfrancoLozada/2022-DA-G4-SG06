let nums = [23,46,69,102,125];
let strings = ['Mayonaise','escalator','is going up','so see ya later','button text']
let objetos = [{cuadrado:23*23, texto:"Macaco"},{cuadrado:46*46, texto:"Sopa"},{cuadrado:69*69, texto:"Bueno"},{cuadrado:102*102, texto:"Todos somos extraños"},{cuadrado:125*125, texto:"Sin ideas como siempre"}]

//probar los arrays (por accidente hice el iterador)
//for
for (i=0; i<objetos.length; i++){
    console.log("Lista de datos, columna" + i + ":\n Numero:" + nums[i] + "\n Cuadrado:" + objetos[i].cuadrado + "\n Letra:" + strings[i] + "\n Letra (Otra):" + objetos[i].texto)
}

//for each  SOLO nums
let index=0
nums.forEach(element => {
    console.log("Numero: " + element + " / Index: " + index++)
});

//while     SOLO strings
index = 0
while (true) {
    if (index == strings.length){
        break
    }
    console.log("Index: " + index + " / Texto: " + strings[index]);
    index++;
}

//do while  SOLO objeto
index = 0
do{
    if (index == objetos.length)
    break
    console.log("Index: " + index + " / cuadrado: " + objetos[index].cuadrado + " / texto: " + objetos[index].texto);
    index++;
}while(true)