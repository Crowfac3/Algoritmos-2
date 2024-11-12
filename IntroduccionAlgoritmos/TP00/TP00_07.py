"""
-----------------------------------------------------------------------------------------------
Título: TP00-07 - FORMAS DE PAGO 
Fecha: 03-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Escribir un programa que, ingresado el precio de lista de un producto, muestre cuanto le costará al cliente según todas 
las  opciones  de  pago  disponibles  (si  es  en  cuotas  además  del  precio  final  debe  mostrar  el  valor  de  cada  cuota).  Los 
descuentos o recargos según las formas de pago son los siguientes: 

En efectivo aplicar 10% de descuento 
Tarjeta 1 pago mantener el precio de lista 
Tarjeta 3 pagos recargar 5% 
Tarjeta 6 pagos recargar 10% 
Tarjeta 12 pagos recargar 15% 

Una vez mostrados los valores, el algoritmo debe esperar un nuevo ingreso, y sólo debe finalizar si se ingresa un precio 
de 0 pesos (en dicho caso debe terminar sin calcular nada). Se pide usar un tipo de bucle que evite tener que escribir el 
input dos veces.

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
def validarEntrada(textoCondicion, textoError, limite, condicionCorte):
    var = float((input(textoCondicion)))
    while ((var < limite) and var != condicionCorte):
        print(textoError)
        var = float(input(textoCondicion))
    return var


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

#
# ENTRADA DE DATOS
#

primeraVuelta = True
while(primeraVuelta == True or precio != 0):
    primeraVuelta = False
    precio = validarEntrada(
    "Ingrese 0 para terminar \nIngrese el precio de lista del producto: ",
    "El precio no puede ser menor a 0", 0, 0)
    print()
    if precio != 0:
        print("FORMA DE PAGO \t\tPRECIO TOTAL \t\tVALOR CUOTA")
        print("EFECTIVO \t\t${:.2f}".format(precio * 0.9))
        print("Tarjeta 1 pago: \t${:.2f}".format(precio))
        print("Tarjeta 3 pagos: \t${:.2f}\t\t${:.2f}".format(precio * 1.05, (precio * 1.05) / 3))
        print("Tarjeta 6 pagos: \t${:.2f}\t\t${:.2f}".format(precio * 1.1, (precio * 1.1) / 6))
        print("Tarjeta 12 pagos: \t${:.2f}\t\t${:.2f}".format(precio * 1.15, (precio * 1.15) / 12))
    print()
        