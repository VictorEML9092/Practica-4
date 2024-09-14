"""
Created on Monday 09/09/24

@author: Victor Mendoza
"""
import numpy as np

# Función para crear la matriz
def Crear_matriz(Alumnos, Materias):
    Calificaciones = np.random.randint(50, 101, size=(Alumnos, Materias))
    # Ajustar las opciones de impresión para mostrar toda la matriz
    np.set_printoptions(threshold=np.inf)
    print("\n",Calificaciones)

    Resp = input("\n¿Desea buscar un dato de la matríz? (Si/No) ")
    if Resp.lower() == "si":

        # Función para buscar un dato
        def Buscar_dato(Alumno, Materia):
            if 0 <= Alumno < Calificaciones.shape[0] and 0 <= Materia < Calificaciones.shape[1]:
                # Obtener el dato de la matriz
                Dato = Calificaciones[Alumno, Materia]
                print(f"\nLa calificación del alumno {Alumno + 1} en la materia {Materia + 1} es: {Dato}")
            else:
                print("Índices fuera de rango.")
        # Pedir el alumno y la materia
        Alumno = int(input("\nIngrese el número del alumno: "))
        Alumno -= 1
        while Alumno < 0:
            print("Error, intente de nuevo")
            Alumno = int(input("\nIngrese el número del alumno: "))
            Alumno -= 1

        Materia = int(input("\nIngrese el número de la materia: "))
        Materia -= 1
        while Materia < 0:
            print("Error, intente de nuevo")
            Materia = int(input("\nIngrese el número de la materia: "))
            Materia -= 1

    Buscar_dato(Alumno, Materia)
# Aquí se piden la cantidad de Alumnos y Materias para las dimensiones de la matriz
Alumnos = int(input("\nIngrese la cantidad de alumnos: "))
while Alumnos < 500:
    print("Mínimo deben ser 500 alumnos")
    Alumnos = int(input("\nIngrese la cantidad de alumnos: "))

Materias = int(input("\nIngrese la cantidad de materias: "))
while Materias < 6:
    print("Mínimo deben ser 6 materias")
    Materias = int(input("\nIngrese la cantidad de materias: "))

Crear_matriz(Alumnos, Materias)