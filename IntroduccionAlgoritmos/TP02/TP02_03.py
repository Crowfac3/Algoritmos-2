"""
-----------------------------------------------------------------------------------------------
Título: TP02-03 | ELEMENTOS NUMÉRICOS
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento,
imprimiendo lo que devuelve cada función luego de invocar a cada una de ellas:
    a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar
    de dos dígitos.
    b. Calcular y devolver el producto de todos los elementos de la lista anterior.
    c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la
    función lo recibe como parámetro. No utilizar listas auxiliares.
    d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa
    es [50, 17, 91, 17, 50].

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
def generarLista():
    """
    Genera una lista con numeros al azar de cuatro digitos. La cantidad tambien es un numero al azar de dos digitos
    """
    lista = []
    rango = random.randint(1,99)
    for i in range (rango):
        lista.append(random.randint(0,9999))
    return lista

def calcularElProducto(lista):
    productoTotal = 1
    for elemento in lista:
        productoTotal *= elemento
    return productoTotal

def eliminarUnValor (elemento, lista):
    while elemento in lista:
        lista.remove(elemento)
    return lista

def esCapicua(lista):
    largo = len(lista)

    for i in range(largo // 2):
        if lista[i] != lista[largo - i - 1]:
            return False
    return True


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
        print("[1] Generar una lista entre 1 y 99 elementos")
        print("[2] Calcular el producto de todos los elementos de la lista")
        print("[3] Eliminar un valor de la lista")
        print("[4] Verificar si una lista es Capicua")
        print("---------------------------")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3","4"): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

    if opcion == "0": # Opción salir del programa
        exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    elif opcion == "1":   # Opción 1
        listaNumeros = generarLista()
        print("Lista Generada!")
        print()
        print(listaNumeros)
    elif opcion == "2":   # Opción 2
        print("El producto de todos los elementos de la lista es:",calcularElProducto(listaNumeros))
    elif opcion == "3":   # Opción 3
        print(listaNumeros)
        print()
        valorParaEliminar = int(input("Ingrese el valor para eliminar: "))
        listaNumeros = eliminarUnValor(valorParaEliminar, listaNumeros)
        print(listaNumeros)
    elif opcion == "4":   # Opción 4
        if esCapicua(listaNumeros) == True:
            print("La lista es capicua")
        else:
            print("La lista no es capicua")

    input("\nPresione ENTER para volver al menú.")
    print("\n\n")
