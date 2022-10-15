listaEstudiantes = []

#Agregamos la Clase Estudiante
#Agregamos sus respectivos atributos
class Estudiantes(object):
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

    def entregarDatos(self):
        print(" No. codigo: {} \n Nombres: {} \n Apellidos: {} \n Cursos Matriculados: \n     Curso 1: {} \n     Curso 2: {} \n     Curso 3: {} \n     Pensión: {}".format(self.codigo, self.nombres, self.apellidos, self.curso1, self.curso2, self.curso3, self.pension))
    
    def editarCursos(self, _curso1, _curso2, _curso3):
        self.curso1 = _curso1
        self.curso2 = _curso2
        self.curso3 = _curso3

    def editarPension(self, _pension):
        self.pension = _pension

        print("¡Registro Exitoso!")
    def incluirEvento(self, _curso1, _curso2, _curso3):
        return ("Rectificación de Matricula: Curso_1: {} Curso_2: {} Curso_3: {}".format(_curso1, _curso2, _curso3))
    
    def ingresarDatos():
        print("Registro de Estudiantes\n")
        codigo = int(input("Ingrese el número de código: "))
        nombres = input("Ingrese los Nombres: ")
        apellidos = input("Ingrese los Apellidos: ")
        edad = int(input("Ingrese la Edad: "))
        curso1 = input("Ingrese el Curso 1: ")
        curso2 = input("Ingrese el Curso 2: ")
        curso3 = input("Ingrese el Curso 3: ")
        pension = False
        objAlumno = Estudiantes(codigo, nombres, apellidos, edad, curso1, curso2, curso3, pension)
        listaEstudiantes.append(objAlumno)

    def imprimirDatos():
        print("Listado de Estudiantes\n")
        for objAlumno in listaEstudiantes:
            objAlumno.entregarDatos()
            input("Presione cualquier tecla para salir")


    def matricular():
        Estudiantes.ingresarDatos()
        print("¡Matrícula Exitosa!")
        input("Presione cualquier tecla para salir")

    def pagarPension():
        print("Actualizar estado de pensión\n")
        codigo = int(input("Ingrese el número de código del estudiante a buscar: "))
        for objAlumno in listaEstudiantes:
            if codigo == objAlumno.codigo:
                pension = bool(input("Escribra 'True', si es que pagó y 'False' si es que no pagó: "))
                objAlumno.editarPension(pension)
                objAlumno.entregarDatos()
                input("Presione cualquier tecla para salir")
            elif print("¡Número incorrecto!"):
                pass

    def buscarEstudiante():
        print("Buscar Estudiante\n")
        codigo = int(input("Ingrese el número de código del estudiante a buscar: "))
        for objAlumno in listaEstudiantes:
            if codigo == objAlumno.codigo:
                objAlumno.entregarDatos()
                input("Presione cualquier tecla para salir")
            elif print("¡Número incorrecto!"):
                pass

    def modificarCursos():
        print("Modificar Cursos\n")
        codigo = int(input("Ingrese el número de código del estudiante a buscar: "))
        for objAlumno in listaEstudiantes:
            if codigo == objAlumno.codigo:
                curso1 = input("Ingrese el Nuevo Curso 1: ")
                curso2 = input("Ingrese el Nuevo Curso 2: ")
                curso3 = input("Ingrese el Nuevo Curso 3: ")
                objAlumno.editarCursos(curso1, curso2, curso3)
                objAlumno.entregarDatos()
                input("Presione cualquier tecla para salir")
            elif print("¡Número incorrecto!"):
                pass
 

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
        print("3.- Buscar Estudiante")
        print("4.- Modificar Pensión")
        print("5.- Modificar Cursos")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            Estudiantes.matricular()
        elif opcion == 2:
            Estudiantes.imprimirDatos()
        elif opcion == 3:
            Estudiantes.buscarEstudiante()
        elif opcion == 4:
            Estudiantes.pagarPension()
        elif opcion == 5:
            Estudiantes.modificarCursos()
        elif opcion == 6:
            salir()

if __name__ == '__main__':
    main()

