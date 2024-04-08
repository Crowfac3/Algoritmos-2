"""
-----------------------------------------------------------------------------------------------
Título: TP00-02 - ASIENTOS DE CONFERENCIA
Fecha: 03-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Realizar  un  programa  que  permita  ingresar  la  cantidad  de  inscriptos  a  una  conferencia  y  la  cantidad  de  asientos 
disponibles en el auditorio. Se debe indicar si alcanzan los asientos. Si los asientos no alcanzan, indicar cuantos faltan para 
que todos los inscriptos puedan sentarse.  

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
...


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

#
# ENTRADA DE DATOS
#

cantidadInscriptos = int(input("Ingrese la cantidad de inscriptos a la conferencia: "))
cantidadAsientos = int(input("Ingrese la cantidad de asientos en el auditorio: "))

if cantidadInscriptos > cantidadAsientos:
    print("La cantidad de asientos no alcanza para la totalidad de los inscriptos")
    print("Faltarian",(cantidadInscriptos - cantidadAsientos),"asientos para que los inscriptos puedan sentarse.")
else:
    print("La cantidad de asientos es suficiente.")