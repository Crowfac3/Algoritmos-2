"""
-----------------------------------------------------------------------------------------------
Título: TP02-02 | MES NÚMERO A TEXTO
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Escribir una función que reciba un número de mes y devuelva una cadena con el nombre del mes.
Probar la función desde un programa principal con un input para la entrada del número de mes, luego la llamada a la
función con dicho número como argumento, y finalmente un print de lo que la función devuelve.

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
def nombreDelMes(numero):
    LISTA_NOMBRE_MESES = ["Enero" , "Febrero" , "Marzo" , "Abril" , "Mayo" , "Junio" , "Julio" , "Agosto" , "Septiembre" , "Octubre" , "Noviembre" , "Diciembre"]
    return LISTA_NOMBRE_MESES[numero  - 1]
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

numeroDelMes = int(input("Ingrese el numero del mes 1-12: "))
print (nombreDelMes(numeroDelMes))

