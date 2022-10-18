dato = dict()
blanco = dict()

dato = {
    1:"Domicilio",
    10:"Albino",
    3:True,
    4:420,
    50:['Uno','Dos','Cuatro','Tres'],
    6:{'name':"Roberto", 'Number':12345},
}
dato2 = dict();
def prueba(Dict=dict()):
    if (len(Dict) != 0):
        print("\nINICIANDO METODO PARA MOSTRAR DATOS\n")
        PasoDeDatos(Dict.items())
        print("Fin de metodos\n\n\n")
    else:
        print("Añadir datos antes de empezar\n\n\n")

def Indicacion(var1,var2):
    print("Numero: ", var1, "\nDato: ", var2,"\nResultado de su metodo respectivo:\n")

def PasoDeDatos(lista):
    for k,v in lista:
        Indicacion(k,v)
        if (v == "Domicilio") or (v == "Albino"):
            print ("%s -> %s" %(k,v))
        if (k == 3):
            print (v)
            print ("\nPrueba que funciona dict como un booleano falso al no tener contenido:")
            if(blanco):
                print (True)
            else:
                print (False)
        if (k == 4):
            v = v - 200
            print (v)
        if (k == 'Ocho'):
            print(v)
            print((v/4))
        if (k == 50):
            print (v[0])
            print (v[1])
            print (v[3])
            print (v[2])
        if (k ==6) or (k==222):
            print(f'{v["name"]:10} || {v["Number"]:7} ||')
        print("----------------------------------")

def NuevoDato(Victima,Dir=222,Dato={'name':"Tomate", 'Number':9732}):
    Victima[Dir]=Dato
    return Victima

def repaso(datos):
    print("==============================")
    for k,v in datos:
        print ("%s -> %s" %(k,v))
    print("------------------------------")

prueba()        
prueba(dato)
prueba(dato2)
dato2 = dato
dato2 = NuevoDato(dato2)
dato2 = NuevoDato(dato2,'Ocho',212433516)
prueba(dato2)

repaso(dato.items())
repaso(dato2.items())
repaso(blanco.items())
