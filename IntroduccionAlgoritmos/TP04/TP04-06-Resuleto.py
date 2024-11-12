"""
-----------------------------------------------------------------------------------------------
Título: TP04-06
Fecha: 10-2023
Autor: nombre (legajo)

Descripción:
Escribir una función filtrarPalabras() que reciba una cadena de caracteres conteniendo una
frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres
de la cadena original. Escribir también un programa para verificar el comportamiento de la
misma. Hacer tres versiones de la función.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
# Utilizando ciclos normales y slicing. Sin utilizar el método split()
def filtrar_palabras_A(cadenaEntrada, largoMinimo):
    # VARIANTE 1 (sin slicing) ======================================
#     cadenaSalida = ""
#     cadenaAux = ""
#     contadorAux = 0
#     
#     for i in range(len(cadena)):
#         caracter = cadenaEntrada[i]
#         
#         if caracter != " ":
#             contadorAux += 1
#             cadenaAux += caracter
#         
#         else:
#             if contadorAux >= largoMinimo:
#                 cadenaSalida += cadenaAux + " "
# 
#             cadenaAux = ""
#             contadorAux = 0
#     else:
#         if contadorAux >= largoMinimo:
#             cadenaSalida += cadenaAux
# 
#     return cadenaSalida

    # VARIANTE 2 (con slicing) ======================================
    cadenaSalida = ""
    puntero = 0
    
    for i in range(len(cadena)):
        caracter = cadenaEntrada[i]
        
        if caracter == " ":
            if (i - puntero) >= largoMinimo:
                cadenaSalida += cadenaEntrada[puntero:i+1]

            puntero = i + 1
    else:
        if (i - puntero) >= largoMinimo:
            cadenaSalida += cadenaEntrada[puntero:i+1]

    return cadenaSalida



# Utilizando el método split() y listas por comprensión
def filtrar_palabras_B(cadenaEntrada, largoMinimo):
    palabras = cadenaEntrada.split(" ")
    
    cadenaSalida = [palabra for palabra in palabras if len(palabra) >= largoMinimo]
    
    return " ".join(cadenaSalida)



# Utilizando el método split() y la función filter() donde largoMinimo que es global es invocada desde un ámbito local
def filtrar_palabras_C(cadenaEntrada, largoMinimo):
    palabras = cadenaEntrada.split(" ")

    cadenaSalida = filter(fil, palabras)

    return " ".join(cadenaSalida)

def fil(palabra):
    if len(palabra) >= largoMinimo:
        return True
    else:
        return False



# Utilizando el método split() y la función filter() junto con una función lambda para manejar el parámetro larMin como local e independiente del global largoMinimo
def filtrar_palabras_D(_cadenaEntrada, _largoMinimo):
    palabras = _cadenaEntrada.split(" ")

    _cadenaSalida = filter(lambda palabra: largo(palabra, _largoMinimo), palabras)

    return " ".join(_cadenaSalida)

def largo(_pal, _larMin):
    return len(_pal) >= _larMin



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------
cadena = "texto de prueba para el ejercicio del trabajo práctico"
largoMinimo = 5


#-------------------------------------------------
# Procesos
#-------------------------------------------------
salidaA = filtrar_palabras_A(cadena, largoMinimo)
salidaB = filtrar_palabras_B(cadena, largoMinimo)
salidaC = filtrar_palabras_C(cadena, largoMinimo)
salidaD = filtrar_palabras_D(cadena, largoMinimo)


#-------------------------------------------------
# Resultados
#-------------------------------------------------
print(salidaA)
print(salidaB)
print(salidaC)
print(salidaD)
