"""
-----------------------------------------------------------------------------------------------
Título: TP02-06 | ELEMENTOS ELIMINADOS
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Eliminar de una lista de números enteros aquellos valores que se encuentren en una segunda lista. Imprimir la lista
original, la lista de valores a eliminar y la lista resultante. La función deben modificar la lista original sin crear una copia
modificada.

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
def eliminarElementos(lista1, lista2):
    for elemento in lista2:
        if elemento in lista1:
            lista1.remove(elemento)
    return lista1

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
lista1 = []
lista2 = []

for i in range(random.randint(1,50)):
    lista1.append(random.randint(1,100))
for i in range(random.randint(1,50)):
    lista2.append(random.randint(1,100))

print("La lista original es: ")
print(lista1)
print()
print("La lista con valores a eliminar es:")
print(lista2)
print()
print("La lista resultante es:")
print(eliminarElementos(lista1,lista2))
