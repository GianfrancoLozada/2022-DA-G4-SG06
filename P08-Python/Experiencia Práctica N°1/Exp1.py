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

#1c
def calculo(a=3,b=5):
        resul=a*b
        print(resul)

lista = (10,7)
calculo(*lista)
     
def mifuncion(a,b=2,c=3):
        print(a+b+c)
        
mifuncion(6,4)
mifuncion(5)
