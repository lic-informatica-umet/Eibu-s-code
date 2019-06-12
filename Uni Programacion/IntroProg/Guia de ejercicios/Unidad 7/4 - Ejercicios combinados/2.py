'''
Codifique un programa que permita determinar la situación de un alumno a partir de su nota
final de cursada. Se sabe que las situaciones son “Desaprobado” (nota inferior a 4),
“Aprobado” (nota entre 4 y 6,99) y “Sobresaliente” (nota igual o superior a 7).
'''

# Programa: Alumno, aprobacion
# Nombre: Agustin Arce
# Fecha: 27/05/2019

# Inicializacion de variables

notaAlumno = 0

# Ingreso de datos

while notaAlumno == 0:
    notaAlumno = float(input("Ingrese la nota del alumno: "))
    if notaAlumno < 1 or notaAlumno > 10:
        print("Ingrese un valor entre 1 y 10.")
        nota = 0

# Control de flujo

if notaAlumno <= 3.99:
    print("El alumno esta desaprobado")
elif 4 <= notaAlumno <= 6.99:
    print("El alumno esta aprobado")
elif notaAlumno >= 7:
    print("El alumno es sobresaliente")