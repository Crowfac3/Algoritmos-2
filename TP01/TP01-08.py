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


def diasDelMes(mes, anio):
    if mes == 1:
        return 31
    elif mes == 2:
        if anioBisiesto(anio) == True:
            return 29
        else: return 28
    elif mes == 3: return 31
    elif mes == 4: return 30
    elif mes == 5: return 31  
    elif mes == 6: return 30
    elif mes == 7: return 31
    elif mes == 8: return 31
    elif mes == 9: return 30
    elif mes == 10: return 31
    elif mes == 11: return 30
    elif mes == 12: return 31
    

def anioBisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
mes = int(input("Ingrese el mes a mostrar: "))
anio = int(input("Ingrese el año a mostrar: "))
dias = 1

cantidadDeDias = diasDelMes(mes, anio)
primerDia = diaDeLaSemana(1, mes, anio)

print("Do\tLu\tMa\tMi\tJu\tVi\tSa")
for i in range(primerDia):
    print("\t", end="")
while dias <= cantidadDeDias:
    for i in range (primerDia, 7):
        print(dias,"\t", end="")
        dias += 1
        primerDia = 0
        if dias-1 == cantidadDeDias:
            break
    print()
    

