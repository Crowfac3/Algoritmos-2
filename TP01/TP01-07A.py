"""
-----------------------------------------------------------------------------------------------
Título: TP01-07 | DÍA SIGUIENTE
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción: Escribir una función diaSiguiente() que reciba como parámetro una fecha cualquiera expresada por tres enteros 
(correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes el día siguiente al dado. Utilizando 
esta misma función, sin modificaciones ni agregados, desarrollar programas que permitan:
• Programa TP01-07A: Sumar N días a una fecha.
• Programa TP01-07B: Calcular la cantidad de días existentes entre dos fechas cualesquiera

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
def fechaValida(dia, mes, anio):
    if dia < 1 or mes < 1 or mes > 12:
        return False
    else:
        if mes == 1 and dia <= 31:
            return True
        elif mes == 2:
            if anioBisiesto(anio) == True:
                if dia <= 29:
                    return True
            elif dia <= 28:
                return True
        elif mes == 3 and dia <= 31:
            return True
        elif mes == 4 and dia <= 30:
            return True
        elif mes == 5 and dia <= 31:
            return True
        elif mes == 6 and dia <= 30:
            return True
        elif mes == 7 and dia <= 31:
            return True
        elif mes == 8 and dia <= 31:
            return True
        elif mes == 9 and dia <= 30:
            return True
        elif mes == 10 and dia <= 31:
            return True
        elif mes == 11 and dia <= 30:
            return True
        elif mes == 12 and dia <= 31:
            return True
        else:
            return False
    

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

def diaSiguiente(dia,mes,anio):
    dia += 1
    if fechaValida(dia,mes,anio) == False:
        dia = 1
        mes += 1
        if fechaValida(dia,mes,anio) == False:
            mes = 1
            anio += 1
    return (dia,mes,anio)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

diasAgregar = int(input("Ingrese la cantidad de dias a sumar: "))

for i in range (diasAgregar):
    dia, mes, anio = diaSiguiente(dia, mes, anio)
print("La fecha con los dias agregados es: ",dia,"/",mes,"/",anio)

