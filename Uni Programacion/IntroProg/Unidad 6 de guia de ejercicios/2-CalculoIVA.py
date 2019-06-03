# Programa: Calculo de IVA
# Fecha: 15/04/2019
# Autor: Agustin Arce

# inicializacion de variables

precioUnitario = 0
precioIVA = 0
IVA = 4.761904761904762

# Ingreso de datos

precioUnitario = float(input("Ingrese el valor unitario del producto: $ "))

# Operaciones

precioIVA = precioUnitario / IVA

# Redondeo

precioIVA = round(precioIVA, 2) # La funcion round() redondea el valor float por los digitos despues declarados

# Mostrar el resultado

print("El precio del IVA del producto es de: $", precioIVA)