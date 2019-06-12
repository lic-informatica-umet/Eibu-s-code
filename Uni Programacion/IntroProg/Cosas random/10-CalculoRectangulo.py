# Programa: Calculo de rectangulo
# Fecha: 08/04/2019
# Autor: Agustin Arce

# inicializacion de variables

base = 0
altura = 0
diagonal = 0
superficie = 0
perimetro = 0

# Ingreso de datos

base = float(input("Ingrese la base del rectangulo: ")) # Declara que el ingreso es float (por que el resultado de la diagonal puede ser con coma)

altura = float(input("ingrese la altura del rectangulo: "))

# Operacion diagonal

import math # Importa las funciones matematicas para llamar a la funcion math.sqrt()
diagonal = math.sqrt(base**2 + altura**2) # math.sqrt() calcula la raiz cuadrada del resultado interno

# Operacion superficio

superficie = base * altura # Multiplica base por altura para la superficie, el resultado es en m2

# Operacion perimetro

perimetro = (base + altura) * 2 # Suma los valores de la base y de la altura y los multiplica por dos, para abarcar el otro lado del rectangulo

# Muestra de resultados

print("La diagonal del rectangulo es:" , diagonal)
print("La superficie del rectangulo es:" , superficie, "m2")
print("El perimetro del rectangulo es:", perimetro)