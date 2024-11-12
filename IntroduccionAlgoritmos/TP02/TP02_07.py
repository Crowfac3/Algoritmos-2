"""
-----------------------------------------------------------------------------------------------
Título: TP02-07 | VERIFICAR ORDEN DE ELEMENTOS
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente
o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función.

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
def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
listaOrdenada = [1, 2, 3]
listaDesordenada = ['b', 'a']
listaOrdenada2 = [4, 5, 6]
listaDesordenada2 = [3, 2, 1]

print("Lista ordenada:", listaOrdenada, "Resultado:", ordenada(listaOrdenada))
print("Lista desordenada:", listaDesordenada, "Resultado:", ordenada(listaDesordenada))
print("Lista ordenada:", listaOrdenada2, "Resultado:", ordenada(listaOrdenada2))
print("Lista desordenada:", listaDesordenada2, "Resultado:", ordenada(listaDesordenada2))
