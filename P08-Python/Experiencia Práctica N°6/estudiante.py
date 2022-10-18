listaEstudiante = []

#Agregamos la Clase Estudiante
#Agregamos sus respectivos atributos
class Estudiante(object):
    def __init__(self, _codigo, _nombres, _apellidos, _edad, _curso1, _curso2, _curso3, _pension):
        self.codigo = _codigo
        self.nombres = _nombres
        self.apellidos = _apellidos
        self.edad = _edad
        self.curso1 = _curso1
        self.curso2 = _curso2
        self.curso3 = _curso3
        self.pension = _pension

    #Método ingresarDatos()
    def ingresarDatos():
        print("Registro de Estudiante\n")
        codigo = int(input("Ingrese el número de código: "))
        nombres = input("Ingrese los Nombres: ")
        apellidos = input("Ingrese los Apellidos: ")
        edad = int(input("Ingrese la Edad: "))
        curso1 = input("Ingrese el Curso 1: ")
        curso2 = input("Ingrese el Curso 2: ")
        curso3 = input("Ingrese el Curso 3: ")
        pension = False
        objAlumno = Estudiante(codigo, nombres, apellidos, edad, curso1, curso2, curso3, pension)
        listaEstudiante.append(objAlumno)

    #Método imprimirDatos()
    def imprimirDatos():
        print("Listado de Estudiante\n")
        for objAlumno in listaEstudiante:
            objAlumno.entregarDatos()
            input("Presione cualquier tecla para salir")

    #Método matricular()
    def matricular():
        Estudiante.ingresarDatos()
        print("¡Matrícula Exitosa!")
        input("Presione cualquier tecla para salir")

    #Método pagarPension()
    def pagarPension():
        print("Actualizar estado de pensión\n")
        codigo = int(input("Ingrese el número de código del estudiante a buscar: "))
        for objAlumno in listaEstudiante:
            if codigo == objAlumno.codigo:
                _pension = bool(input("Escribra 'True', si es que pagó y 'False' si es que no pagó: "))
                if _pension == True:
                    objAlumno.editarPension(_pension)
                objAlumno.entregarDatos()
                input("Presione cualquier tecla para salir")
            elif print("¡Número incorrecto!"):
                pass

    def editarPension(self, _pension):
        self.pension = _pension
        print("¡Registro Exitoso!") 

    def entregarDatos(self):
        print(" N° Código: {} \n Nombres: {} \n Apellidos: {} \n Cursos Matriculados: \n     Curso 1: {} \n     Curso 2: {} \n     Curso 3: {} \n     Pensión: {}".format(self.codigo, self.nombres, self.apellidos, self.curso1, self.curso2, self.curso3, self.pension))


def salir():
    print("Salida inminente...!")
    exit()

def main():
    while True:
        print("")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:")
        print("1.- Matricular un Nuevo Estudiante")
        print("2.- Mostrar Estudiantes")
        print("3.- Modificar Pensión")
        print("4.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            Estudiante.matricular()
        elif opcion == 2:
            Estudiante.imprimirDatos()
        elif opcion == 3:
            Estudiante.pagarPension()
        elif opcion == 4:
            salir()
        

if __name__ == '__main__':
    main()

    
