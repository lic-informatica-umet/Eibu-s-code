'''
2. Codificar un programa que dado el precio unitario del producto calcule el IVA correspondiente (21% del precio).
'''

# Fecha: 15/04/2019
# Autor: Agustin Arce
# Programa: Calculo de IVA

# inicializacion de variables

precioUnitario = 0
precioIVA = 0
IVA = 0.21

# Ingreso de datos

precioUnitario = float(input("Ingrese el valor unitario del producto: $ "))

# Operaciones

precioIVA = precioUnitario * IVA

# Mostrar el resultado

print("El precio del IVA del producto es de: $", precioIVA)