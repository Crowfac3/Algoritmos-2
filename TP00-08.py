"""
-----------------------------------------------------------------------------------------------
Título: TP00-08 - PROMEDIO DE TEMPERATURAS
Fecha: 03-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Realizar  un  programa  que  solicite  la  carga  de  las  temperaturas  de  todos  los  días  de  enero  y  al  finalizar  devuelva  la 
temperatura promedio, máxima y mínima del mes. 

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
sumaTemperatura = 0

for i in range (1,31):
    while True:
        try:
            temperatura = float(input("Ingrese la temperatura: "))
            break
        except ValueError:
            print("Por favor, ingrese una temperatura correcta")
    
    sumaTemperatura += temperatura
    if i == 1:
        temperaturaMaxima = temperatura
        temperaturaMinima = temperatura
    elif temperatura > temperaturaMaxima:
        temperaturaMaxima = temperatura
    elif temperatura < temperaturaMinima:
        temperaturaMinima = temperatura

print("La temperatura promedio del mes es: " , round((sumaTemperatura / 31) , 2 ))
print("La temperatura Maxima registrada fue: " , round(temperaturaMaxima))
print("La temperatura Minima registrada fue: " , round(temperaturaMinima))

