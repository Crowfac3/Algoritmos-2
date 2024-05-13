"""
-----------------------------------------------------------------------------------------------
TP03-02
GENERACIÓN DE MATRICES CON PATRONES
05-2023
Hecho por: Adolfo German Garcia Bohl (1185420)

Para cada una de las siguientes matrices, desarrollar una función que la genere.

Escribir un programa con un menú que invoque a cada una de ellas y muestre por pantalla la matriz obtenida. El tamaño
de las matrices debe establecerse como N x N solicitando el valor por teclado, y las funciones deben servir para cualquier
valor ingresado. Antes de volver al menú detener el programa y continuar con ENTER.

a:  1   0   0   0       b:  0   0   0   27      c:  4   0   0   0
    0   3   0   0           0   0   9   0           3   3   0   0
    0   0   5   0           0   3   0   0           2   2   2   0
    0   0   0   7           1   0   0   0           1   1   1   1

d:  8   8   8   8       e:  0   1   0   2       f:  0   0   0   1
    4   4   4   4           3   0   4   0           0   0   3   2
    2   2   2   2           0   5   0   6           0   6   5   4
    1   1   1   1           7   0   8   0           10  9   8   7

g:  1   2   3   4       h:  1   2   4   7       I:  1   2   6   7
    12  13  14  5           3   5   8   11          3   5   8   13
    11  16  15  6           6   9   12  14          4   9   12  14
    10  9   8   7           10  13  15  16          10  11  15  16

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


