"""
-----------------------------------------------------------------------------------------------
Título: TP00-01 - AUTONOMÍA DE VEHÍCULO
Fecha: 03-2023
Autor: Alejandro Ariel Torres (legajo)

Descripción:
Calcula cuantos kilómetros puede recorrer un vehículo según la cantidad de litros de combustible
ingresados y el tipo de camino

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
litrosCombustible = int(input("Ingresa la cantidad de litros de combustible: "))
tipoCamino = input("Ingresa el tipo de camino [r=ruta, c=ciudad]: ")

#
# PROCESOS
#
if tipoCamino == "r":
    autonomia = litrosCombustible * 14.1
else:
    autonomia = litrosCombustible * 10.3 

#
# RESULTADOS
#
print()
print("La autonomía es de " + str(autonomia) + " kilómetros")
