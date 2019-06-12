# Variables

numero = 0
cantidadpositivos = 0
cantidadnegativos = 0
cantidadceros = 0
sumapositivos = 0
sumanegativos = 0

# Inicio del prorama

while numero != 99:
	numero = int(input("Ingrese un numero: "))
	if numero == 99:
		break
	if numero > 0:
		cantidadpositivos += 1
		sumapositivos += numero
	elif numero < 0:
		cantidadnegativos += 1
		sumanegativos += numero
	else:
		cantidadceros += 1
print("La cantidad de positivos fue: ", cantidadpositivos)
print("La cantidad de negativos fue: ", cantidadnegativos)
print("La cantidad de ceros fue: ", cantidadceros)
print("La suma de numeros positivos es: ", sumapositivos)
print("La suma de numeros negativos es: ", sumanegativos)
print("El promedio de los numeros positivos es: ", sumapositivos / cantidadpositivos)