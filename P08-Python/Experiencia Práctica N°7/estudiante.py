import os
from time import time

def limpiar_pantalla():
    os.system("cls")

#Lista para los objetos
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
        self.historial = []

    #Método ingresarDatos()
    def ingresarDatos():
        limpiar_pantalla()
        print("Registro de Estudiante\n")
        codigo = int(input("Ingrese el número de código: "))
        nombres = input("Ingrese los Nombres: ")
        apellidos = input("Ingrese los Apellidos: ")
        edad = int(input("Ingrese la Edad: "))
        curso1 = input("Ingrese el Curso 1: ")
        curso2 = input("Ingrese el Curso 2: ")
        curso3 = input("Ingrese el Curso 3: ")
        pension = False
        #Creación de objetos de instancia
        objAlumno = Estudiante(codigo, nombres, apellidos, edad, curso1, curso2, curso3, pension)
        #Almacenamos los objetos de instancia en una lista
        listaEstudiante.append(objAlumno)

    def imprimirDatos():
        limpiar_pantalla()
        print("Listado de Estudiante\n")
        for objAlumno in listaEstudiante:
            print(objAlumno.nombreCompleto)
            objAlumno.entregarDatos()
            print(objAlumno.nombreCursos)
            input("Presione cualquier tecla para salir")
            limpiar_pantalla()

    def matricular():
        Estudiante.ingresarDatos()
        print("¡Matrícula Exitosa!")
        input("Presione cualquier tecla para salir")
        limpiar_pantalla()

    def pagarPension():
        limpiar_pantalla()
        print("Actualizar estado de pensión\n")
        codigo = int(input("Ingrese el número de código del estudiante a buscar: "))
        for objAlumno in listaEstudiante:
            if codigo == objAlumno.codigo:
                print(objAlumno.nombreCompleto)
                objAlumno.entregarDatosPension()
                pension = bool(input("Escribra 'True', si es que pagó o presione Enter si es que no pagó: "))
                objAlumno.editarPension(pension)
                print(objAlumno.nombreCompleto)
                objAlumno.entregarDatosPension()
                input("Presione cualquier tecla para salir")
                limpiar_pantalla()
            elif print("¡Número incorrecto!"):
                input("Presione cualquier tecla para salir")
                limpiar_pantalla()
                pass   

    def editarPension(self, _pension):
        self.pension = _pension

    #Agregamos métodos
    def entregarDatos(self):
        print(" No. codigo: {} \n Pensión: {} \n Cursos Matriculados: ".format(self.codigo, self.pension))

    def entregarDatosPension(self):
        print(" No. codigo: {} \n Pensión: {}".format(self.codigo, self.pension))
    
    def editarCursos(self, _curso1, _curso2, _curso3):
        self.curso1 = _curso1
        self.curso2 = _curso2
        self.curso3 = _curso3
        print("¡Registro Exitoso!")
        input("Presione cualquier tecla para salir")
        limpiar_pantalla()

    #Agregamos métodos estáticos
    @staticmethod
    def buscarEstudiante():
        limpiar_pantalla()
        print("Buscar Estudiante\n")
        codigo = int(input("Ingrese el número de código del estudiante a buscar: "))
        for objAlumno in listaEstudiante:
            if codigo == objAlumno.codigo:
                print(objAlumno.nombreCompleto)
                objAlumno.entregarDatos()
                print(objAlumno.nombreCursos)
                input("Presione cualquier tecla para salir")
                limpiar_pantalla()
            elif print("¡Número incorrecto!"):
                input("Presione cualquier tecla para salir")
                limpiar_pantalla()
                pass

    @staticmethod
    def modificarCursos():
        print("Modificar Cursos\n")
        codigo = int(input("Ingrese el número de código del estudiante a buscar: "))
        for objAlumno in listaEstudiante:
            if codigo == objAlumno.codigo:
                curso1 = input("Ingrese el Nuevo Curso 1: ")
                curso2 = input("Ingrese el Nuevo Curso 2: ")
                curso3 = input("Ingrese el Nuevo Curso 3: ")
                objAlumno.editarCursos(curso1, curso2, curso3)
                print("¡Rectificación de Matricula Exitosa!")
                objAlumno.entregarDatos()
                print(objAlumno.nombreCursos)
                input("Presione cualquier tecla para salir")
                limpiar_pantalla()
            elif print("¡Número incorrecto!"):
                input("Presione cualquier tecla para salir")
                limpiar_pantalla()
                pass

    #Agregamos Propiedades
    @property
    def nombreCompleto(self):
        return ' Nombre Completo del Estudiante: ' + self.apellidos + ', ' + self.nombres    

    @property
    def nombreCursos(self):
        return '   Curso N°1: ' + self.curso1 + '\n   Curso N°2: ' + self.curso2 + '\n   Curso N°3: ' + self.curso3
    

def salir():
    print("Salida inminente...!")
    input("Presione cualquier tecla para salir")
    limpiar_pantalla()
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
        print("3.- Buscar Estudiante")
        print("4.- Modificar Pensión")
        print("5.- Modificar Cursos")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            Estudiante.matricular()
        elif opcion == 2:
            Estudiante.imprimirDatos()
        elif opcion == 3:
            Estudiante.buscarEstudiante()
        elif opcion == 4:
            Estudiante.pagarPension()
        elif opcion == 5:
            Estudiante.modificarCursos()
        elif opcion == 6:
            salir()
        

if __name__ == '__main__':
    limpiar_pantalla()
    main()
