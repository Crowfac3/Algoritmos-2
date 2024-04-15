"""
-----------------------------------------------------------------------------------------------
Título: TP01-04 | BILLETES SEGÚN VUELTO
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción: Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que 
debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero 
recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que 
se minimice la cantidad de billetes. Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10. Emitir 
un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $3170 y se abona con $5000, el 
vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 billete de $200, 1 billete de $100 y 3 billetes de $10.


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
def cambioADevolver(totalCompra, dineroRecibido):
    billete5000 = 0
    billete1000 = 0
    billete500 = 0
    billete200 = 0
    billete100 = 0
    billete50 = 0
    billete10 = 0
    if totalCompra > dineroRecibido:
        print("El dinero recibido es insuficiente")
    else:
        cambio = dineroRecibido - totalCompra
        while cambio != 0:
            if cambio >= 5000:
                cambio -= 5000
                billete5000 += 1
            elif cambio >= 1000:
                cambio -= 1000
                billete1000 += 1
            elif cambio >= 500:
                cambio -= 500
                billete500 += 1
            elif cambio >= 200:
                cambio -= 200
                billete200 += 1
            elif cambio >= 100:
                cambio -= 100
                billete100 += 1
            elif cambio >= 50:
                cambio -= 50
                billete50 += 1
            elif cambio >= 10:
                cambio -= 10
                billete10 += 1
                
        print("El vuelto debe contener: ")
        if billete5000 > 0:
            print(billete5000, " billete/s de $5000")
        if billete1000 > 0:
            print(billete1000, " billete/s de $1000")
        if billete500 > 0:
            print(billete500, " billete/s de $500")
        if billete200 > 0:
            print(billete200, " billete/s de $200")
        if billete100 > 0:
            print(billete100, " billete/s de $100")
        if billete50 > 0:
            print(billete50, " billete/s de $50")
        if billete10 > 0:
            print(billete10, " billete/s de $10")



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
totalCompra = int(input("Ingrese el total de la compra: "))
cantidadRecibida = int(input("Ingrese la cantidad de dinero recibida: "))

cambioADevolver(totalCompra, cantidadRecibida)

