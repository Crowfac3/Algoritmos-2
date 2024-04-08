"""
-----------------------------------------------------------------------------------------------
Título: TP01-01 - MAYOR ENTRE TRES NÚMEROS
Fecha: 03-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor 
estricto).  En  caso  de  no  existir  el  mayor  estricto  devolver  -1.  No  utilizar  operadores  lógicos  (and,  or,  not).  Desarrollar 
también  un  programa  para  ingresar  los  tres  valores,  invocar  a  la  función  y  mostrar  el  máximo  hallado,  o  un  mensaje 
informativo si éste no existe.

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
def mayorEstricto(num1 , num2 , num3):
    """Funcion que recibe 3 numeros y devuelve el mayor solo si este es unico(mayor estricto) sino devuelve -1"""
    if num1 > num2:
        if num1 > num3:
            return num1
        elif num3 > num1:
            return num3
    if num2 > num1:
        if num2 > num3:
            return num2
        elif num3 > num2:
            return num3
    else:
        return -1

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if mayorEstricto(numero1 , numero2)


