"""
-----------------------------------------------------------------------------------------------
Título: TP01-05 | OBLONGOS Y TRIANGULARES
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción: Escribir dos funciones separadas que reciban un número natural y devuelvan verdadero o falso según el número sea de 
alguna de las siguientes categorías:

    Función oblongo(): Informa si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener 
    multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.

    Función triangular(): Informa si un número es triangular. Un número se define como triangular si puede expresarse 
    como la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número 
    triangular porque se obtiene sumando 1+2+3+4.

    Opcional: Desarrollar estas funciones pero bajo la forma de funciones lambda.


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
def esOblongo (numero):
    for i in range (1, numero - 1):
        if i * (i + 1) == numero:
            return True
    return False

def esTriangular (numero):
    suma = 0
    for i in range (1, numero // 2):
        suma += i
        if suma == numero:
            return True
    return False


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
numero = int(input("Ingrese el numero: "))
if esOblongo(numero) == True:
    print("El numero es Oblongo")
if esTriangular(numero) == True:
    print("El numero es Triangular")

