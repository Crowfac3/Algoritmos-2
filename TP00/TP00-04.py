"""
-----------------------------------------------------------------------------------------------
Título: TP00-04 - AUMENTO DE LÍMITES DE TARJETAS 
Fecha: 03-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Un banco necesita establecer los nuevos límites de crédito de sus tarjetas. Las de tipo 1 aumentarán un 25%; las de tipo 
2 aumentarán un 35%; las de tipo 3 aumentarán un 40%, y las de cualquier otro tipo aumentarán un 50%. Desarrollar un 
algoritmo para calcular el nuevo límite según el límite actual y el tipo de tarjeta del cliente. 

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
def validarEntrada(textoCondicion, textoError, limite):
    entrada = float(input(textoCondicion))
    while (entrada < limite):
        print(textoError)
        entrada = float(input(textoCondicion))
    return entrada


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

#
# ENTRADA DE DATOS
#
limiteActual = validarEntrada("Ingrese el limite actual del cliente: ","El limmite no puede ser menor a 0",0)
tipoTarjetaCliente = validarEntrada("Ingrese el tipo de la tarjeta del cliente: ","El tipo de tarjeta es incorrecto.",1)

if tipoTarjetaCliente == 1:
    limiteNuevo = limiteActual * 1.25
elif tipoTarjetaCliente == 2:
    limiteNuevo = limiteActual * 1.35
elif tipoTarjetaCliente == 3:
    limiteNuevo = limiteActual * 1.40
else:
    limiteNuevo = limiteActual * 1.5