file = open ("Prueba.txt", "w") 

file.write("Hola Mundo\n") 

file.write("Ing. de sistemas\n") 

nombre=input("introduce tu nombre: ") 

numero=int(input("Ingresa tu numero de celular: ")) 

file.write(nombre +"\n") 

file.write('% s' %numero+"\n") 

n=int(input("Numero de Elementos de la lista: ")) 

lista=[] 

for i in range (n): 

    x=input("Elemento: ") 

    lista.append(x) 

file.write('la lista es: =%s' %lista)    

file.close() 

file2 = "prueba2.dat" 

file2 = open ("Prueba2.dat", "wb") 

file2.write(b"Desarrollo de Aplicaciones") 

file2.write(b"Desarrollo de Aplicaciones") 