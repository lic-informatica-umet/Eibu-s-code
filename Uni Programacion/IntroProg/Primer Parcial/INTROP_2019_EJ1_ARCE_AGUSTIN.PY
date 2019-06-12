# Programa: Ejercicio practico 1
# Autor: Agustin Arce Martinez
# Fecha: 29/04/2019

# Inicializacion de Variables

nombre_alumno = 0
edad_alumno = 0
carrera_alumno = 0
eleccion_carrera = 0

# Ingreso de datos

nombre_alumno = input("Ingrese nombre del alumno: ")
edad_alumno = input("Ingrese la edad del alumno: ")
print("Elija la carrera:")
print("1 - Construcciones Inteligentes")
print("2 - Informatica")
print("3 - Economia" )

while True:
    try:
        eleccion_carrera = int(input("ingrese el numero de la carrera del alumno: "))
        if 1 < eleccion_carrera > 3: 
            raise ValueError 
        break
    except ValueError:
        print("El valor asignado no es valido")

# Control de flujo

if eleccion_carrera == 1:
    carrera_alumno = "Construcciones Inteligentes"
elif eleccion_carrera == 2:
    carrera_alumno = "Informatica"
elif eleccion_carrera == 3:
    carrera_alumno = "Economia"

# Muestra de informacion en pantalla

print("El alumno", nombre_alumno, "de", edad_alumno, "años de edad, esta en la carrera", carrera_alumno,".")