nombre = 4 # declara a la varaible como tipo integro
print(isinstance(nombre, str)) # chequea si la variable "nombre" es del tipo string y lo muestra
if isinstance(nombre, str) == False: # si la instancia es false
    nombre = str(input()) # cambiar el valor de la variable nombre
print(isinstance(nombre, str)) # mostrar si el nuevo valor es un string