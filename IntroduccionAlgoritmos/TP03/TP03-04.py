"""
-----------------------------------------------------------------------------------------------
TP03-04
FÁBRICA DE BICICLETAS
04-2023
Hecho por: Adolfo German Garcia Bohl (1185420)

Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas en cada una de sus plantas durante
una semana. De este modo, cada columna representa el día de la semana (Lunes columna 0, Martes columna 1, etc.) y
cada fila representa a una de sus fábricas. Ejemplo:

                    (Lunes)     (Martes)    (Miercoles)     (Jueves)    (Viernes)   (sabado)
                        0           1           2               3           4           5
(fabrica 1) 0           23          150         20              120         25          150
(fabrica 2) 1           40          75          80              0           80          35
(...)                   ...         ...         ...             ...         ...         ...
(fabrica n) 3           80          80          80              80          80          80

Se solicita:

A. Crear una matriz con datos generados al azar de N fábricas durante una semana, considerando que la
    capacidad máxima de fabricación es de 150 unidades por día y puede suceder que en ciertos días no se
    fabrique ninguna. Mostrar la matriz por pantalla.
B. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
C. Mostrar cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
D. Mostrar cuál es el día más productivo, considerando todas las fábricas combinadas.
E. Crear una lista por comprensión que contenga la menor cantidad fabricada por cada fábrica. Mostrarla.


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


