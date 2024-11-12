"""
-----------------------------------------------------------------------------------------------
TP03-03
MATRIZ ALEATORIA SIN REPETICIONES
04-2023
Hecho por: Adolfo German Garcia Bohl (1185420)

Desarrollar un programa para rellenar una matriz de N x N con números enteros al azar
comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz
por pantalla.

TODO:
- ...
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
tamanioMatriz = int(input("Ingrese el tamaño de la matriz: "))

# Se crea una lista con valores desde 0 hasta el tamaño de la matriz al cuadrado
valores = [x for x in range(0, tamanioMatriz ** 2)] 

# Se mezclan al azar los valores
random.shuffle(valores) 

# Se genera la matriz cargando los valores previamente mezclados
filas, columnas = tamanioMatriz, tamanioMatriz
matriz = []
for f in range (filas):
    matriz.append([])
    for c in range (columnas):
        matriz[f].append(valores[f * tamanioMatriz + c]) # Se toman de a uno los valores

# Se muestra la matriz
for fila in matriz:
    print(fila)


