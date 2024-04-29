"""
-----------------------------------------------------------------------------------------------
Título: TP02-05 | ELEMENTOS AL CUADRADO
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado.
Luego se solicita imprimir los últimos 10 valores de la lista.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------
def calcularCuadrados(numeroLimite):
    _cuadrados = []
    for i in range(1, numeroLimite + 1):
        _cuadrados.append(i ** 2)
    return _cuadrados


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
print("Calcular los cuadrados entre 1 y N")
numeroLimite = int(input("Ingrese N: "))

cuadrados = []

cuadrados = calcularCuadrados(numeroLimite)

print("Los ultimos 10 valores de la lista son: ")
print(cuadrados[-10:])



