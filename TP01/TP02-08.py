"""
-----------------------------------------------------------------------------------------------
Título: TP01-08 | DÍA DE LA SEMANA
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción: La siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma 
de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa 
para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes y año cualquiera basándose en 
la función suministrada. Considerar que la semana comienza en domingo.

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
def diaDeLaSemana (dia, mes, anio):
    """
    Funcion para calcular a que dia de la semana corresponde una fecha (0,1,2,3,4,5,6).
    PARAMETROS:
        dia, mes, anio: fecha para la cual obtener el dia de la semana.
    SALIDA:
        Entero indicando el dia de la semana (0,1,2,3,4,5,6) (0 = domningo)
    """
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diaSem = (((26 * mes -2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diaSem < 0:
        diaSem = diaSem + 7
    return diaSem


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
...

