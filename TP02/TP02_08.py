"""
-----------------------------------------------------------------------------------------------
Título: TP02-08 | LISTA NORMALIZADA
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Escribir una función que reciba una lista de números enteros como parámetro y la normalice, es decir que todos sus
elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar
también un programa que permita verificar el comportamiento de la función. Por ejemplo, normalizar([1, 1, 2]) debe
devolver [0.25, 0.25, 0.50].

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def normalizar(lista):
    nuevaLista = []
    suma = sum(lista)
    for elemento in lista:
        nuevaLista.append(elemento/suma)
    return nuevaLista

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
lista1 = [1, 1, 2]
lista2 = [1, 2, 3, 4]
lista3 = [10, 20, 30]


print("Lista original:", lista1, "Resultado:", normalizar(lista1))
print("Lista original:", lista2, "Resultado:", normalizar(lista2))
print("Lista original:", lista3, "Resultado:", normalizar(lista3))

