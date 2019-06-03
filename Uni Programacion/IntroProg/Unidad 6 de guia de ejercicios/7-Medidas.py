# Programa: Medidas
# Fecha: 15/04/2019
# Autor: Agustin Arce

# inicializacion de variables

metros = 0
centimetros = 0
milimetros = 0

# Ingreso de datos

metros = float(input("Ingrese la medida en metros: "))

# Operaciones

centimetros = metros * 100
milimetros = metros * 1000

# Mostrar el resultado

print("En centimetros es:", centimetros)
print("En milimetros es:", milimetros)