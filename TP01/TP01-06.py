"""
-----------------------------------------------------------------------------------------------
Título: TP01-06 | CONCATENAR BÁSICO
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción: Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva el número que resulte de 
concatenar ambos valores. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades 
de Python no vistas en clase, ni tampoco concatenar strings mediante la conversión de número a cadena.


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
def concatenarNumero(numero1, numero2):
    multiplicador = 1
    esCero = False
    while esCero == False:
        if numero2 // multiplicador != 0:
            multiplicador *= 10
        else:
            esCero = True
    numero1 = numero1 * multiplicador
    return (numero1 + numero2)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero para concatenar: "))

print("El numero concatenado es:", concatenarNumero(numero1, numero2))

