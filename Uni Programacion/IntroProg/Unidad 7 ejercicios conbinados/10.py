'''
 Se ha corrido una maratón de 10(diez) participantes, y se tienen los tiempos en minutos que tardó cada uno de los participantes. 
 Dicho dato proviene de un sensor instalado en línea de llegada. Se necesita contar con la siguiente información: 
 
1. Cuál corredor llegó primero a la meta. 
2. Cuál corredor llegó en último lugar. 
3. Tiempo promedio. 
'''
# Declaracion de constante

CICLOSMAXIMO = 10

# Inicializacion de variables

corredor1_tiempo = 0
corredor2_tiempo = 0
corredor3_tiempo = 0
corredor4_tiempo = 0
corredor5_tiempo = 0
corredor6_tiempo = 0
corredor7_tiempo = 0
corredor8_tiempo = 0
corredor9_tiempo = 0
corredor10_tiempo = 0

nombre_corredor = ""

tiempo = 0
tiempo_promedio = 0

primer_corredor = ""
ultimo_corredor = ""

tiempomax = 0
tiempomin = 9999999

ciclo = 0

while ciclo != CICLOSMAXIMO:
    while tiempo == 0:
        print("Ingrese tiempo en minutos para los corredores.")
        tiempo = int(input())
        if tiempo < 0: 
            print("No se puede poner minutos negativos.")
            tiempo = 0

    if ciclo == 0:
        corredor1_tiempo = tiempo
        nombre_corredor = "Corredor 1"
    if ciclo == 1:
        corredor2_tiempo = tiempo
        nombre_corredor = "Corredor 2"
    if ciclo == 2:
        corredor3_tiempo = tiempo
        nombre_corredor = "Corredor 3"
    if ciclo == 3:
        corredor4_tiempo = tiempo
        nombre_corredor = "Corredor 4"
    if ciclo == 4:
        corredor5_tiempo = tiempo
        nombre_corredor = "Corredor 5"
    if ciclo == 5:
        corredor6_tiempo = tiempo
        nombre_corredor = "Corredor 6"
    if ciclo == 6:
        corredor7_tiempo = tiempo
        nombre_corredor = "Corredor 7"
    if ciclo == 7:
        corredor8_tiempo = tiempo
        nombre_corredor = "Corredor 8"
    if ciclo == 8:
        corredor9_tiempo = tiempo
        nombre_corredor = "Corredor 9"
    if ciclo == 9:
        corredor10_tiempo = tiempo
        nombre_corredor = "Corredor 10"

    if tiempo < tiempomin:
        tiempomin = tiempo
        primer_corredor = nombre_corredor
    if tiempo > tiempomax:
        tiempomax = tiempo
        ultimo_corredor = nombre_corredor

    ciclo = ciclo + 1
    tiempo = 0

tiempo_promedio = (corredor1_tiempo + corredor2_tiempo + corredor3_tiempo + corredor4_tiempo + corredor5_tiempo + corredor6_tiempo + corredor7_tiempo + corredor8_tiempo + corredor9_tiempo + corredor10_tiempo) / 10

print("El primer corredor en cruzar la meta es:", primer_corredor)
print("El ultimo corredor en cruzar la meta es:", ultimo_corredor)
print("El tiempo promedio fue de:", tiempo_promedio)
