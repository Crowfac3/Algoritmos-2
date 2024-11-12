"""
-----------------------------------------------------------------------------------------------
Título: TP01-03 | GASTO DE TRANSPORTE SUBTE
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que 
dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita 
desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el 
total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.

Cantidad de viajes      Valor de 1 pasaje
1 a 20                  Averiguar en internet el valor actualizado
21 a 30                 20% de descuento
31 a 40                 30% de descuento
41 o más                40% de descuento

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
def gastosRealizados(cantidadViajes, precioPasaje):
    gasto = cantidadViajes * precioPasaje
    if cantidadViajes >= 21 and cantidadViajes <= 30:
        gasto = gasto * 0.80
    elif cantidadViajes >= 31 and cantidadViajes <= 40:
        gasto = gasto * 0.70
    elif cantidadViajes >= 41:
        gasto = gasto * 0.60
    return gasto



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
precioPasaje = 125

viajesRealizados = int(input("Ingrese la cantidad de viajes realizados: "))

if viajesRealizados > 0:
    gastoDeViajes = gastosRealizados(viajesRealizados, precioPasaje)
    print("El total gastado en viajes es: $", gastoDeViajes)
else:
    print("No puede haber viajes negativos")

