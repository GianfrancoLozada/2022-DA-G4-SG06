#4
archivo = open('NuevoTexto.txt', 'w')	               
lin = int(input('Ingresar numero de lineas del archivo: '))	               
i = 0	                
while i < lin:	                
    text = input('Ingresar texto: ')	                
    archivo.write(text + '\n')	               
    i = i + 1	                
archivo.close()