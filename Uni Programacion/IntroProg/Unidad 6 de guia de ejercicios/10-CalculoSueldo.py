# Programa: Calculo de sueldo
# Fecha: 15/04/2019
# Autor: Agustin Arce

# inicializacion de variables

sueldoBruto = 0
obraSocial = 0
jubilacion = 0
cuotaSindical = 0
sueldoNeto = 0

# Ingreso de datos

sueldoBruto = float(input("Ingrese sueldo bruto a calcular neto: $"))

# Operaciones

obraSocial = (sueldoBruto * 3) / 100
jubilacion = (sueldoBruto * 11) / 100
cuotaSindical = (sueldoBruto * 1) / 100
sueldoNeto = sueldoBruto - obraSocial - jubilacion - cuotaSindical

# Redondeo

sueldoNeto = round(sueldoNeto, 2)
obraSocial = round(obraSocial, 2)
jubilacion = round(jubilacion, 2)
cuotaSindical = round(cuotaSindical, 2)

# Mostrar el resultado

print("A partir del sueldo bruto: $", sueldoBruto)
print("Su sueldo neto es de: $", sueldoNeto)
print("El costo de la obra social es de: $", obraSocial)
print("El costo de la jubilacion es de: $", jubilacion)
print("El costo de la cuota sindical es de: $", cuotaSindical)