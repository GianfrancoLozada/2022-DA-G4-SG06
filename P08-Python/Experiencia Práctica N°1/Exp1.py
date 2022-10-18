#1a
mayor = 0
menor = 9999999999999999
lista = []
i=1
while i <= 6:
    num = int(input("Ingrese un numero:" ))
    if num not in lista:
        lista.append(num)
        i=i+1
    else:
        print("Este numero ya fue ingresado, intente otro:")

print("Los numeros del medio son: ",lista[2], " y ",lista[3])
print("El numero mayor es: ", max(lista))
print("El numero menor es: ", min(lista))

#1b
def es_primo(n):
if(n!=0):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True
num = 1
while(num!=0):
    num = int(input("Ingrese un numero: "))
    print(es_primo(num))
