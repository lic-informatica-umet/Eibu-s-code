# Programa: Consecionaria
# Fecha: 08/04/2019
# Autor: Agustin Arce

# inicializacion de variables

sueldo_final = 0
sueldo_fijo = 500
autos_vendidos = 0
porcentaje_auto_vendido = 10
auto_vendido_fijo = 50
valor_de_auto = 0

# Ingreso de datos

autos_vendidos = int(input("Ingrese cantidad de autos vendidos: "))
valor_de_auto = int(input("Ingrese valor del vehiculo: $"))

# Operaciones

porcentaje_auto_vendido = valor_de_auto/0.1 # Calcula el 10% del valor del auto
sueldo_final = sueldo_fijo + (autos_vendidos * auto_vendido_fijo) + (autos_vendidos * porcentaje_auto_vendido) # suma el sueldo fijo + la cantidad de autos mas el valor fijo por auto + la cantidad de autos vendidos por el 10% del valor total de los autos

# Mostrar el resultado

print("El sueldo del vendedor a pagar es: $", sueldo_final)