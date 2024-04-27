"""
-----------------------------------------------------------------------------------------------
Título: TP00-05 - COMPRA TOTAL Y CANTIDAD
Fecha: 03-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
En un mercado los clientes pueden comprar sólo una unidad de cada producto. Realizar un programa que pida uno por 
uno los precios de los productos comprados por el cliente, y que al ingresar un precio igual a cero muestre el total  que 
debe abonar por la compra y la cantidad de productos comprados.

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

def validarEntrada(textoCondicion , textoError , limite , condicionCorte):
    var = float(input(textoCondicion))
    while (var < limite and var != condicionCorte):
        print(textoError)
        var = float(input(textoCondicion))
    return var

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

#
# ENTRADA DE DATOS
#


precio = validarEntrada("Ingrese 0 para salir \nSino ingrese el precio del producto: " , "El precio no puede ser menor que 0" , -1 , 0)
contadorProductos = 0
sumaTotal = 0
while precio != 0:
    contadorProductos += 1
    sumaTotal += precio
    print()
    print("Productos en el carrito:" , contadorProductos)
    print()
    precio = validarEntrada("Ingrese 0 para salir \nSino ingrese el precio del producto: " , "El precio no puede ser menor que 0" , -1, 0)
print()
print("Se abonaran" , contadorProductos , "de productos")
print("El total a abonar es:" , sumaTotal)
