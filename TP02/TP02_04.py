"""
-----------------------------------------------------------------------------------------------
Título: TP02-04 | ELEMENTOS REPETIDOS
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no
debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.

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
def generarNumeroAleatorios(cantidad):
    lista = []
    for i in range (cantidad):
        lista.append(random.randint(1,100))
    return lista

def elementoRepetido(_lista):
    for i in range(len(_lista)):
        for j in range(i + 1, len(_lista)):
            if _lista[i] == _lista[j]:
                return True
    return False

def devolverElementosUnicos(_lista):
    """
    Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.
    """
    nuevaLista = []
    for elemento in _lista:
        if elemento not in nuevaLista:
            nuevaLista.append(elemento)
    return nuevaLista

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#----------------------------------------------------------------------------------------------
listaNumeros = []


#-------------------------------------------------
# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Generar una lista de N números aleatorios del 1 al 100 ")
        print("[2] La lista tiene algun parametro repetido?")
        print("[3] Devolver lista solo con elementos unicos")
        print("---------------------------")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3"): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

    if opcion == "0": # Opción salir del programa
        exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    elif opcion == "1":   # Opción 1
        cantidadDeNumero = int(input("Ingrese la cantidad de numero aleatorios: "))
        listaNumeros = generarNumeroAleatorios(cantidadDeNumero)
        print(listaNumeros)

    elif opcion == "2":   # Opción 2
        if elementoRepetido(listaNumeros) == True:
            print("La lista contiene elementos repetidos")
        else:
            print("La lista no contiene elementos repetidos")
    elif opcion == "3":   # Opción 3
        print("La lista con elementos unicos es:")
        print(devolverElementosUnicos(listaNumeros))

    input("\nPresione ENTER para volver al menú.")
    print("\n\n")



