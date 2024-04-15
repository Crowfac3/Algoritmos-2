"""
-----------------------------------------------------------------------------------------------
Título: TP01-02 | FECHA VÁLIDA
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción: Desarrollar una función que reciba tres números enteros positivos correspondientes al día, mes y año de una fecha, y 
verifique si corresponden a una fecha válida. Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años 
bisiestos. La función debe devolver True o False según la fecha sea correcta o no. Realizar también un programa para 
verificar el comportamiento de la función.

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


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if fechaValida(dia, mes, anio) == True:
    print("Es una fecha valida")
else:
    print("No es una fecha valida")
