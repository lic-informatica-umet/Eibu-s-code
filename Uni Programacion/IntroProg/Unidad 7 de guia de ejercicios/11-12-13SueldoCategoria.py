# Programa: Sueldo categoria
# Fecha: 20/04/2019
# Autor: Agustin Arce

# Inicializacion de variables

horas = 0
valor = 0
categoria = 0
sueldo = 0

# Ingreso de datos

horas = int(input("Ingrese cantidad de horas trabajadas: "))
categoria = int(input("Ingrese la categoria del trabajador: "))

# Operaciones, Control de flujo

if categoria == 1:
    valor = 50
elif categoria == 2:
    valor = 70
elif categoria == 3:
    valor = 80
else:
    print("Ingrese una categoria existente.")

sueldo = valor * horas
print("El sueldo del empleado de categoria", categoria, "es de: $", sueldo)