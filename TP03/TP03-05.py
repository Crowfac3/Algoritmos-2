"""
-----------------------------------------------------------------------------------------------
TP03-05
CINE DE BARRIO
04-2023
Hecho por: Adolfo German Garcia Bohl (1185420)

Desarrollar un programa con menú que permita realizar reservas en una sala de cine de barrio de N filas con M butacas
por cada fila. Desarrollar las siguientes funciones y utilizarlas en el mismo programa:

    Función cargarSala: recibirá la matriz como parámetro y la cargará con valores aleatorios para simular una sala
    con butacas ya reservadas.

    Función mostrarButacas: Mostrará por pantalla el estado de cada una de las butacas del cine. Esta función deberá
    ser invocada antes de que el usuario realice la reserva, y se volverá a invocar luego de la misma con los estados
    actualizados.

    Función reservar: Deberá recibir la matriz y la butaca seleccionada, y actualizará la matriz en caso de estar
    disponible dicha butaca. La función devolverá True/False si logró o no reservar la butaca

    Función butacasLibres: Recibirá como parámetro la matriz y retornará cuántas butacas desocupadas hay en la
    sala.

    Función butacasContiguas: Buscará la secuencia más larga de butacas libres contiguas en una misma fila y
    devolverá las coordenadas de inicio de la misma.

Al elegir cada opción de menú mostrar la sala o el dato calculado según corresponda. Antes de volver al menú detener el
programa y continuar con ENTER.

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


