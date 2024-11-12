"""
-----------------------------------------------------------------------------------------------
Título: TP02-11 | AZAR Y ELEMENTOS IMPARES
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que sean
impares. Imprimir las dos listas por pantalla.
• Programa TP02-11A: El proceso deberá realizarse utilizando listas por comprensión.
• Programa TP02-11B: El proceso deberá realizarse utilizando la función incorporada filter(). (investigarla)

Pendientes:
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
listaNumerosAleatorios = [random.randint(1,100) for i in range(100)]
impares = list(filter(lambda elemento: elemento % 2!= 0,listaNumerosAleatorios))

print("Lista de números aleatorios:")
print(listaNumerosAleatorios)
print("Lista de números impares:")
print(impares)
