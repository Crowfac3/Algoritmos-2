"""
-----------------------------------------------------------------------------------------------
Título: TP00-03 - COBRO Y VUELTO
Fecha: 03-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Escribir un programa básico de caja, donde se ingrese el precio total de la compra, luego se ingrese el monto con el cual 
el cliente abona la compra, y finalmente informe con un mensaje si no es suficiente con lo que abonó o, caso contrario, 
informe el vuelto que se le debe dar al cliente.  

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

precioTotalCompra = float(input("Ingrese el precio total de la compra: "))
montoAbonado = float(input("Ingrese el monto que entrego el cliente: "))

if precioTotalCompra < montoAbonado:
    print("El vuelto del cliente es: $" , (montoAbonado - precioTotalCompra))
else:
    print("No alcanza para pagar el precio total de la compra")
