# Programa: Calculo de IVA V2
# Fecha: 15/04/2019
# Autor: Agustin Arce

# inicializacion de variables

precioUnitario = 0
precioIVA = 0
precioConIVA = 0
precioSinIVA = 0
IVA = 4.761904761904762

# Ingreso de datos

precioUnitario = float(input("Ingrese el valor unitario del producto: $ "))

# Operaciones

precioIVA = precioUnitario / IVA
precioConIVA = precioUnitario + precioIVA
precioSinIVA = precioUnitario - precioIVA

# Redondeo

precioIVA = round(precioIVA, 2) # La funcion round() redondea el valor float por los digitos despues declarados
precioConIVA = round(precioConIVA, 2)
precioSinIVA = round(precioSinIVA, 2)

# Mostrar el resultado

print("El precio del IVA del producto es de: $", precioIVA)
print("El precio del producto mas el IVA es de: $", precioConIVA)
print("El precio del producto menos el IVA es de: $", precioSinIVA)