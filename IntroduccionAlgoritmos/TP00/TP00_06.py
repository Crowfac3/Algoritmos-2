"""
-----------------------------------------------------------------------------------------------
Título: TP00-06 - PROMEDIO DE CURSO 
Fecha: 03-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Realizar  un  programa  donde  se  vayan  ingresando  las  calificaciones  de  los  alumnos  de  un  curso.  Luego  de  ingresar  la 
calificación del último alumno, se ingresará un -1 para terminar la carga. El programa informará entonces la calificación 
promedio del curso.

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
def validarEntrada(textoCondicion, textoError, limiteInferior, limiteSuperior, condicionCorte):
    var = float(input(textoCondicion))
    while ((var < limiteInferior or var > limiteSuperior) and var != condicionCorte):
        print(textoError)
        var = float(input(textoCondicion))
    return var


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

#
# ENTRADA DE DATOS
#

calificacion = validarEntrada(
    "Ingrese -1 para terminar \nIngrese la calificacion del alumno: ",
    "La calificacion no puede ser menor que 0 o superior a 10", -1, 10, -1)
contadorAlumnos = 0
sumaCalificaciones = 0
while calificacion != -1:
    contadorAlumnos += 1
    sumaCalificaciones += calificacion
    print()
    print("Alumnos cargados:",contadorAlumnos)
    print()
    calificacion = validarEntrada(
        "Ingrese -1 para terminar \nIngrese la calificacion del alumno: ",
        "La calificacion no puede ser menor que 0 o superior a 10", -1, 10, -1)
print()
print("Se cargaron:",contadorAlumnos,"alumnos.")
if contadorAlumnos > 0:
    print("El promedio del curso es:",(sumaCalificaciones / contadorAlumnos))