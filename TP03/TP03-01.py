"""
-----------------------------------------------------------------------------------------------
TP03-01
FUNCIONES CON MATRICES Y MENÚ
05-2023
Hecho por: Adolfo German Garcia Bohl (1185420)

Desarrollar un programa que presente el siguiente menú de opciones:

SELECCIONE LA OPCIÓN DEL MENÚ
1  Generar matriz
2  Ordenar matriz
3  Intercambiar dos filas
4  Intercambiar dos columnas
5  Transponer matriz
6  Promedio de fila
7  Porcentaje de impares de columna
8  Verificación de simetría diagonal principal.
9  Verificación de simetría diagonal secundaria.
0 - Salir del programa
opción?:


Cada opción llamará a una función a desarrollar según las siguientes funcionalidades:

1. Cargar números enteros aleatorios de 0 a 99 en una matriz de N x N, ingresando la medida desde el teclado.
2. Ordenar en forma ascendente cada una de las filas de la matriz.
3. Intercambiar dos filas, cuyos números se reciben como parámetro.
4. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
5. Trasponer la matriz sobre sí misma. (intercambiar cada elemento Aij por Aji)
6. Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
7. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
8. Determinar si la matriz es simétrica con respecto a su diagonal principal.
9. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
0. Salir del programa usando exit()

Para operar el programa siempre primero se elegirá la opción 1 que llamará a una función para generar la matriz de
trabajo. La matriz de trabajo debe quedar en el ámbito global del programa para que pueda servir de argumento para
otras funciones. En el ámbito global también se debe crear una copia de la matriz de trabajo para mantener la matriz
original sin alteraciones. Al elegir la opción 1 se debe mostrar por pantalla la matriz generada.

Luego, al elegir cualquiera de las demás opciones del menú, se solicitarán datos de ser necesario, y luego se llamará a la
correspondiente función, para finalmente presentar la matriz original junto al resultado de la función invocada para poder
comprobar los cambios. Se deberá esperar a presionar ENTER para que vuelva a aparecer el menú de opciones,
codificando para esto input("Presione ENTER para continuar.")

NOTA: No incluir instrucciones “input” ni “print” dentro de las funciones.

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


