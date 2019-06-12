'''
3. Modifique el programa anterior para además calcule el precio sin iva, y el precio con iva incluido. Muestre ambos por pantalla.
'''

# Fecha: 15/04/2019
# Autor: Agustin Arce
# Programa: Calculo de IVA V2

# inicializacion de variables

precioUnitario = 0
precioIVA = 0
precioConIVA = 0
precioSinIVA = 0
IVA = 0.21

# Ingreso de datos

precioUnitario = float(input("Ingrese el valor unitario del producto: $ "))

# Operaciones

precioIVA = precioUnitario * IVA
precioConIVA = precioUnitario + precioIVA
precioSinIVA = precioUnitario - precioIVA

# Mostrar el resultado

print("El precio del IVA del producto es de: $", precioIVA)
print("El precio del producto mas el IVA es de: $", precioConIVA)
print("El precio del producto menos el IVA es de: $", precioSinIVA)