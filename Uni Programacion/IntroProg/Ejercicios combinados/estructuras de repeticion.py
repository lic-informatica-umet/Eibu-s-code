# Programa: Aprobado o desaprobado
# Nombre: Agustin Arce
# Fecha: 13/05/2019

# Inicializacion de constantes

CANTIDAD_DE_NOTAS = 20

# Declaración de variables

nombre = ""
nota = 0
ciclo = 0

# ingreso y validación

while ciclo < CANTIDAD_DE_NOTAS:

    while nombre == "":
        nombre = str(input("Ingrese Nombre: "))
        if nombre == "":
            print("Ingrese un nombre valido.")

    while nota == 0:
        nota = int(input("Ingrese la nota: "))
        if nota < 0 or nota > 10:
            print("Ingrese un valor entre 1 y 10.")
            nota = 0

    if nota <= 3:
        print("El alumno:", nombre, "esta desaprobado")
    elif nota >= 4:
        print("El alumno:", nombre, "esta aprobado")

    nombre = ""
    nota = 0
    ciclo += 1